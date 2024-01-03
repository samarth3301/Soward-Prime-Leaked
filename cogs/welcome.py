from __future__ import annotations
import discord
import asyncio
import os
import logging
from discord.ext import commands
from prince1.Tools import *
from discord.ext.commands import Context
from discord.ui import *
import time
import datetime
import re
from typing import *
from time import strftime
#from core import Cog, Astroz, Context
from discord.ext import commands
from prince1.Tools2 import *
from prince1.Tools import *
logging.basicConfig(
    level=logging.INFO,
    format=
    "\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)


class welcomer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
           

    @commands.group(name="welcome",
                    
                    invoke_without_command=True)
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    
            
        

    

            

    @_welcome.command(name="message", help="Setups welcome message.")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_message(self, ctx: commands.Context):
        data = getDB(ctx.guild.id)

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        msg = discord.Embed(color=0x2f3136,description="""Here are some vaiables, which you can use in your welcome message.\n\nSend your welcome message in this channel now.\n\n\n```xml\n{server.member_count} = server member count\n{server.name} = server name\n{user.name} = username of new member\n{user.mention} = mention of the new user\n{user.created_at} = creation time of account of user\n{user.joined_at} = joining time of the user.\n```""")
        await ctx.send(embed=msg)
        try:
                welcmsg = await self.bot.wait_for('message',
                                                  check=check,
                                                  timeout=60.0)
        except asyncio.TimeoutError:
            
            await ctx.reply("Timeout please re run the command!")
            return
        else:
                data["welcome"]["message"] = welcmsg.content
                updateDB(ctx.guild.id, data)
                ok = discord.Embed(
                    color=0x2f3136,
                    description=
                    f" Successfully updated the welcome message .",
                    timestamp=ctx.message.created_at)
                ok.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=ok)
        

  #  @_welcome.command(name="color", help="Setups welcome color.")
 #   @blacklist_check()
  #  @ignore_check()
  #  @commands.cooldown(1, 2, commands.BucketType.user)
  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  #  @commands.guild_only()
    #@commands.has_permissions(administrator=True)
  #  async def _welcome_color(self, ctx: commands.Context):
   #     data = getDB(ctx.guild.id)

   #     def check(message):
    #        return message.author == ctx.author and message.channel == ctx.channel
    #    msg = discord.Embed(color=0x2f3136,description="```use 0x before hex code \n ex. 0x2f3136```\n send msg in this channel")
   #     await ctx.send(embed=msg)
   #     try:
    #            welcmsg = await self.bot.wait_for('message',
                                                #  check=check,
                                               #   timeout=60.0)
   #     except asyncio.TimeoutError:
            
   #         await ctx.reply("Timeout please re run the command!")
    #        return
    #    else:
     #           data["welcome"]["color"] = welcmsg.content
     #           updateDB(ctx.guild.id, data)
     #           ok = discord.Embed(
     #               color=0x2f3136,
     #               description=
    #                f" Successfully updated the welcome color.",
   #                 timestamp=ctx.message.created_at)
  # 2             ok.set_author(name=f"{ctx.author.name}",
   #                               icon_url=f"{ctx.author.avatar}")


		
    @_welcome.command(name="embed", help="Toggle embed for welcome message .")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_embed(self, ctx):
        data = getDB(ctx.guild.id)
        
        if data["welcome"]["embed"] == True:
                data["welcome"]["embed"] = False
                updateDB(ctx.guild.id, data)
                ok = discord.Embed(
                    color=0x2f3136,
                    description=
                    "Now your embed is removed and welcome message will be a plain message .",
                    timestamp=ctx.message.created_at)
                ok.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.display_avatar}")
                await ctx.send(embed=ok)
        elif data["welcome"]["embed"] == False:
                data["welcome"]["embed"] = True
                updateDB(ctx.guild.id, data)
                ok1 = discord.Embed(
                    color=0x2f3136,
                    description=
                    " Now your embed is enabled and welcome message will be a embed message.",
                    timestamp=ctx.message.created_at)
                ok1.set_author(name=f"{ctx.author.name}",
                                   icon_url=f"{ctx.author.display_avatar}")
                await ctx.send(embed=ok1)
        

    @_welcome.group(name="ping", help="Setups welcome ping message.")
    @blacklist_check()
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_ping(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)

    @_welcome_ping.command(name="on",
                            help="enable welcome ping")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_ping_on(self, ctx: commands.Context, title=None):
        data = getDB(ctx.guild.id)
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        msg = discord.Embed(color=0x2f3136,description="""Use {user.mention} for enable member mention\n\nSend your ping message in this channel now.\n\n\n```xml\n\n{user.name} <message>(optional) \n{user.mention} = mention of the new member.\n```""")
        await ctx.send(embed=msg)
        try:
                welcmsg = await self.bot.wait_for('message',
                                                  check=check,
                                                  timeout=60.0)
        except asyncio.TimeoutError:
            
            await ctx.reply("Timeout please re run the command!")
            return
        else:
                data["welcome"]["ping"] = welcmsg.content
                updateDB(ctx.guild.id, data)
                ok = discord.Embed(
                    color=0x2f3136,
                    description=
                    f" Successfully updated the welcome message .",
                    timestamp=ctx.message.created_at)
                ok.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=ok)
        

    @_welcome_ping.command(name="off",
                            help="Remove welcome ping msg.")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_ping_off(self, ctx):
        data = getDB(ctx.guild.id)

        data["welcome"]["ping"] = ""
        updateDB(ctx.guild.id, data)
        ok = discord.Embed(
                    color=0x2f3136,
                    description=
                    " Successfully disabled welcome ping message  .",
                    timestamp=ctx.message.created_at)
        ok.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.display_avatar}")
        await ctx.send(embed=ok)

    
    
                        
        
        
    @_welcome.group(name="title", help="Setups welcome title.")
    @blacklist_check()
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_title(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)

    @_welcome_title.command(name="add",
                            help="Add a welcome title ")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_title_add(self, ctx: commands.Context, title=None):
        data = getDB(ctx.guild.id)

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        msg = discord.Embed(color=0x2f3136,description="""**u can use only 1 variable ```py
		{user.name}``` in welcome title\n\n**send welcome title in this channel""")
        await ctx.send(embed=msg)
        try:
                welcmsg = await self.bot.wait_for('message',
                                                  check=check,
                                                  timeout=50.0)
        except asyncio.TimeoutError:
            
            await ctx.reply("Timeout please re run the command!")
            return
        else:
                data["welcome"]["title"] = welcmsg.content
                updateDB(ctx.guild.id, data)
                ok = discord.Embed(
                    color=0x2f3136,
                    description=
                    " Successfully updated the welcome title.",
                    timestamp=ctx.message.created_at)
                ok.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.display_avatar}")
                await ctx.send(embed=ok)

    @_welcome_title.command(name="remove",
                            help="Remove welcome title .")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_title_remove(self, ctx):
        data = getDB(ctx.guild.id)

        data["welcome"]["title"] = ""
        updateDB(ctx.guild.id, data)
        ok = discord.Embed(
                    color=0x2f3136,
                    description=
                    " Successfully removed the welcome title .",
                    timestamp=ctx.message.created_at)
        ok.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.display_avatar}")
        await ctx.send(embed=ok)

    @_welcome.group(name="footer", help="Setups welcome footer.")
    @blacklist_check()
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_footer(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)

    @_welcome_footer.command(name="add",
                            help="Add a welcome footer ")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_footer_add(self, ctx: commands.Context, title=None):
        data = getDB(ctx.guild.id)

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        msg = discord.Embed(color=0x2f3136,description="""**variableÂ¢ ```py
		{user.name}\n{server.name}\n{server.member_count}``` \n\n**send welcome footer msg in this channel""")
        await ctx.send(embed=msg)
        try:
                welcmsg = await self.bot.wait_for('message',
                                                  check=check,
                                                  timeout=50.0)
        except asyncio.TimeoutError:
            
            await ctx.reply("Timeout please re run the command!")
            return
        else:
                data["welcome"]["footer"] = welcmsg.content
                updateDB(ctx.guild.id, data)
                ok = discord.Embed(
                    color=0x2f3136,
                    description=
                    " Successfully updated the welcome footer.",
                    timestamp=ctx.message.created_at)
                ok.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.display_avatar}")
                await ctx.send(embed=ok)

    @_welcome_footer.command(name="remove",
                            help="Remove welcome footer  .")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_footer_remove(self, ctx):
        data = getDB(ctx.guild.id)

        data["welcome"]["footer"] = ""
        updateDB(ctx.guild.id, data)
        ok = discord.Embed(
                    color=0x2f3136,
                    description=
                    " Successfully removed the welcome footer.",
                    timestamp=ctx.message.created_at)
        ok.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.display_avatar}")
        await ctx.send(embed=ok)

    

    @_welcome.group(name="thumbnail", help="Setups welcome thumbnail.")
    @blacklist_check()
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_thumbnail(self,ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
        ...

    @_welcome_thumbnail.command(name="add",
                            help="Add a welcome thumbnail ")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True) 
    async def _welcome_thummbnail_add(self, ctx, thumbnail_link):
        data = getDB(ctx.guild.id)
        streamables = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        
        if streamables.search(thumbnail_link):
                data["welcome"]["thumbnail"] = thumbnail_link
                updateDB(ctx.guild.id, data)
                ok = discord.Embed(
                    color=0x2f3136,
                    description=
                    " Successfully updated the welcome thumbnail url .",
                    timestamp=ctx.message.created_at)
                ok.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.display_avatar}")
                await ctx.send(embed=ok)
        else:
                await ctx.send(" Kindly put a valid link.")
    
    

    @_welcome_thumbnail.command(name="remove",
                            help="remove welcome thumbnail")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_thummbnail_remove(self, ctx):
        data = getDB(ctx.guild.id)
        data["welcome"]["thumbnail"] = ""
        updateDB(ctx.guild.id, data)
        ok = discord.Embed(
                    color=0x2f3136,
                    description=
                    " Successfully removed welcome thumbnail .",
                    timestamp=ctx.message.created_at)
        ok.set_author(name=f"{ctx.author.name}",icon_url=f"{ctx.author.display_avatar}")
        await ctx.send(embed=ok)
    
        
	    
	    
        
        
    @_welcome.group(name="image", help="Setups welcome image.")
    @blacklist_check()
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_image(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)

    @_welcome_image.command(name="add",
                            help="Add a welcome image")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True) 
    async def _welcome_image_add(self, ctx, *, image_link):
        data = getDB(ctx.guild.id)
        streamables = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$',
            re.IGNORECASE)
        with open ("premium.json","r") as f:

            member = json.load(f)

            prm = member["guild"]
        if str(ctx.guild.id) not in prm:
            embed = discord.Embed(title="You are not a premium user! Please buy premium to use this command!",color=0x2f3136)

            embed.set_thumbnail(url=self.bot.user.avatar)

            embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

            embed.set_footer(text="Made By Prince",icon_url=self.bot.user.avatar)

            B = Button(label='Get Premium',emoji="<a:Diamonds:1087431201117179944>" ,style=discord.ButtonStyle.link,url='https://discord.gg/soward')

            view = View()

            view.add_item(B)

            return await ctx.send(embed=embed,view=view)

        
        if streamables.search(image_link):
                data["welcome"]["image"] = image_link
                updateDB(ctx.guild.id, data)
                ok = discord.Embed(
                    color=0x2f3136,
                    description=
                    "Successfully updated the welcome image url .",
                    timestamp=ctx.message.created_at)
                ok.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.avatar}")
                await ctx.send(embed=ok)
        else:
                await ctx.send(" Kindly put a valid link.")
    
    

    @_welcome_image.command(name="remove",
                            help="remove welcome image")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_thummbnail(self, ctx):
        data = getDB(ctx.guild.id)
        data["welcome"]["image"] = ""
        updateDB(ctx.guild.id, data)
        ok = discord.Embed(
                    color=0x2f3136,
                    description=
                    " Successfully removed welcome image .",
                    timestamp=ctx.message.created_at)
        ok.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.display_avatar}")
        await ctx.send(embed=ok)
                                    
                                                  
         


    @_welcome.group(name="channel", help="Setups welcome channel.")
    @blacklist_check()
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_channel(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    @_welcome_channel.command(name="add",
                            help="Add a channel to the welcome channel.")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_channel_add(self, ctx, channel: discord.TextChannel):
		   data = getDB(ctx.guild.id)
		   
		   chh = data["welcome"]["channel"] 
		   if len(chh) == 1:
			   ok = discord.Embed(color=0x2f3135,description=" You have reached maximum channel limit for channel which is one .",timestamp=ctx.message.created_at)
			   ok.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.display_avatar}")
			   await ctx.send(embed=ok)
		   else:
			   if str(channel.id) in data:
				   ok1 = discord.Embed(color=0x2f3136,description=" This channel is already in the welcome channels list .",timestamp=ctx.message.created_at)
				   ok1.set_author(name=f"{ctx.author.name}",icon_url=f"{ctx.author.display_avatar}")
				   await ctx.send(embed=ok1)
			   else:
				   data["welcome"]["channel"] = [channel.id]

				   updateDB(ctx.guild.id, data)
				   ok4 = discord.Embed(color=0x2f3136,description=f" Successfully added {channel.mention} to welcome channel list .",timestamp=ctx.message.created_at)
				   ok4.set_author(name=f"{ctx.author.name}",icon_url=f"{ctx.author.display_avatar}")
				   await ctx.send(embed=ok4)
		
	
                        

    @_welcome_channel.command(name="remove",
                            help="Remove a chanel from welcome channel ."
                            )
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _welcome_channel_remove(self, ctx,):
        data = getDB(ctx.guild.id)
        chh = data["welcome"]["channel"]
        
        if len(chh) == 0:
                ok = discord.Embed(
                    color=0x2f3136,
                    description=
                    f" This server dont have any welcome channel setupped yet .",
                    timestamp=ctx.message.created_at)
                ok.set_author(name=f"{ctx.author.name}",
                                  icon_url=f"{ctx.author.display_avatar}")
                await ctx.send(embed=ok)
        else:
                data["welcome"]["channel"] = []
         
                updateDB(ctx.guild.id, data)
                ok3 = discord.Embed(
                        color=0x2f3136,
                        description=
                        f" Successfully removed  from welcome channel list .",
                        timestamp=ctx.message.created_at)
                ok3.set_author(name=f"{ctx.author.name}",
                                       icon_url=f"{ctx.author.display_avatar}")
                await ctx.send(embed=ok3)
        

    

		

    @_welcome.command(name="test",
                    help="Test the welcome message how it will look like.")
    @blacklist_check()
    @ignore_check()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def welcmtestt(self, ctx):

        data = getDB(ctx.guild.id)

        msg = data["welcome"]["message"]

        chan = list(data["welcome"]["channel"])

        emtog = data["welcome"]["embed"]

        emping = data["welcome"]["ping"]

        emimage = data["welcome"]["image"]

        emthumbnail = data["welcome"]["thumbnail"]

        emautodel = data["welcome"]["autodel"]

        emfooter = data["welcome"]["footer"]

        emtitle = data["welcome"]["title"]

        emc = data["welcome"]["color"]

        user = ctx.author

        

        if chan == []:

            ok = discord.Embed(

                color=0x2f3136,

                description=

                f" Kindly setup your welcome channel first .",

                timestamp=ctx.message.created_at)

            ok.set_author(name=f"{ctx.author.name}",

                              icon_url=f"{ctx.author.display_avatar}")

            await ctx.send(embed=ok)

        else:

            if "{server.name}" in msg:

                msg = msg.replace("{server.name}", "%s" % (user.guild.name))

            if "{server.member_count}" in msg:

                msg = msg.replace("{server.member_count}",

                                  "%s" % (user.guild.member_count))

            if "<<user.name>>" in msg:

                msg = msg.replace("{user.name}", "%s" % (user))

            if "{user.mention}" in msg:

                msg = msg.replace("{user.mention}", "%s" % (user.mention))

            if "{user.created_at}" in msg:

                msg = msg.replace("{user.created_at}",

                                  f"<t:{int(user.created_at.timestamp())}:F>")

            if "{user.joined_at}" in msg:

                msg = msg.replace("{user.joined_at}",

                                  f"<t:{int(user.joined_at.timestamp())}:F>")

            if emping == "":

                emping = ""

            

            if "{user.mention}" in emping:

                emping = emping.replace("{user.mention}", "%s" % (user.mention))				

            else:

                emping = ""

            if emautodel == 0 or emautodel == "":

                emautodel = None

            else:

                emautodel = emautodel
            if emc == "":
                emc = ""
         #   else:
          #      emc = 0x2f3136
            if emtitle == "":

                emtitle = ""

            if "{user.name}" in emtitle:

              emtitle = emtitle.replace("{user.name}", "%s" % (user))

            if emfooter == "":

                emfooter = "" 

            if "{server.name}" in emfooter:

                emfooter = emfooter.replace("{server.name}", "%s" % (user.guild.name))

            if "{server.member_count}" in emfooter:

                emfooter = emfooter.replace("{server.member_count}",

                                  "%s" % (user.guild.member_count))

            if "{user.name}" in emfooter:

                emfooter = emfooter.replace("{user.name}", "%s" % (user))

            

            

				

            em = discord.Embed(title=emtitle,description=msg, color=0x2f3136)

            em.timestamp = discord.utils.utcnow()

            ok1 = {emautodel}

            if emimage == "":

                em.set_image(url="")

            else:

                em.set_image(url=emimage)

            if emthumbnail == "":

                em.set_thumbnail(url="")

            else:

                em.set_thumbnail(url=emthumbnail)

            if user.guild.icon is not None:

            

                em.set_footer(text=emfooter,icon_url=user.guild.icon)

                em.set_author(name=ctx.author.name,icon_url=ctx.author.display_avatar)

                           

            for chann in chan:

                channn = self.bot.get_channel(int(chann))

            if emtog == True:

                await channn.send(emping,embed=em)

            else:

                if emtog == False:

                    await channn.send(msg, delete_after=ok1)
  

         
         
          

     
             
      
            
         
           
                                  
           
                
            

            
				


           

    
            
  
                
          
              
           
              


async def setup(bot):
    await bot.add_cog(welcomer(bot)) 