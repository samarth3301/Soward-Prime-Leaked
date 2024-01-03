from __future__ import annotations

from discord.ext import commands

from core import Context

import discord

from prince1.Tools import *

from prince.bot import Bot
from discord.ui import Button, View
from discord.ext.commands import Cog

from prince.custom_checks import voter_only

import json

#from prince1.Tools import server_owner

import motor.motor_asyncio as mongodb
from prince1.Tools2 import *
#from prince1.Tools2 import getExt,updateExt

class Antinuke(Cog,name="Antinuke"):

  """Shows a list of commands regarding antinuke"""

  def __init__(self, client):

    self.client = client

    

    

    

  @commands.group(name="antinuke", help="Enables/Disables antinuke in your server!", invoke_without_command=True)

  

  @commands.cooldown(1, 10, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  @blacklist_check()
  @ignore_check()

 # @voter_only()

  async def _antinuke(self, ctx: Context):

    if ctx.subcommand_passed is None:

        await ctx.send_help(ctx.command)

        ctx.command.reset_cooldown(ctx)

  

  @_antinuke.command(name="enable", help="Server owner should enable antinuke for the server!", aliases=["on"])

  

  @commands.cooldown(1, 10, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()
  @ignore_check()

  async def antinuke_enable(self, ctx: Context):

    data = getanti(ctx.guild.id)

    

    d2 = getConfig(ctx.guild.id)
  #  data2 = getExt(ctx.guild.id)

    wled = d2["whitelisted"]

    punish = d2["punishment"]

    ok = d2["extraowner"]

    if ctx.author.id == ctx.guild.owner_id or str(ctx.author.id) in ok:

      if data == "on":

        embed = discord.Embed(title="Soward", description=f"**Antinuke already enabled on this server** \n To disable antinuke  use `antinuke disable`\n Status: enabled <:enabled:1017426787438960651>", color=discord.Colour(0xFF1B1B), timestamp=ctx.message.created_at)

        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)

        if ctx.guild.icon:

          embed.set_thumbnail(url=ctx.guild.icon)

        embed.set_footer(text="Made by prince", icon_url="https://images-ext-1.discordapp.net/external/XrJavR2bQK47KNCY3DnTog-f4QPNg2NQLI-_UV5zRCM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1004248513435152484/901eaf50a9e389a7e00cab6c06a2bb59.png")

          

        await ctx.reply(embed=embed, mention_author=False)

      else:

        data = "on"

        updateanti(ctx.guild.id, data)

        embed2 = discord.Embed(title="__Soward__", description=f"**{ctx.guild.name} Antinuke Status** \nMove my role above for more protection \n\n**Successfully enabled Antinuke**\n **Anti Kick** <:enabled:1017426787438960651> \n**Anti Ban**<:enabled:1017426787438960651> \n**Anti prune** <:enabled:1017426787438960651> \n**Anti Bot** <:enabled:1017426787438960651> \n **Anti Role** <:enabled:1017426787438960651> \n**Anti Channel** <:enabled:1017426787438960651> \n**Anti Emoji** <:enabled:1017426787438960651> \n**Anti webhook create** <:enabled:1017426787438960651> \n**Anti Community Spam** <:enabled:1017426787438960651> \n**Anti Guild Update** \n**Anti Integration Create:** <:enabled:1017426787438960651>", color=discord.Colour(0x42f579), timestamp=ctx.message.created_at)

        embed2.add_field(name="**__Auto Recovery__**", value="Enabled")

        embed2.add_field(name="**__EXTRA OWNERS__**", value=len(ok))

        embed2.add_field(name="**__Extra settings__**", value=f"To change the punishment type `{ctx.prefix}punishment set <ban/kick>`")

        embed2.add_field(name=f"**__Current punishment type__**", value=f"{punish}")

        embed2.set_footer(text=f"Made By Prince", icon_url="https://images-ext-1.discordapp.net/external/XrJavR2bQK47KNCY3DnTog-f4QPNg2NQLI-_UV5zRCM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1004248513435152484/901eaf50a9e389a7e00cab6c06a2bb59.png")

        if ctx.guild.icon:

          embed2.set_thumbnail(url=f"{ctx.guild.icon}")

        embed2.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)

        await ctx.reply(embed=embed2, mention_author=False)

    else:

      await ctx.reply("You must be the guild owner or extra owner to use this command!", mention_author=False)

  @_antinuke.command(name="disable", help="You can disable antinuke for your server using this command", aliases=["off"])

  

  @commands.cooldown(1, 10, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  @ignore_check()

  async def antinuke_disable(self, ctx: Context):

    data = getanti(ctx.guild.id)

   # data2 = getExt(ctx.guild.id)

    d2 = getConfig(ctx.guild.id)

   # bc = d2["extraowner"]

    ok = d2["extraowner"]

    if ctx.author.id == ctx.guild.owner_id or str(ctx.author.id) in ok:

      if data == "off":

        emb = discord.Embed(title="**__Soward Prime__**", description=" Antinuke already disabled in this server\nCurrent Status: Disabled <:off:1031276015152021604>\n\nTo enable Antinuke use `antinuke enable`", color=0x42f579, timestamp=ctx.message.created_at)

        emb.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)

        if ctx.guild.icon:

          emb.set_thumbnail(url=ctx.guild.icon)

        emb.set_footer(text="Made By Prince")

        await ctx.reply(embed=emb, mention_author=False)

      else:

        data = "off"

        updateanti(ctx.guild.id, data)

        swrd = discord.Embed(title="Soward Prime", description=f"Successfully disabled Antinuke for this server \n\nCurrent Status: Disabled <:off:1031276015152021604> \n\n To enable Antinuke use `antinuke enable`", color=0xFF1B1B, timestamp=ctx.message.created_at)

        swrd.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)

        if ctx.guild.icon:

          swrd.set_thumbnail(url=ctx.guild.icon)

        swrd.set_footer(text="Made By Prince")

        await ctx.reply(embed=swrd, mention_author=False)

    else:

      await ctx.reply("You must be the guild owner or extra owner to use this command!", mention_author=False)

  @_antinuke.command(name="config", help="Shows currently antinuke config settings of your server")

  

  @commands.has_permissions(administrator=True)

  @commands.cooldown(1, 10, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  @ignore_check()

  async def antinuke_config(self, ctx: Context):

    data = getanti(ctx.guild.id)

    d2 = getConfig(ctx.guild.id)

    wled = d2["whitelisted"]

    punish = d2["punishment"]
    ext = d2["extraowner"]

    if data == "off":

      emb = discord.Embed(title="**__Soward Prime__**", description=f"**{ctx.guild.name} Antinuke Status **\n Antinuke  disabled in this server \n\nCurrent Status:- Disabled  <:off:1031276015152021604>\n\n To enable use \n`antinuke enable`", color=0x42f579, timestamp=ctx.message.created_at)

      if ctx.guild.icon:

        emb.set_thumbnail(url=ctx.guild.icon)

      emb.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)

      emb.set_footer(text="Made By Prince")

      await ctx.reply(embed=emb, mention_author=False)

    elif data == "on":

      embed2 = discord.Embed(title="**__Soward Prime__**", description=f"**Antinuke settings for** {ctx.guild.name}\n\n**Move my role above for more protection** \n\n**Anti Kick** <:enabled:1017426787438960651> \n**Anti Ban**<:enabled:1017426787438960651> \n**Anti prune** <:enabled:1017426787438960651> \n**Anti Bot** <:enabled:1017426787438960651> \n **Anti Role** <:enabled:1017426787438960651> \n**Anti Channel** <:enabled:1017426787438960651> \n**Anti Emoji** <:enabled:1017426787438960651> \n**Anti webhook create** <:enabled:1017426787438960651> \n**Anti Community Spam** <:enabled:1017426787438960651> \n**Anti Guild Update** \n**Anti Integration Create:** <:enabled:1017426787438960651>", color=discord.Colour(0x42f579), timestamp=ctx.message.created_at)

      embed2.add_field(name="**__Extra__**", value=f"To change the punishment type `{ctx.prefix}punishment set <kick/ban>`")

      embed2.add_field(name="**__Whitelisted users__**", value=len(wled))
      embed2.add_field(name="**__Extra Owner(s)__**",value=len(ext))

      embed2.add_field(name=f"**__Current punishment type__**" , value=f"{punish}")

      embed2.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)

      embed2.set_footer(text="Made By Prince")

      if ctx.guild.icon:

        embed2.set_thumbnail(url=ctx.guild.icon)

      

      await ctx.reply(embed=embed2, mention_author=False)

  #@_antinuke.command(name="recover",aliases=["rcvr"],help="Deletes all channels with name of rules and moderator-only")

  

 # @commands.has_permissions(administrator=True)

  #@commands.cooldown(1, 10, commands.BucketType.user)

 # @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  #@voter_only()

  #@commands.guild_only()

  #async def _recover(self, ctx: Context):

   #2 for channel in ctx.guild.channels:

     #   if channel.name in ('rules', 'moderator-only'):

       #     try:

        #        await channel.delete()

     #       except:

      #          pass

  #  await ctx.reply(embed=discord.Embed(title=f"Successfully Deleted All Channels With Name Of `rules, moderator-only`", mention_author=False), color=0xFF1B1B)

  @_antinuke.group(name="punishment", help="Changes Punishment of antinuke and antiraid for this server.", invoke_without_command=True)

  @blacklist_check()
  @ignore_check()
  @commands.has_permissions(administrator=True)

  @commands.cooldown(1, 10, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  async def _punishment(self, ctx):

    if ctx.subcommand_passed is None:

        await ctx.send_help(ctx.command)

        ctx.command.reset_cooldown(ctx)

  @_punishment.command(name="set", help="Changes Punishment of antinuke  for this server.", aliases=["change"])

  

  @commands.has_permissions(administrator=True)

  @commands.cooldown(1, 10, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  async def punishment_set(self, ctx, punishment: str):

        data = getConfig(ctx.guild.id)

    #    prince = getExt(ctx.guild.id)

        op = data["extraowner"]

        owner = ctx.guild.owner

        if ctx.author == owner or str(ctx.author.id) in op:

            kickOrBan = punishment.lower()

            if kickOrBan == "kick":

                data = getConfig(ctx.guild.id)

                data["punishment"] = "kick"

                await ctx.reply(embed=discord.Embed(title=f"Punishment set To **{kickOrBan}**", color=0xFF1B1B))

                updateConfig(ctx.guild.id, data)

            elif kickOrBan == "ban":

                data = getConfig(ctx.guild.id)

                data["punishment"] = "ban"

                await ctx.reply(embed=discord.Embed(title=f"Punishment Set To **{kickOrBan}**", color=0xFF1B1B))

                updateConfig(ctx.guild.id, data)

            elif kickOrBan == "none":

                data = getConfig(ctx.guild.id)

                data["punishment"] = "none"

                await ctx.reply(embed=discord.Embed(title=f"Punishment Changed To **{kickOrBan}**", color=0xFF1B1B))

                updateConfig(ctx.guild.id, data)

            else:

               await ctx.reply(embed=discord.Embed(title=f"Invalid Punishment Type\nValid Punishment  Kick, Ban", color=0xFF1B1B))

        else:

            await ctx.reply(embed=discord.Embed(title="This Command Can Only be Executed By This Server Owner or extra owners", color=0xFF1B1B))

  @_punishment.command(name="show", help="Shows custom punishment type for this server")

  @blacklist_check()

  @ignore_check()

  @commands.has_permissions(administrator=True)

  @commands.cooldown(1, 10, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  async def punishment_show(self, ctx: Context):

    data = getConfig(ctx.guild.id)

    punish = data["punishment"]

    await ctx.reply(embed=discord.Embed(title="Antinuke punishment in this server is: **{}**".format(punish.title(), color=0xFF1B1B)))

 

     

  @_antinuke.group(name="whitelist",aliases=["wl"], help="Whitelist your TRUSTED users for anti-nuke" )

  @blacklist_check()
  @ignore_check()
  @commands.cooldown(1, 4, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  @commands.has_permissions(administrator=True)

  async def _whitelist(self, ctx):
      ...
      if ctx.subcommand_passed is None:

        await ctx.send_help(ctx.command)

      ctx.command.reset_cooldown(ctx)

      

  @_whitelist.command(name="add", help="Add a user to whitelisted users")

  @ignore_check()

  @commands.cooldown(1, 4, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  

  @commands.has_permissions(administrator=True)

  async def whitelist_add(self, ctx, user: discord.User):
  

    data = getConfig(ctx.guild.id)

    prince = getConfig(ctx.guild.id)

    wled = data["whitelisted"]

    op = prince["extraowner"]

    owner = ctx.guild.owner
    with open ("premium.json","r") as f:

        member = json.load(f)

        prm = member["guild"]

    if ctx.author == owner or str(ctx.author.id) in op:

      if len(wled) == 7 and str(ctx.guild.id) not in prm:

        embed = discord.Embed(title="This server have already maximum number of whitelisted users (7) Buy Premium to add More",color=0x2f3136)
        embed.set_thumbnail(url=self.client.user.avatar)
        embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)
        embed.set_footer(text="Made By Prince",icon_url=self.client.user.avatar)

                

                

                

        B = Button(label='Get Premium',emoji="<a:Diamonds:1087431201117179944>" ,style=discord.ButtonStyle.link,url='https://discord.gg/soward')

        view = View()

        view.add_item(B)

        return await ctx.send(embed=embed,view=view)

      else:

        if str(user.id) in wled:

          await ctx.reply(embed=discord.Embed(title="That user is already  whitelisted!", color=0x42f579))

        else:

          wled.append(str(user.id))

          updateConfig(ctx.guild.id, data)

          await ctx.reply(embed=discord.Embed(title=" **{}** has been added to the whitelist".format(user), color=0x42f579))

    else:

          await ctx.reply(embed=discord.Embed(title="You must be guild owner or extra owner to whitelist someone  ", color=0x42f579))

  @_whitelist.command(aliases=["uwl, unwhitelist"], name="remove", help="Remove a user from whitelisted users")
  @ignore_check()
  

  @commands.cooldown(1, 4, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  

  @commands.has_permissions(administrator=True)

  async def whitelist_remove(self, ctx, user: discord.User):

    data = getConfig(ctx.guild.id)

    prince = getConfig(ctx.guild.id)

    wled = data["whitelisted"]

    op = prince["extraowner"]

    owner = ctx.guild.owner

    if ctx.author == owner or str(ctx.author.id) in op:

      if str(user.id) in wled:

        wled.remove(str(user.id))

        updateConfig(ctx.guild.id, data)

        await ctx.reply(embed=discord.Embed(title="**{}** has been removed from the whitelist".format(user), color=0x42f579))

      else:

        await ctx.reply(embed=discord.Embed(title="That user was never whitelisted", color=0x42f579))

    else:

      await ctx.reply(embed=discord.Embed(title="You must be the guild owner or extra owner to remove someone from whitelist", color=0x42f579))

  @_whitelist.command(name="show", help="Check who are in whitelist database")

  @blacklist_check()

  @ignore_check()

  @commands.cooldown(1, 4, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  @commands.has_permissions(administrator=True)

  async def whitelist_show(self, ctx):

      data = getConfig(ctx.guild.id)

      wled = data["whitelisted"]

      if len(wled) == 0:

        await ctx.reply("nothing found in this guild!", mention_author=False)

      else:

        embed = discord.Embed(title="Soward", description="Whitelisted users for this server:\n", color=discord.Colour(0x42f579), timestamp=ctx.message.created_at)

      for idk in wled:

        embed.description += f"<@{idk}> \n"

        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)

        if ctx.guild.icon:

          embed.set_thumbnail(url=ctx.guild.icon)

      await ctx.reply(embed=embed, mention_author=False)

  @_whitelist.command(name="reset", help="removes every user from whitelist database", aliases=["clear"])

  @ignore_check()

  @commands.cooldown(1, 4, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  @commands.has_permissions(administrator=True)

  async def wl_reset(self, ctx: Context):

      data = getConfig(ctx.guild.id)

    #  prince = getExt(ctx.guild.id)

      op = data["extraowner"]

      data["whitelisted"] = []

      if ctx.author.id == ctx.guild.owner_id or str(ctx.author.id) in op:

        updateConfig(ctx.guild.id, data)

        await ctx.reply(embed=discord.Embed(title="Successfully Removed all whitelisted users ", color=0x42f579))

      else:

        await ctx.reply(embed=discord.Embed(title="You must be the guild owner to use this command", color=0x42f579))

  @_antinuke.group(name="extraowner", aliases=["ext","ex","trusty"], help="add  your TRUSTED users as owner", invoke_without_command=True)

  @blacklist_check()
  @ignore_check()
  @commands.cooldown(1, 4, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  @commands.has_permissions(administrator=True)

  async def _extraowner(self, ctx):

    if ctx.subcommand_passed is None:

        await ctx.send_help(ctx.command)

        ctx.command.reset_cooldown(ctx)

      

  @_extraowner.command(name="add", help="Add a user to extra owner")

  @ignore_check()

  @commands.cooldown(1, 4, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  @commands.has_permissions(administrator=True)

  async def extraowner_add(self, ctx, user: discord.User):

    data = getConfig(ctx.guild.id)

    ex = data["extraowner"]

    owner = ctx.guild.owner
    with open ("premium.json","r") as f:
        prince = json.load(f)
        prm = prince["guild"]

    embed = discord.Embed(title="**You discovered a premium feature**",color=0x42f579)

    embed.set_footer(text="Made By Prince")

    B = Button(label='get premium',emoji="<a:Diamonds:1087431201117179944>" ,style=discord.ButtonStyle.link,url='https://discord.gg/JUCyurj7gR')

    view = View()

    view.add_item(B)   

    if str(ctx.guild.id) not in prm:           

        await ctx.reply(embed=embed,view=view)

        return

    if ctx.author == owner or ctx.message.author.id == 1018139793789563000 or ctx.author.id == 980361546918162482:

      if len(ex) == 5:

        await ctx.reply(embed=discord.Embed(title="This server have already maximum number of extra owners  (5)\nRemove one to add another", color=0x42f579))

      else:

        if str(user.id) in ex:

          await ctx.reply(embed=discord.Embed(title="That user is already  in extra owner!", color=0x42f579))

        else:

          ex.append(str(user.id))

          updateConfig(ctx.guild.id, data)

          await ctx.reply(embed=discord.Embed(title=" **{}** has been added to the extra owner".format(user), color=0x42f579))

    else:

          await ctx.reply(embed=discord.Embed(title="You must be guild owner to use this command", color=0x42f579))

  @_extraowner.command(aliases=["eor"], name="remove", help="Remove a user from whitelisted users")

  @ignore_check()

  @commands.cooldown(1, 4, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  @commands.has_permissions(administrator=True)

  async def extraowner_remove(self, ctx, user: discord.User):

    data = getConfig(ctx.guild.id)

    ex = data["extraowner"]

    owner = ctx.guild.owner

    if ctx.author == owner:

      if str(user.id) in ex:

        ex.remove(str(user.id))

        updateConfig(ctx.guild.id, data)

        await ctx.reply(embed=discord.Embed(title="**{}** has been removed from extra owmer".format(user), color=0x42f579))

      else:

        await ctx.reply(embed=discord.Embed(title="That user was never added in extra owner", color=0x42f579))

    else:

      await ctx.reply(embed=discord.Embed(title="You must be the guild owner to remove extra owner", color=0x42f579))

  @_extraowner.command(name="show", help="Check who are in extra owner database")

  @blacklist_check()
  @ignore_check()
  @commands.cooldown(1, 4, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  @commands.has_permissions(administrator=True)

  async def extraowner_show(self, ctx):

      data = getConfig(ctx.guild.id)

      ex = data["extraowner"]

      if len(ex) == 0:

        await ctx.reply("nothing found in this guild!", mention_author=False)

      else:

        embed = discord.Embed(title="Soward Prime", description="extra owner for this server:\n", color=discord.Colour(0x42f579), timestamp=ctx.message.created_at)

      for idk in ex:

        embed.description += f"<@{idk}> \n"

        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)

        if ctx.guild.icon:

          embed.set_thumbnail(url=ctx.guild.icon)

      await ctx.reply(embed=embed, mention_author=False)

  @_extraowner.command(name="reset", help="removes every user from extra owner database", aliases=["clear"])

  @ignore_check()

  @commands.cooldown(1, 4, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

  @commands.guild_only()

  @commands.has_permissions(administrator=True)

  async def extraowmer_reset(self, ctx: Context):

    if ctx.author.id == ctx.guild.owner_id:

      data = getConfig(ctx.guild.id)

      data["extraowner"] = []

      updateConfig(ctx.guild.id, data)

      await ctx.reply(embed=discord.Embed(title="Successfully Removed all extra owners", color=0x42f579))

    else:

      await ctx.reply(embed=discord.Embed(title="You must be the guild owner to use this command", color=0x42f579))

  @_antinuke.command(name="features")

  @blacklist_check()
  @ignore_check()
  async def features(self,ctx):

      em = discord.Embed(description=f"**Antinuke Events** <:eg_shield:1018057685637275670>\nMove my role above for more protection.\n\nAnti Ban\nAnti Bot \nAnti Channel create  \nAnti Channel delete: \nAnti Channel update: \nAnti Guild update \nAnti Kick \nAnti Member update \nAnti Role create \nAnti Role delete \nAnti Role update: \nAnti Webhook: \nAnti prune \nAnti integration create \nAnti Emoji create \nAnti emoji update \nAnti emoji delete \nAnti community spam \nAnti guild update ", color=0x42f579, timestamp=ctx.message.created_at)

      em.set_thumbnail(url=self.client.user.display_avatar.url)

      em.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)

      em.set_footer(text="Made By Prince", icon_url="https://images-ext-2.discordapp.net/external/XpYSeN_4K1TG8OtzI3R3LE3zXbhvqB1rwgQkKRSs-Ww/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/980361546918162482/aa3b4e68dd27540854c0e0e3f374fe32.png")

      await ctx.send(embed=em)

async def setup(client):

    await client.add_cog(Antinuke(client))