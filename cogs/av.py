import discord
from discord.ext import commands
import json
from prince1.Tools import *
from prince.bot import Bot
import discord
from discord.ext import commands
from afks import afks
from discord.utils import get
import psutil
import time
import datetime
import random
import requests
import aiohttp
import re
from discord.ext.commands.errors import BadArgument
from discord.colour import Color
import hashlib
#from utils.Tools import *
import contextlib
from traceback import format_exception
import discord
from discord.ext import commands
import io
import textwrap
import datetime
import sys
from discord.ui import Button, View
import psutil
import time
import datetime
import platform
import typing
from typing import *
from .op import default
from prince3.Api import do_rtfm


class arv(commands.Cog,name="Utility"):
    def __init__(self, client):
        self.client = client

    @commands.command(
        usage="Avatar [member]",
        name='avatar',
        aliases=['av', 'pic', 'pfp'],
        help="""Wanna steal someone's avatar here you go
Aliases""")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()  
    async def _user(self,
                    ctx,
                    member: Optional[Union[discord.Member,
                                           discord.User]] = None):
        if member == None or member == "":
            member = ctx.author
        user = self.client.get_user(member.id)     
        webp = user.avatar.replace(format='webp')
        jpg = user.avatar.replace(format='jpg')
        png = user.avatar.replace(format='png')
        embed = discord.Embed(
                color=0x2f3136,
                description=f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp})"
                if not user.avatar.is_animated() else
                f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp}) | [`GIF`]({user.avatar.replace(format='gif')})"
            )
        embed.set_author(name=f"{member}",
                             icon_url=member.avatar.url
                             if member.avatar else member.default_avatar.url)
        embed.set_image(url=user.avatar.url)
        embed.set_footer(
                text=f"Requested By {ctx.author}",
                icon_url=ctx.author.avatar.url
                if ctx.author.avatar else ctx.author.default_avatar.url)
            
        await ctx.send(embed=embed)
      
    @commands.group()
    @ignore_check()

    @commands.guild_only()

    @commands.has_permissions(ban_members=True)

    async def find(self, ctx):

        """ Finds a user within your search term """

        if ctx.invoked_subcommand is None:

            await ctx.send_help(str(ctx.command))

    @find.command(name="playing")
    @ignore_check()
                  

    async def find_playing(self, ctx, *, search: str):

        loop = []

        for i in ctx.guild.members:

            if i.activities and (not i.bot):

                for g in i.activities:

                    if g.name and (search.lower() in g.name.lower()):

                        loop.append(f"{i} | {type(g).__name__}: {g.name} ({i.id})")

        await default.pretty_results(

            ctx, "playing", f"Found **{len(loop)}** on your search for **{search}**", loop

        )

    @find.command(name="username", aliases=["name"])
    @ignore_check()

    async def find_name(self, ctx, *, search: str):

        loop = [f"{i} ({i.id})" for i in ctx.guild.members if search.lower() in i.name.lower() and not i.bot]

        await default.pretty_results(

            ctx, "name", f"Found **{len(loop)}** on your search for **{search}**", loop

        )

    @find.command(name="nickname", aliases=["nick"])
    @ignore_check()

    async def find_nickname(self, ctx, *, search: str):

        loop = [f"{i.nick} | {i} ({i.id})" for i in ctx.guild.members if i.nick if (search.lower() in i.nick.lower()) and not i.bot]

        await default.pretty_results(

            ctx, "name", f"Found **{len(loop)}** on your search for **{search}**", loop

        )

    @find.command(name="id")
    @ignore_check()
    async def find_id(self, ctx, *, search: int):

        loop = [f"{i} | {i} ({i.id})" for i in ctx.guild.members if (str(search) in str(i.id)) and not i.bot]

        await default.pretty_results(

            ctx, "name", f"Found **{len(loop)}** on your search for **{search}**", loop

        )

    @find.command(name="discriminator", aliases=["discrim"])
    @ignore_check()
    async def find_discriminator(self, ctx, *, search: str):

        if not len(search) == 4 or not re.compile("^[0-9]*$").search(search):

            return await ctx.send("You must provide exactly 4 digits")

        loop = [f"{i} ({i.id})" for i in ctx.guild.members if search == i.discriminator]

        await default.pretty_results( ctx,"discriminator", f"Found **{len(loop)}** on your search for **{search}**", loop

            )        
      
    @commands.group(aliases=['docs', 'ctd', 'documentation', 'rtfm', 'rtfd'], invoke_without_command=True)
    @ignore_check()
    async def rtd(self, ctx, *, obj: str = None):

	    await do_rtfm(self, ctx, 'stable', obj)

    @rtd.command(aliases=['python'])

    async def py(self, ctx, *, obj: str = None):

	    await do_rtfm(self, ctx, 'python', obj)

    @rtd.command(aliases=['2.0'])

    async def latest(self, ctx, *, obj: str = None):

        await do_rtfm(self, ctx, 'latest', obj)
async def setup(client):
    await client.add_cog(arv(client))