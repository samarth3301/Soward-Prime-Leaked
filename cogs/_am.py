import datetime
import time
import random
import requests
import json
import discord
import os
import io
from discord.ext import commands

from cogs.op.dataIO import dataIO
from cogs.op.checks import embed_perms, cmd_prefix_len, parse_prefix, get_user, hastebin
from prince.bot import Bot
from prince.ui import Paginator, PaginatorText
import utilities as tragedy
import humanize
from core import Context
import aiohttp
from prince1.Tools import *
'''Module for miscellaneous commands'''



class Misc2(commands.Cog):
    def __init__(self, client: Bot):
        self.bot = Bot

    
            
        
                
            

    

       
     
  
         
                  
        

  

       
            
            
                
       
           
               
                   

    
              
           
          

    @commands.command(aliases=['si'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    @ignore_check()

   # @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    async def serverinfo(self, ctx: commands.Context):
      vanity = "VANITY_URL" in str(ctx.guild.features)

      splash = "INVITE_SPLASH" in str(ctx.guild.features)
      animicon = "ANIMATED_ICON" in str(ctx.guild.features)
      discoverable = "DISCOVERY" in str(ctx.guild.features)
      banner = "BANNER" in str(ctx.guild.features)
      vanityFeature = "{} - Vanity URL".format(tragedy.EmojiBool(vanity)) if not vanity else "{} - Vanity URL ({})".format(tragedy.EmojiBool(vanity), str(await ctx.guild.vanity_invite())[15:])
      nsfw_level = ''
    #  button = discord.ui.Button(label=f'Server icon', style=discord.ButtonStyle.url, url=f'{ctx.guild.icon}')
      button2 = discord.ui.Button(label=f'Roles', style=discord.ButtonStyle.grey)
      view = discord.ui.View()
    #  view.add_item(button)
      view.add_item(button2)
      if ctx.guild.nsfw_level.name == 'default':
        nsfw_level = '**Default**'
      if ctx.guild.nsfw_level.name == 'explicit':
        nsfw_level = '**Explicit**'
      if ctx.guild.nsfw_level.name == 'safe':
        nsfw_level = '**Safe**'
      if ctx.guild.nsfw_level.name == 'age_restricted':
        nsfw_level = '**Age Restricted**'
      async def button2_callback(interaction: discord.Interaction):
        roles = ""
        for i in ctx.guild.roles:
          roles += "• " + str(i.mention) + "\n"
        embed1 = discord.Embed(title=f'{ctx.guild.name}', description=f'{roles}', colour=ctx.author.colour)
        await interaction.response.send_message(embed=embed1, ephemeral=True)
      embed = discord.Embed(title="")
   #   embed.set_author(name=f"{ctx.guild.name}'s information", icon_url=ctx.guild.icon)
      embed.add_field(name=f'**__ Server General Information__**', value=f"""
Owner: {ctx.guild.owner.mention}
owner tag: {ctx.guild.owner.name}
Owner Id: {ctx.guild.owner.id}
Member count: {ctx.guild.member_count}
Created: <t:{int(ctx.guild.created_at.timestamp())}:D> <t:{round(ctx.guild.created_at.timestamp())}:R>

__**Server Roles & Channels Info**__
Server Channels: {len(ctx.guild.channels)}
Server Voice Channels: {len(ctx.guild.voice_channels)}
Server Roles: {len(ctx.guild.roles)}
NSFW level: {nsfw_level}

__**Server Verification & Emojis Info**__
Verification level: {ctx.guild.verification_level.name}
Explicit Content Filter: {ctx.guild.explicit_content_filter.name}
Max Talk Bitrate: {int(ctx.guild.bitrate_limit)}kbps
Emojis: {len(ctx.guild.emojis)}
Stickers: {len(ctx.guild.stickers)}""")
      embed.add_field(name="__**Server Features**__", value="{} - Banner\n{}\n{} - Splash Invite\n{} - Animated Icon\n{} - Server Discoverable".format(tragedy.EmojiBool(banner), vanityFeature, tragedy.EmojiBool(splash), tragedy.EmojiBool(animicon), tragedy.EmojiBool(discoverable)))
      embed.add_field(name="__**Server Boost Info**__", value="Number of Boosts - {}\nBooster Role - {}\nBoost Level/Tier - {}".format( str(ctx.guild.premium_subscription_count), ctx.guild.premium_subscriber_role.mention if ctx.guild.premium_subscriber_role != None else ctx.guild.premium_subscriber_role, ctx.guild.premium_tier), inline=False)
      embed.add_field(name="__**Server Afk Info**__", value="AFK Channel: {}\nAFK Timeout: {} minute(s)\nFilesize Limit - {}".format( ctx.guild.afk_channel, str(ctx.guild.afk_timeout / 60), len(ctx.guild.emojis), len(ctx.guild.roles), humanize.naturalsize(ctx.guild.filesize_limit)), inline=False)
      embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
        
      if ctx.guild.banner:
              embed.set_image(url=ctx.guild.banner)
      if ctx.guild.icon:
                      embed.set_thumbnail(url=ctx.guild.icon)

      button2.callback = button2_callback
      await ctx.send(embed=embed, view=view)


    


   
       
 
          
       
        
       
        

   
         
            
           
            

      
         
            

        

    @commands.command(name="snick")
    @commands.is_owner()
    async def change_nickname(self, ctx, *, name: str = None):
        """ Change nickname. """
        try:
            await ctx.guild.me.edit(nick=name)
            if name:
                await ctx.send(f"Successfully changed nickname to **{name}**")
            else:
                await ctx.send("Successfully removed nickname")
        except Exception as err:
            await ctx.send(err)
         
 #   @commands.command(name="savatar")
  #  @commands.is_owner()
#    async def change_avatar(self, ctx, url: str = None):
  #      """ Change avatar. """
   #     if url is None and len(ctx.message.attachments) == 1:
   #         url = ctx.message.attachments[0].url
  #      else:
  #          url = url.strip("<>") if url else None

   #     try:
   #         bio = await http.get(url, res_method="read")
  #          await self.bot.user.edit(avatar=bio)
  #          await ctx.send(f"Successfully changed the avatar. Currently using:\n{url}")
  #      except aiohttp.InvalidURL:
   #         await ctx.send("The URL is invalid...")
  #      except discord.InvalidArgument:
   #         await ctx.send("This URL does not contain a useable image")
     #   except discord.HTTPException as err:
   #         await ctx.send(err)
   #     except TypeError:
   #         await ctx.send("You need to either provide an image URL or upload one with the command")
    
    

    
 
    
        
        
            

    


async def setup(bot):
    await bot.add_cog(Misc2(bot))
