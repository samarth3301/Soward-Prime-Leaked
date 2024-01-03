from discord.ext import commands

from prince.bot import Bot

import discord, requests

import json

from prince.bot import Bot

from discord.ui import View, Button

from discord.ext.commands import Cog

from ast import literal_eval

import time

from prince1.Tools import*

import asyncio

from prince.confirm import ConfirmationPrompt

from prince import emote

from prince import embed_creator

from typing import Optional

#from googletrans import Translator

from typing import *

from discord import app_commands

from io import BytesIO

import datetime 

        

class Afk2(Cog,name="utilities"):

    def __init__(self, client):

        self.client = client

    
        

    @commands.command(aliases=["dnt"])
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)

   # @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    async def donate(self,ctx):

        embed = discord.Embed(title="**Wanna Donate?**", description="You Can Donate In Owo/Inr/crypto($)\nYour contribution will be used in our Maintianence and development\n Thanks For Your Support",color=0x2f3136)

        embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

        embed.set_thumbnail(url=self.client.user.avatar)

        embed.set_footer(text="Made By Prince")

        await ctx.send(embed = embed)

    @commands.group(name="boost69", help="Enables/Disables boost message !", invoke_without_command=True)

  

 

    @commands.cooldown(1, 10, commands.BucketType.user)
    @ignore_check()
  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    @blacklist_check()

#  @voter_only()

    async def _boost69(self, ctx: Context):

        if ctx.subcommand_passed is None:

          await ctx.send_help(ctx.command)

          ctx.command.reset_cooldown(ctx)

  

                

    @_boost69.command(name="enable",aliases=["on"])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @ignore_check()
    @commands.has_permissions(administrator=True)

 #   @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    async def _boot_enable(self,ctx):

        data = getboost(ctx.guild.id)

        if data == "on": 

           embed =  discord.Embed(title="__Soward Prime__", description="Boost message already enabeld",color=0x2f3136)

           await ctx.send(embed=embed)

        else:

            data = "on"

            updateboost(ctx.guild.id,data)

            em=discord.Embed(title="__Soward Prime__", description="Successfully enabled boost message",color=0x2f3136)

            em.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

            em.set_thumbnail(url=self.client.user.avatar)

            em.set_footer(text="Made By Prince")

            await ctx.send(embed=em)

 

      

        

        

        

        

        

        

        

        

          

        

        

    

    @_boost69.command(name="disable", help="You can disable boost message ", aliases=["off"])
    @ignore_check()
  

    @commands.cooldown(1, 10, commands.BucketType.user)

   # @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

 # @voter_only()

    async def _boost_disable(self, ctx: Context):

        data = getboost(ctx.guild.id)

     

        if data == "off":

          emb = discord.Embed(title="**__Soward Prime__**", description=f" Boost Message already disabled in this server", color=0x2f3136, timestamp=ctx.message.created_at)

          emb.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)

          if ctx.guild.icon:

            emb.set_thumbnail(url=ctx.guild.icon)

          emb.set_footer(text="Made By Prince")

          await ctx.reply(embed=emb, mention_author=False)

        else:

          data = "off"

          updateboost(ctx.guild.id, data)

          swrd = discord.Embed(title="Soward Prime", description=f"Successfully disabled Boost message for this server ", color=0xFF1B1B, timestamp=ctx.message.created_at)

          swrd.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)

          if ctx.guild.icon:

            swrd.set_thumbnail(url=ctx.guild.icon)

          swrd.set_footer(text="Made By Prince")

          await ctx.reply(embed=swrd, mention_author=False)

    @commands.command(pass_context=True)

    @commands.cooldown(1, 3, commands.BucketType.user)

 #   @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @ignore_check()
    @commands.cooldown(1, 5, commands.BucketType.user)

  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    async def ping(self,ctx):

        """ Pong! """

    #    message = ctx.message

     #   await message.delete()

        before = time.monotonic()

    #    message = await ctx.send("Pong!")

        ping = round(self.client.latency* 1000)

        await ctx.reply(f"Pong!  `{int(ping)}ms`")

        print(f'Ping {int(ping)}ms')

    @commands.command(aliases=["ast","addstick"],usage="addsticker <reply with sticker message>")
    @ignore_check()
    @commands.cooldown(1, 5, commands.BucketType.user)

  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    @commands.has_permissions(manage_emojis=True)

    async def addsticker(self,ctx):

        ref = ctx.message.reference

        if not ref:

          await ctx.send_help(ctx.command)

        else:

            msg = await ctx.fetch_message(ref.message_id)

        stickers = msg.stickers

        for sticker in stickers:

            name = sticker.name

        sticker = await sticker.fetch()

        file = discord.File(fp=BytesIO(await sticker.read()))

        try:

           sticker = await ctx.guild.create_sticker(name=name, description=f"Uploaded by {ctx.author}",emoji=sticker.name, file=file, reason=f"Command used by {ctx.author}")

           

           await ctx.reply(f"<:Icons_correct:1017402689027592222> | Sticker created with the Name `{sticker.name}`",stickers=[sticker])

        except Exception:

          embed=discord.Embed(description="Maximum number of stickers reached",color=0x2f3136, timestamp=ctx.message.created_at)

    

          embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

        embed.set_footer(text="Made By Prince",icon_url=self.client.user.avatar)

        return await ctx.reply(embed=embed,delete_after=5)

    @commands.command()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)

  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    @commands.has_permissions(administrator=True)

    async def roleicon(self,ctx,role:discord.Role,*,emoji:discord.PartialEmoji=None):

        if ctx.guild.premium_subscription_count <=6:

            await ctx.reply("<:zzcross:1104092956039848017> | This server does not support role icons. Servers with level 2 boosts are allowed to set role icons.")

            return

        if emoji is None:

            

            await role.edit(display_icon=None,reason=f"command executed by {ctx.author}")

            await ctx.send(f"<:Icons_correct:1017402689027592222> | successfully edited `{role.name}` icon")

        else:

            emoji_op = await emoji.read()

            await role.edit(display_icon=emoji_op,reason=f"command executed by {ctx.author}")

            await ctx.send(f"<:Icons_correct:1017402689027592222> |successfully edited `{role.name}` icon to {emoji} ")

    

        

    

            

            

          

           

       

        

            

           

            

            

    @commands.command()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)

  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    async def users(self,ctx):

        total_members = sum(g.member_count for g in self.client.guilds if g.member_count != None)

        await ctx.send(total_members)

                           

                  

    @commands.hybrid_command(name="embed",description="""Create a custom embed""",help="""Create a custom embed""",brief="Create a custom embed",aliases=["cembed", "ce","cem"],enabled=True,hidden=False,)
    @ignore_check()
    @commands.has_permissions(manage_messages=True)

    @commands.cooldown(1.0, 5.0, commands.BucketType.user)

    async def custom_embed_cmd(self, ctx: commands.Context) -> None:

        """

        Create a custom embed

           """

        embed = discord.Embed(

            title="Embed Creator",

            description="Create an embed with this view!",color=0x2f3136,

            timestamp=discord.utils.utcnow(),

        )

        view = embed_creator.CustomEmbedView(ctx, embed)

        await ctx.reply(embed=embed, view=view)      

               

    @commands.hybrid_command(aliases=["tl"])
    @ignore_check()

  #  @app_commands.guilds(*GuildIDs.ALL_GUILDS)

    @commands.cooldown(1, 3, commands.BucketType.user)

   # @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    @app_commands.describe(message="The string or message to translate.")

    async def translate(self, ctx: commands.Context, *, message: str = None) -> None:

        """Translates a message from any language to english.

        Specify a string to translate, or a message to translate by either using message ID/Link,

        or replying to a message.

        Attempts to guess the original language.

        """

        # First we check if the user is replying to a message.

        if ctx.message.reference and not message:

            fetched_message = await ctx.channel.fetch_message(

                ctx.message.reference.message_id

            )

            message = fetched_message.content

        # Similar to the emoji command, we have to use the converter ourselves here,

        # instead of just typehinting a Union of Message and str and letting discord.py handle it.

        try:

            message_converter = commands.MessageConverter()

            fetched_message = await message_converter.convert(ctx, message)

            message = fetched_message.content

        except commands.CommandError:

            pass

        # Checks if the message is empty if either the user failed to specify anything,

        # or if the message content of the message specified is empty.

        if not message:

            await ctx.send("You need to specify a message to translate!")

            return

        translation = Translator().translate(f"{message}", dest="en")

        embed = discord.Embed(description=translation.text[:1000], colour=0x2f3136)

      #  embed.add_field(

      #      name=f"Original Text :",

     #       value=translation.origin[:1000],

     #       inline=False,

    #    )

    #    embed.add_field(

     #       name="Translated Text (en):", value=translation.text[:1000], inline=False

   #     )

   #     embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar)

        await ctx.reply(embed=embed)

        

    @commands.group(name="banner")
    @ignore_check()

    async def banner(self, ctx):

        if ctx.invoked_subcommand is None:

            await ctx.send_help(ctx.command)

    @banner.command(name="server")
    @ignore_check()

    @commands.cooldown(1, 5, commands.BucketType.user)

   # @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    async def server(self, ctx):

        if not ctx.guild.banner:

            await ctx.reply("This server does not have a banner.")

        else:

            webp = ctx.guild.banner.replace(format='webp')

            jpg = ctx.guild.banner.replace(format='jpg')

            png = ctx.guild.banner.replace(format='png')

            embed = discord.Embed(

                color=0x2f3136,

                description=f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp})"

                if not ctx.guild.banner.is_animated() else

                f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp}) | [`GIF`]({ctx.guild.banner.replace(format='gif')})"

            )

            embed.set_image(url=ctx.guild.banner)

            embed.set_author(name=ctx.guild.name,

                             icon_url=ctx.guild.icon.url

                             if ctx.guild.icon else ctx.guild.default_icon.url)

            embed.set_footer(

                text=f"Requested By {ctx.author}",

                icon_url=ctx.author.avatar.url

                if ctx.author.avatar else ctx.author.default_avatar.url)

            await ctx.reply(embed=embed)

    @blacklist_check()

  #  @ignore_check()

    @banner.command(name="user")
    @ignore_check()

    @commands.cooldown(1, 2, commands.BucketType.user)

   # @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    async def _user(self,

                    ctx,

                    member: Optional[Union[discord.Member,

                                           discord.User]] = None):

        if member == None or member == "":

            member = ctx.author

        bannerUser = await self.client.fetch_user(member.id)

        if not bannerUser.banner:

            await ctx.reply("{} does not have a banner.".format(member))

        else:

            webp = bannerUser.banner.replace(format='webp')

            jpg = bannerUser.banner.replace(format='jpg')

            png = bannerUser.banner.replace(format='png')

            embed = discord.Embed(

                color=0x2f3136,

                description=f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp})"

                if not bannerUser.banner.is_animated() else

                f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp}) | [`GIF`]({bannerUser.banner.replace(format='gif')})"

            )

            embed.set_author(name=f"{member}",

                             icon_url=member.avatar.url

                             if member.avatar else member.default_avatar.url)

            embed.set_image(url=bannerUser.banner)

            embed.set_footer(

                text=f"Requested By {ctx.author}",

                icon_url=ctx.author.avatar.url

                if ctx.author.avatar else ctx.author.default_avatar.url)

            await ctx.send(embed=embed)

    @commands.command(aliases=["special","cursive", "italics"])
    @ignore_check()

    async def fancy(self, ctx, *, message):

        letters = {

            "z": "𝓏",

            "y": "𝓎",

            "x": "𝓍",

            "w": "𝓌",

            "v": "𝓋",

            "u": "𝓊",

            "t": "𝓉",

            "s": "𝓈",

            "r": "𝓇",

            "q": "𝓆",

            "p": "𝓅",

            "o": "𝑜",

            "n": "𝓃",

            "m": "𝓂",

            "l": "𝓁",

            "k": "𝓀",

            "j": "𝒿",

            "i": "𝒾",

            "h": "𝒽",

            "g": "𝑔",

            "f": "𝒻",

            "e": "𝑒",

            "d": "𝒹",

            "c": "𝒸",

            "b": "𝒷",

            "a": "𝒶"

        }

        message = message.lower()

        NewMessage = ""

        for letter in message:

            if letter in letters:

                NewMessage += letters[letter]

            else:

                NewMessage += letter

        await ctx.reply(NewMessage, mention_author=False)

    

    

    

      

     

    @commands.group(invoke_without_command=True,aliases=["clear"])
    @ignore_check()

    @commands.cooldown(1, 3, commands.BucketType.user)

  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    @commands.has_permissions(manage_messages=True)

    async def purge(self, ctx,amount:int=10):

        if amount >999:

            return await ctx.send(embed=discord.Embed(color=0x010101, description="❌ | Not more than 999"))

        deleted = await ctx.channel.purge(limit=amount+1)
        embed=discord.Embed(color=0x010101, description=f"<:ri8:1038487759750438912> | Successfully Purged {len(deleted)-1} Messages")
        return await ctx.send(embed=embed,delete_after=5)


    

    

    async def do_removal(self, ctx, limit, predicate, *, before=None, after=None, message=True):

        if limit > 2000:

            return await ctx.send(f"Too many messages to search given ({limit}/2000)")

        if not before:

            before = ctx.message

        else:

            before = discord.Object(id=before)

        if after:

            after = discord.Object(id=after)

        try:

            deleted = await ctx.channel.purge(limit=limit, before=before, after=after, check=predicate)

        except discord.Forbidden:

            return await ctx.send(embed=discord.Embed(color=0x2f3136,  description=" I Need Manage Messages"))

        except discord.HTTPException as e:

            return await ctx.send(f"Error: {e} (try a smaller search?)")

        deleted = len(deleted)

        if message is True:

            await ctx.send(embed=discord.Embed(color=0x2f3136, description=f"<:ri8:1038487759750438912> | Successfully removed {deleted} message{'' if deleted == 1 else 's'} of bots."), delete_after=5)

    

      

    

    @purge.command()
    @ignore_check()

    @commands.has_permissions(manage_messages=True)

    @commands.cooldown(1, 3, commands.BucketType.user)

  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

  #  @checks.ignore_check()  

  #  @checks.not_blacklisted()

    @commands.has_guild_permissions(manage_messages=True)
    @ignore_check()

    async def embeds(self, ctx, search=100):

        """Removes messages that have embeds in them."""

        await self.do_removal(ctx, search, lambda e: len(e.embeds))

    @purge.command(help="Clears the messages containing invite links",usage="purge invites")
    @ignore_check()

    @commands.cooldown(1, 3, commands.BucketType.user)

  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

  #  @checks.ignore_check()  

  #  @checks.not_blacklisted()

    @commands.has_permissions(manage_messages=True)

    @commands.has_guild_permissions(manage_messages=True)

    async def invites(self, ctx, amount: int = 10):

        if amount >1000:

            return await ctx.send("Maximum number of amount reached")

        global counter

        counter = 0

        def check(m):

            global counter

            if counter >= amount:

                return False

            if "discord.gg/" in m.content.lower():

                counter += 1

                return True

            else:

                return False

        deleted = await ctx.channel.purge(limit=100, check=check)

        return await ctx.send(f"<:ri8:1038487759750438912> | Successfully Deleted {len(deleted)} Invites In {ctx.channel.mention}",delete_after=5)

    @purge.command()
    @ignore_check()

    @commands.cooldown(1, 3, commands.BucketType.user)

   # @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

 #   @checks.ignore_check()  

   # @checks.not_blacklisted()

    @commands.has_permissions(manage_messages=True)

    async def files(self, ctx, search=100):

        """Removes messages that have attachments in them."""

        await self.do_removal(ctx, search, lambda e: len(e.attachments))

    @purge.command()

    @commands.cooldown(1, 3, commands.BucketType.user)

   # @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

 #   @checks.ignore_check()  

  #  @checks.not_blacklisted()

    @commands.has_permissions(manage_messages=True)

    async def mentions(self, ctx, search=100):

        """Removes messages that have mentions in them."""

        await self.do_removal(ctx, search, lambda e: len(e.mentions) or len(e.role_mentions))

    @purge.command()
    @ignore_check()

    @commands.cooldown(1, 3, commands.BucketType.user)

   # @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

  #  @checks.ignore_check()  

  #  @checks.not_blacklisted()

    @commands.has_permissions(manage_messages=True)
    @ignore_check()

    async def images(self, ctx, search=100):

        """Removes messages that have embeds or attachments."""

        await self.do_removal(ctx, search, lambda e: len(e.embeds) or len(e.attachments))

    @purge.command(name="all")
    @ignore_check()

    @commands.cooldown(1, 3, commands.BucketType.user)

  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

  #  @checks.ignore_check()  

  #  @checks.not_blacklisted()

    @commands.has_permissions(manage_messages=True)

    async def _remove_all(self, ctx, search=100):

        """Removes all messages."""

        await self.do_removal(ctx, search, lambda e: True)

    @purge.command(name="bots",aliases=["bot"])
    @ignore_check()

    @commands.cooldown(1, 3, commands.BucketType.user)

  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    @commands.has_permissions(manage_messages=True)

    async def _bots(self, ctx, search=100):

        """Removes a bot user's messages and messages with their optional prefix."""

        getprefix = [";", "$", "!", "-", "?", ">", "^", "$", "w!", ".", ",", "a?", "g!", "m!", "s?"]

        def predicate(m):

            return (m.webhook_id is None and m.author.bot) or m.content.startswith(tuple(getprefix))

        await self.do_removal(ctx, search, predicate)

    @purge.command(name="emojis")
    @ignore_check()

    @commands.cooldown(1, 3, commands.BucketType.user)

  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

   # @checks.ignore_check()  

   # @checks.not_blacklisted()

    @commands.has_permissions(manage_messages=True)

    async def _emojis(self, ctx, search=100):

        """Removes all messages containing custom emoji."""

        custom_emoji = re.compile(r"<a?:(.*?):(\d{17,21})>|[\u263a-\U0001f645]")

        def predicate(m):

            return custom_emoji.search(m.content)

        await self.do_removal(ctx, search, predicate)

    @purge.command(name="reactions")
    @ignore_check()

    @commands.cooldown(1, 3, commands.BucketType.user)

  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

  #  @checks.ignore_check()  

  #  @checks.not_blacklisted()

    @commands.has_permissions(manage_messages=True)

    async def _reactions(self, ctx, search=100):

        """Removes all reactions from messages that have them."""

        if search > 2000:

            return await ctx.send(f"Too many messages to search for ({search}/2000)")

        total_reactions = 0

        async for message in ctx.history(limit=search, before=ctx.message):

            if len(message.reactions):

                total_reactions += sum(r.count for r in message.reactions)

                await message.clear_reactions()

        await ctx.send(f"Successfully removed {total_reactions} reactions.",delete_after=5)

    @purge.command(help="Clears the messages of the given user",usage="purge <user>")
    @ignore_check()

    @commands.cooldown(1, 3, commands.BucketType.user)

   # @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

   # @checks.ignore_check()  

 #   @blacklist_check()

    @commands.has_permissions(manage_messages=True)

    async def user(self, ctx, user: discord.Member, amount: int = 50):

        if amount >1000:

            return await ctx.author.send(embed=discord.Embed(description="Purge limit Reached",delete_after=5))

        global counter

        counter = 0

        def check(m):

            global counter

            if counter >= amount:

                return False

            if m.author.id == user.id:

                counter += 1

                return True

            else:

                return False

        deleted = await ctx.channel.purge(limit=100, check=check)

        return await ctx.send(embed=discord.Embed(description=f"Successfully Purged User  {len(deleted)} Messages"), delete_after=5)

    @commands.group(invoke_without_command=True,aliases=["mm"])
    @ignore_check()

    async def maintenance(self, ctx):

        """Maintenance ON/ OFF for the server."""

        await ctx.send_help(ctx.command)

    @maintenance.command(name="on")
    @ignore_check()

    @commands.has_permissions(administrator=True)

    @commands.cooldown(1, 3, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    @commands.bot_has_guild_permissions(manage_channels=True)

    async def maintenace_on(self, ctx, *, role: discord.Role = None):

        """

        Turn ON maintenance mode.

        You can turn on maintenance for a specific role too , the default role is everyone.

        This will hide all the channels where `role` has `read_messages` permission enabled.

        """

        me = ctx.guild.me

        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:

            await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))

            return

        else:

         role = role or ctx.guild.default_role

        

        channels = list(filter(lambda x: x.overwrites_for(role).read_messages, ctx.guild.channels))

        mine = sum(1 for i in filter(lambda x: x.permissions_for(ctx.me).manage_channels, (channels)))

        if not (channels):

            return await ctx.reply(f"**{role}** doesn't have `read_messages` enabled in any channel.")

            return

        if not mine:

            return await ctx.reply(

                f"`{sum(1 for i in channels)} channels` have read messages enabled. But unfortunately I don't permission to edit any of them."

            )

            return

        confirmation = ConfirmationPrompt(ctx, color=0x010101)

        await confirmation.confirm(title="confirmation", description = f"This Will Lock All The Channel in this Server")    

        if confirmation.confirmed:

            await confirmation.update(description = f"{emote.loading} | locking {len(channels)} Channels")

            success, failed = [], 0

            reason = f"Action done by -> {str(ctx.author)} ({ctx.author.id})"

            for channel in channels:

                overwrite = channel.overwrites_for(role)

                overwrite.read_messages = False 

                try:

                    await channel.set_permissions(role, overwrite=overwrite, reason=reason)

                    success.append(channel.id)

                except:

                    failed += 1

                    continue    

            await confirmation.update(description = f"Updated settings for `{len(success)} channels`.(`{failed}` failed)")

            channels_create_confirmation = ConfirmationPrompt(ctx)

            await channels_create_confirmation.confirm(title = "confirmation", description = f"This Will Create Maintainence Channels")    

            if channels_create_confirmation.confirmed:

                await channels_create_confirmation.update(description = f"{emote.loading} | Creating Maintainence Channels")

                overwrites = {

                    role: discord.PermissionOverwrite(read_messages=True, send_messages=True, read_message_history=True),

                    ctx.guild.me: discord.PermissionOverwrite(

                        read_messages=True, send_messages=True, read_message_history=True

                    ),

                }

                await ctx.guild.create_text_channel(f"maintenance-chat", overwrites=overwrites, reason=reason)

                await ctx.guild.create_voice_channel(f"maintenance-vc", overwrites=overwrites, reason=reason)

                await channels_create_confirmation.update(f"Done")

            else:

                return await channels_create_confirmation.update(description = f"Ok! Not Creating Channels")

        else:

            await confirmation.update(description = "Not confirmed", hide_author=True, color=0x2f3136)

            

    @maintenance.command(name="off")
    @ignore_check()

    @commands.cooldown(1, 3, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    @commands.bot_has_guild_permissions(manage_channels=True)

    @commands.has_permissions(administrator=True)

    async def maintenance_off(self, ctx, *, role: discord.Role = None):

        """

        Turn OFF maintenance mode.

        If you turned ON maintenance mode for a specific role , you need to mention it here too.

        """

        me = ctx.guild.me

        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:

            await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))

            return 

        else:

         role = role or ctx.guild.default_role

        editable = await ctx.send(f'{emote.loading} | Unocking The Server')

        success = 0

        for channel in ctx.guild.channels:

            if channel is not None and channel.permissions_for(channel.guild.me).manage_channels:

                perms = channel.overwrites_for(role)

                perms.read_messages = True

                await channel.set_permissions(role, overwrite=perms, reason="Lockdown timer complete!")

                success += 1

        await editable.edit(

            content = f"{emote.tick} | Successfully disabled maintenance mode"

        )

        tc = discord.utils.get(ctx.guild.channels, name=f"maintenance-chat")

        vc = discord.utils.get(ctx.guild.channels, name=f"maintenance-vc")

        if tc and vc:

            await tc.delete()

            await vc.delete()   

  

 

    

   

 

   

      

     

   

    

      

     

async def setup(client):

    await client.add_cog(Afk2(client))