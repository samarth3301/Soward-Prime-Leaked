from __future__ import annotations
import discord_android
import asyncio
import json
import os
import random

import aiohttp
import discord
import motor.motor_asyncio as motor
from discord.ext import commands, tasks
from rich.console import Console

from cogs._tick import main, ticket_launcher
from prince.ui import ButtonSelfRoleView, DropDownSelfRoleView

console = Console()
toolbar_width = 40
from utils.Tools import *

from .classes import Profile

os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_EMBEDDED_JSK"] = "True"

TOKEN = ""
MONGO_DB_URL = "mongodb+srv://Sowardprime:nxtontop@cluster0.aoy4vww.mongodb.net/?retryWrites=true&w=majority"

OWNERS = [151302260490502144]


default_prefix = "?"


def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        idk = json.load(f)
    with open("nonprefix.json", "r") as f:
        member = json.load(f)
    if str(message.author.id) in member["access"]:
        return "", "?"
    elif str(message.guild.id) not in idk:
        return f"{default_prefix}"
    else:
        idkprefix = idk[str(message.guild.id)]
        return f"{idkprefix}"


class Bot(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            command_prefix=self.get_prefix,
            case_insensitive=True,
            intents=discord.Intents.all(),
            help_command=None,
            shard_count=2,
            chunk_guilds_at_startup=False,
            owner_ids=OWNERS,
            strip_after_prefix=True,
           
            max_messages=5000,
            allowed_mentions=discord.AllowedMentions(
                everyone=False, replied_user=False, roles=False
            ),
        )
        self._BotBase__cogs = commands.core._CaseInsensitiveDict()
        cluster = motor.AsyncIOMotorClient(MONGO_DB_URL)
        self.session = aiohttp.ClientSession()
        #  self.richConsole = RichConsole()

        self.cache_loaded = False
        self.cogs_loaded = False
        self.views_loaded = False
        self.rolemenus_loaded = False
        self.last_updated_leveling_db = 0
        self.last_updated_serverconfig_db = 0

        self.db = cluster["SowardPrime"]
        self.topgg_headers = {
            "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEwMTM3NzE0OTcxNTc5NzIwMDgiLCJib3QiOnRydWUsImlhdCI6MTY4NTkwNTg1OH0.DqVYGUH8wqq-yZkKgymsAM5DIprfKPoWSIb5aj71wZ8"
        }

        self.reminders_db = self.db["reminders"]
        self.prem_db = self.db["premium"]
        self.user_profile_db = self.db["user_profile"]
        self.bookmarks = self.db["bookmarks"]
        self.self_roles = self.db["self_roles"]
        self.loda = self.db["serverss"]
        self.serverconfig = self.db["serverconfig"]
        self.warnings = self.db["warnings"]

        self.prem = []
        self.reminders = []

        self.serverconfig_cache = []

        self.persistent_views_added = False
        self.message_cache = {}

    #     self.update_serverconfig_db.start()

    async def get_user_profile_(self, user_id: int) -> Profile:
        profile_dict = await self.user_profile_db.find_one({"_id": user_id})
        return Profile(**profile_dict) if profile_dict else Profile(user_id)

    async def update_user_profile_(self, user_id: int, **options):
        await self.user_profile_db.update_one(
            {"_id": user_id}, {"$set": options}, upsert=True
        )

    async def load_rolemenus(self, dropdown_view, button_view):
        i = 0
        cursor = self.self_roles.find({})
        h = await cursor.to_list(length=None)
        for amogus in h:
            guild = self.get_guild(amogus["_id"])
            if guild is not None:
                role_menus = amogus["role_menus"]
                for msg_id, menu in role_menus.items():
                    if menu["type"] == "dropdown":
                        self.add_view(
                            dropdown_view(guild, menu["stuff"]), message_id=int(msg_id)
                        )
                        i += 1
                    if menu["type"] == "button":
                        self.add_view(
                            button_view(guild, menu["stuff"]), message_id=int(msg_id)
                        )
                        i += 1
        self.rolemenus_loaded = True

    async def init_extensions(self):
        extLoaded = 1
        extensions = [e for e in os.listdir("cogs/") if e.endswith(".py")]
        # with self.richConsole.status("[bold green][Soward][/] Loading Cogs...") as status:
        for ext in extensions:
            try:
                await self.load_extension(f"{ext[:-3]}")
                extLoaded += 1
                await asyncio.sleep(0.2)
            except commands.ExtensionAlreadyLoaded:
                pass
            except Exception:
                pass
            try:
                extLoaded += 1
            except Exception:
                pass

        try:
            self.loop.create_task(self.status_loop())

        except Exception:
            pass

    @tasks.loop(minutes=1.0)
    async def status_task(self) -> None:
        statuses = ["Soward", "?help", f"{len(self.guilds)} Servers"]
        await self.change_presence(activity=discord.Game(random.choice(statuses)))

    async def on_ready(self) -> None:
        console.print(f"[bold green][Prince][/] Connected as {self.user}")
        if not self.status_task.is_running():
            self.status_task.start()
        if not self.rolemenus_loaded:
            await self.load_rolemenus(DropDownSelfRoleView, ButtonSelfRoleView)
        if not self.persistent_views_added:
            self.add_view(main())
            self.add_view(ticket_launcher())

            self.persistent_views_added = True

        await self.init_extensions()
        #   self.status_task.start()
        #     await self.sync.tree()
        print("synced")

        async with aiohttp.ClientSession(headers=self.topgg_headers) as session:
            async with session.post(
                "https://top.gg/api/bots/1013771497157972008/stats",
                json={"server_count": len(self.guilds)},
            ) as r:
                print("Posted Data On Top GG", r.status)

    async def get_prefix(self, message: discord.Message):
        with open("nonprefix.json", "r") as f:
            p = json.load(f)

        if not message.guild:
            return (
                commands.when_mentioned_or("?", "")(self, message)
                if message.author.id in p["np"]
                else commands.when_mentioned_or("?")(self, message)
            )
        data = getpre(message.guild.id)

        prefix = data["prefix"]

        if message.author.id in p["np"]:
            return commands.when_mentioned_or(prefix, "")(self, message)

        else:
            return commands.when_mentioned_or(prefix)(self, message)

    def run(self) -> None:
        super().run(TOKEN)

    async def get_or_fetch_message(self, channel, message):
        if message in self.message_cache:
            return self.message_cache[message]

        if isinstance(channel, int):
            channel = self.get_channel(channel) or await self.fetch_channel(channel)

        try:
            msg = await channel.fetch_message(message)
            self.message_cache[message] = msg
            return msg
        except discord.NotFound:
            return None

    async def on_message_edit(self, before, after):
        if before.content == after.content:
            return

        if before.id in self.message_cache:
            self.message_cache[after.id] = after

    async def on_reaction_add(self, reaction, user):
        if reaction.message.id in self.message_cache:
            self.message_cache[reaction.message.id] = reaction.message

    async def on_reaction_remove(self, reaction, user):
        if reaction.message.id in self.message_cache:
            self.message_cache[reaction.message.id] = reaction.message

    async def on_message_delete(self, message):
        if message.id in self.message_cache:
            del self.message_cache[message.id]
