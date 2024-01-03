from __future__ import annotations
import discord
import asyncio
import os
import logging
from discord.ext import commands
#from utils.Tools import *
from discord.ext.commands import Context
from discord import app_commands
import time
import datetime
import re
from typing import *
from time import strftime
#from core import Cog, Ventura, Context
from discord.ext import commands
from prince1.Tools import *
from discord.utils import get
from discord.ui import *
logging.basicConfig(
    level=logging.INFO,
    format=
    "\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)


class Autoroles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="autorole", invoke_without_command=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @blacklist_check()
    @ignore_check()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _autorole(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    @_autorole.command(name="config",aliases=["Show"])
   # @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def _ar_config(self, ctx):
        data = getVC(ctx.guild.id)
        human_autoroles = data["autorole"]["humans"]
        bot_at = data["autorole"]["bots"]
        hrole = []
        brole = []
        if human_autoroles == [] and bot_at == []:
          hrole.append("No Human Auto-Roles.")
          brole.append("No Bot Auto-Roles.")
          embed = discord.Embed(title="Autoroles",color=0x2f31356)
          embed.add_field(name="Human Auto-Roles", value="\n".join(hrole))
          embed.add_field(name="Bot Auto-Roles", value="\n".join(brole))
          embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
          await ctx.reply(embed=embed)
          return
        else:
          hrole = []
          brole = []
          #num += 1
          if human_autoroles == []:
            hrole.append("No Human Auto-Roles.")
          else:
            for hid in human_autoroles:
              try:
                role = get(ctx.guild.roles,id=int(hid))
                hrole.append(str(f"[+] {role.mention}"))
              except:
                print("role not found")
            if hrole == []:
              hrole.append("No Human Auto-Roles.")
          if bot_at == []:
            brole.append("No Bot Auto-Roles.")
          else:
            for bid in bot_at:
              try:
                role = get(ctx.guild.roles,id=int(bid))
                brole.append(str(f"[+] {role.mention}"))
              except:
                  print("role not found")
            if brole == []:
              brole.append("No Bot Auto-Roles.")
          embed = discord.Embed(title="Autoroles",color=0x2f3136)
          embed.add_field(name="Human Auto-Roles", value="\n".join(hrole))
          embed.add_field(name="Bot Auto-Roles", value="\n".join(brole))
          embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
          await ctx.reply(embed=embed)
              
                      

      
          
           
           
          



        





                      


















            


            
            

            
    @_autorole.group(name="reset",
                     help="reset autorole config for the server .")
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def _autorole_reset(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    @_autorole_reset.command(name="humans",
                             help="Clear autorole config for the server .")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def _autorole_humans_reset(self, ctx):
        data = getVC(ctx.guild.id)
        rl = data["autorole"]["humans"]
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
          op = discord.Embed(
                description=
                """```diff\n - You must have Administrator permission.\n - Your top role should be above my top role. \n```""",
                color=0x2f3136)
          op.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.display_avatar}")

          return await ctx.send(embed=op)

        if rl == []:
                embed = discord.Embed(
                    description=
                    "<:Wrong:1017402708703064144> | This server don't have any autoroles setupped .",
                    color=0x2f3136)
                await ctx.send(embed=embed)
        else:
                if rl != []:
                    data["autorole"]["humans"] = []
                    updateVC(ctx.guild.id, data)
                    hacker = discord.Embed(
                        description=
                        f"<:Icons_correct:1017402689027592222> | Succesfully cleared all human autoroles for {ctx.guild.name} .",
                        color=0x2f3136)
                    await ctx.send(embed=hacker)
                
            
    @_autorole_reset.command(name="bots")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def _autorole_bots_reset(self, ctx):
        data = getVC(ctx.guild.id)
        rl = data["autorole"]["bots"]
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
          hacker5 = discord.Embed(
                description=
                """```diff\n - You must have Administrator permission.\n - Your top role should be above my top role. \n```""",
                color=0x2f3136)
          hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.display_avatar}")

          return await ctx.send(embed=hacker5)

          if rl == []:
                embed = discord.Embed(
                    description=
                    f"<:Wrong:1017402708703064144> | This server don't have any autoroles setupped .",
                    color=0x2f3136)
                await ctx.send(embed=embed)
          else:
                if rl != []:
                    data["autorole"]["bots"] = []
                    updateVC(ctx.guild.id, data)
                    hacker = discord.Embed(
                        description=
                        f"<:Icons_correct:1017402689027592222> | Succesfully cleared all bot autoroles for this server .",
                        color=0x2f3136)
                    await ctx.send(embed=hacker)
      #  else:
            
    @_autorole_reset.command(name="all")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _autorole_reset_all(self, ctx):
        data = getVC(ctx.guild.id)
        brl = data["autorole"]["bots"]
        hrl = data["autorole"]["humans"]
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
          hacker5 = discord.Embed(
                description=
                """```diff\n - You must have Administrator permission.\n - Your top role should be above my top role. \n```""",
                color=0x2f3136)
          hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.display_avatar}")

          return await ctx.send(embed=hacker5)

          if len(brl) == 0 and len(hrl) == 0:
                embed = discord.Embed(
                    description=
                    f"<:Wrong:1017402708703064144> | This server don't have any autoroles setupped .",
                    color=0x2f3136)
                await ctx.send(embed=embed)
          else:
                if hrl != []:
                    data["autorole"]["bots"] = []
                    data["autorole"]["humans"] = []
                    updateVC(ctx.guild.id, data)
                    hacker = discord.Embed(
                        description=
                        f"<:Icons_correct:1017402689027592222> | Succesfully cleared all autoroles for this server .",
                        color=0x2f3136)
                    await ctx.send(embed=hacker)
     #   else:
            
    @_autorole.group(name="humans", help="Setup humans autoroles")
    @blacklist_check()
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _autorole_humans(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    @_autorole_humans.command(name="add",
                              help="Add role to list of autorole humans"
                              )
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _autorole_humans_add(self, ctx, role: discord.Role):
        data = getVC(ctx.guild.id)
        rl = data["autorole"]["humans"]
        me = ctx.guild.me
        with open ("premium.json","r") as f:

            member = json.load(f)

            prm = member["guild"]
            if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
                hacker5 = discord.Embed(description="""```diff\n - You must have Administrator permission.\n - Your top role should be above my top role. \n```""",color=0x2f3136)

                hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.display_avatar}")

                return await ctx.send(embed=hacker5)
            if len(rl) == 3 and str(ctx.guild.id) not in prm :

                embed = discord.Embed(title="This Server Reached Maximum Auto Roles  Which Is (3) Buy Premium for Add More*",color=0x2f3136)
                embed.set_thumbnail(url=self.bot.user.avatar)
                embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)
                embed.set_footer(text="Made By Prince",icon_url=self.bot.user.avatar)
                B = Button(label='Get Premium',emoji="<a:Diamonds:1087431201117179944>" ,style=discord.ButtonStyle.link,url='https://discord.gg/soward')
                view = View()

                view.add_item(B)

                return await ctx.send(embed=embed,view=view)

                                

                            

                            

                        

                        
        if role.permissions.administrator or role.permissions.ban_members or role.permissions.kick_members or role.permissions.manage_channels or role.permissions.mention_everyone or role.permissions.manage_roles:
                await ctx.reply(embed=discord.Embed(title="<:Wrong:1017402708703064144> | you can't use role with dangerous perms",color=0x2f3136))
                return
        if role.position >= ctx.author.top_role.position and ctx.message.author.id != ctx.guild.owner_id:

                await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))
                return 
        if role.managed: return await ctx.send(embed=discord.Embed(description="Integration roles cannot be added"))

   
        else:
            if str(role.id) in rl:
              embed1 = discord.Embed(description="<:Wrong:1017402708703064144> | {} is already in human autoroles .".format(role.mention),color=0x2f3136)
              await ctx.send(embed=embed1)
            else:
                rl.append(str(role.id))
                updateVC(ctx.guild.id, data)
                hacker = discord.Embed(description=f"<:Icons_correct:1017402689027592222> | {role.mention} has been added to human autoroles .",color=0x2f3136)
                await ctx.send(embed=hacker)
       
            

    @_autorole_humans.command(
        name="remove", help="Remove a role from autoroles for human .")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _autorole_humans_remove(self, ctx, role: discord.Role):
        data = getVC(ctx.guild.id)
        rl = data["autorole"]["humans"]
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
          hacker5 = discord.Embed(
                description=
                """```diff\n - You must have Administrator permission.\n - Your top role should be above my top role. \n```""",
                color=0x2f3136)
          hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.display_avatar}")

          return await ctx.send(embed=hacker5)
          if len(rl) == 0:
                embed = discord.Embed(
                    description=
                    f"<:Wrong:1017402708703064144> | This server dont have any autrole humans setupped yet .",
                    color=0x2f3136)
                await ctx.send(embed=embed)
          else:
                if str(role.id) not in rl:
                    embed1 = discord.Embed(
                        description="{} is not in human autoroles .".format(
                            role.mention),
                        color=0x2f3136)
                    await ctx.send(embed=embed1)
                else:
                    rl.remove(str(role.id))
                    updateVC(ctx.guild.id, data)
                    hacker = discord.Embed(
                        description=
                        f"<:Icons_correct:1017402689027592222> | {role.mention} has been removed from human autoroles .",
                        color=0x2f3136)
                    await ctx.send(embed=hacker)
        
            

    @_autorole.group(name="bots", help="Setup autoroles for bots.")
    @blacklist_check()
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _autorole_bots(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    @_autorole_bots.command(name="add",
                            help="Add role to list of autorole bots")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _autorole_bots_add(self, ctx, role: discord.Role):
        data = getVC(ctx.guild.id)
        rl = data["autorole"]["bots"]
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
          hacker5 = discord.Embed(description="""```diff\n - You must have Administrator permission.\n - Your top role should be above my top role. \n```""",color=0x2f3136)
          hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

          return await ctx.send(embed=hacker5)
          if len(rl) == 5:
                embed = discord.Embed(
                    description=
                    f"<:Wrong:1017402708703064144> | You have reached maximum role limit for autorole bots which is 5.",
                    color=0x2f3136)
                await ctx.send(embed=embed)
        if role.permissions.administrator or role.permissions.ban_members or role.permissions.kick_members or role.permissions.manage_channels or role.permissions.mention_everyone or role.permissions.manage_roles:
                await ctx.reply(embed=discord.Embed(title="<:Wrong:1017402708703064144> | you can't use role with dangerous perms",color=0x2f3136))
                return
        else:
                if str(role.id) in rl:
                    embed1 = discord.Embed(
                        description=
                        "<:Wrong:1017402708703064144> | {} is already in bot autoroles."
                        .format(role.mention),
                        color=0x2f3136)
                    await ctx.send(embed=embed1)
                else:
                    rl.append(str(role.id))
                    updateVC(ctx.guild.id, data)
                    hacker = discord.Embed(
                        description=
                        f"<:Icons_correct:1017402689027592222> | {role.mention} has been added to bot autoroles .",
                        color=0x2f3136)
                    await ctx.send(embed=hacker)
        
            

    @_autorole_bots.command(name="remove",
                            help="Remove a role from autoroles for bot users.")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _autorole_bots_remove(self, ctx, role: discord.Role):
        data = getVC(ctx.guild.id)
        rl = data["autorole"]["bots"]
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
          hacker5 = discord.Embed(
                description=
                """```diff\n - You must have Administrator permission.\n - Your top role should be above my top role. \n```""",
                color=0x2f3136)
        hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.display_avatar}")

        return await ctx.send(embed=hacker5)
        if len(rl) == 0:
                embed = discord.Embed(
                    description=
                    f"<:Wrong:1017402708703064144> | This server dont have any autrole bots setupped yet .",
                    color=0x2f3136)
                await ctx.send(embed=embed)
        else:
                if str(role.id) not in rl:
                    embed1 = discord.Embed(
                        description=
                        "<:Wrong:1017402708703064144> | {} is not in bot autoroles."
                        .format(role.mention),
                        color=0x2f3136)
                    await ctx.send(embed=embed1)
                else:
                    rl.remove(str(role.id))
                    updateVC(ctx.guild.id, data)
                    hacker = discord.Embed(
                        description=
                        f"<:Icons_correct:1017402689027592222> | {role.mention} has been removed from bot autoroles.",
                        color=0x2f3136)
                    await ctx.send(embed=hacker)
        
            
            
async def setup(bot):
	await bot.add_cog(Autoroles(bot))
