import os

import re

import ast

import json

import random

import urllib

import discord

import inspect
from discord.ui import *
import base64

import asyncio

import aiohttp

import datetime

import requests

#import giphy_client
from prince1.Tools import *
import aiosqlite

from discord import utils 

from io import BytesIO

from discord import ui

from pyfiglet import Figlet

from asyncio import sleep

from urllib.request import urlopen

from discord.ext import commands

from discord.ext import tasks

from discord.ui import Button, View

#from giphy_client.rest import ApiException

from discord.utils import get

class customrole(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.Cog.listener()

    async def on_ready(self):

        setattr(self.bot, "db", await aiosqlite.connect("main.db"))

        async with self.bot.db.cursor() as cursor:

            await cursor.execute("CREATE TABLE IF NOT EXISTS customrole (trigger TEXT, role INTEGER, guild INTEGER)")

        await self.bot.db.commit()

    

    @commands.group(aliases = ['setup'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    @ignore_check()

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    async def _setup(self, ctx):

         if ctx.subcommand_passed is None:

            await ctx.send_help(ctx.command)

            ctx.command.reset_cooldown(ctx)

            

    @_setup.command()

    @commands.has_permissions(manage_guild = True)
    @commands.cooldown(1, 3, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @ignore_check()

    @commands.guild_only()

    async def add(self, ctx, trigger, *, role:discord.Role):

        if role.permissions.administrator or role.permissions.ban_members or role.permissions.kick_members or role.permissions.manage_channels or role.permissions.mention_everyone or role.permissions.manage_roles or role.permissions.manage_guild:

            await ctx.reply(embed=discord.Embed(description =f"<:Wrong:1017402708703064144> | I Cant Add {role.mention} To My Custom Role List Because It Has Dangerous Perms",color=0x2f3136))

            return
        if role.position >= ctx.author.top_role.position:

            await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))
            return
        

      

        async with self.bot.db.cursor() as cursor:

          await cursor.execute("SELECT role, trigger FROM customrole WHERE guild = ?", (ctx.guild.id,))
          

            

            
          data = await cursor.fetchall()
          number = []
          if data:

                 for table in data:

                    op = table[1]
                    with open ("premium.json","r") as f:
                        member = json.load(f)
                        prm = member["guild"]

                    if trigger in op:

                      return await ctx.send(embed=discord.Embed(description=f"aliases {trigger} already exists pls use different aliases", color=0x2f3136))
                    
                    for ok in data:

                        number.append(ok)

                    if len(number) == 4 and str(ctx.guild.id) not in prm:
                        embed = discord.Embed(title="This Server Reached Maximum Custom Roles Aliases Which Is (5) Buy Premium For Create More Aliases*",color=0x2f3136)
                        embed.set_thumbnail(url=self.bot.user.avatar)    
                        embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)
                        embed.set_footer(text="Made By Prince",icon_url=self.bot.user.avatar)
                        B = Button(label='Get Premium',emoji="<a:Diamonds:1087431201117179944>" ,style=discord.ButtonStyle.link,url='https://discord.gg/soward')
                        view = View()
                        view.add_item(B)
                        return await ctx.send(embed=embed,view=view)

            

        async with self.bot.db.cursor() as cursor:

            

            await cursor.execute("INSERT INTO customrole VALUES (?, ?, ?)", (trigger, role.id, ctx.guild.id,))

            embed = discord.Embed(description = f""" {ctx.author.mention}: Successfully created an **Custom role** for `{trigger}`""", color = 0x2F3136)

            await ctx.reply(embed=embed)

            await self.bot.db.commit()

        #except Exception as e:

         #   print(e)

      

    @_setup.command(aliases = ['remove'])
    @commands.cooldown(1, 3, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @ignore_check()

    @commands.guild_only()
    @commands.has_permissions(manage_guild = True)

    async def delete(self, ctx, *, msg):

        try:

            async with self.bot.db.cursor() as cursor:

                await cursor.execute("DELETE FROM customrole WHERE guild = ? AND trigger LIKE ?", (ctx.guild.id, msg,))

            embed = discord.Embed(description = f"""<:Icons_correct:1017402689027592222> |  Successfully deleted the **Custom Role aliases** `{msg}`""", color = 0x2F3136)

            await ctx.reply(embed=embed)

            await self.bot.db.commit()

        except Exception as e:

            print(e)

    @_setup.command(aliases = ['list'])
    @commands.cooldown(1, 3, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @ignore_check()

    @commands.guild_only()
    @commands.has_permissions(manage_guild = True)

  
    async def show(self, ctx):
        with open("bot.json", 'r') as f:

            key = json.load(f)

            if f'{ctx.guild.id}' not in key:

              botr = "Role is not set"

            elif f'{ctx.guild.id}' in key:
              try:
                 for idk in key[str(ctx.guild.id)]:

                   br = discord.utils.get(ctx.guild.roles, id=int(idk))

                   botr = f"{br.mention}"
              except:
                   botr = "Role is not set"
        with open("artist.json", 'r') as f:

          key = json.load(f)

          if f'{ctx.guild.id}' not in key:

            artr = "Role is not set"

          elif f'{ctx.guild.id}' in key:
            try:
               for idk in key[str(ctx.guild.id)]:

                 ar = discord.utils.get(ctx.guild.roles, id=int(idk))

                 artr = f"{ar.mention}"
            except:
                 artr = "Role is not set"
        with open("mod.json", 'r') as f:

          key = json.load(f)

          if f'{ctx.guild.id}' not in key:

            modr = "Role is not set"

          elif f'{ctx.guild.id}' in key:
            try:
               for idk in key[str(ctx.guild.id)]:

                 mr = discord.utils.get(ctx.guild.roles, id=int(idk))
                 modr = f"{mr.mention}"
            except:
                 modr = "Role is not set"
            
        with open("vip.json", 'r') as f:

          key = json.load(f)

          if f'{ctx.guild.id}' not in key:
                vr = "Role is not set"
          elif f'{ctx.guild.id}' in key:
            try:
            

        

           

                for idk in key[str(ctx.guild.id)]:

                  v = discord.utils.get(ctx.guild.roles, id=int(idk))

                  vr = f"{v.mention}"
            except:
                  vr = "Role is not set"
        with open("reqrole.json","r") as f:
            key = json.load(f)
            if f'{ctx.guild.id}' not in key:
                rr = "Reqrole is not set"
            elif f'{ctx.guild.id}' in key:
               try:
                   for idk in key[str(ctx.guild.id)]:
                     xd = discord.utils.get(ctx.guild.roles,id=int(idk))
                     rr = f"{xd.mention}"
               except:
                     rr = "Role is not set"
        with open("girl.json", 'r') as f:
            key = json.load(f)

            if f'{ctx.guild.id}' not in key:

              gr = "Role is not set"

            elif f'{ctx.guild.id}' in key:
              try:
                 for idk in key[str(ctx.guild.id)]:

                   a = discord.utils.get(ctx.guild.roles, id=int(idk))

                   gr = f"{a.mention}"
              except:
                   gr = "Role is not set"
            
             

             

 

                 

       

            

        with open("official.json", 'r') as f:

            key = json.load(f)

            if f'{ctx.guild.id}' not in key:

              ofr = "Role is not set"

    #await ctx.send('')

            elif f'{ctx.guild.id}' in key:
              try:
                 for idk in key[str(ctx.guild.id)]:

                   o = discord.utils.get(ctx.guild.roles, id=int(idk))

                   ofr = f"{o.mention}"
              except:
                   ofr = "Role is not set"
        with open("friends.json", 'r') as f:

              key = json.load(f)

              if f'{ctx.guild.id}' not in key:

                fr = "Role is not set"

    #await ctx.send('')

              elif f'{ctx.guild.id}' in key:
                try:
                   for idk in key[str(ctx.guild.id)]:

                     f = discord.utils.get(ctx.guild.roles, id=int(idk))

                     fr = f"{f.mention}"
                except:
                     fr = "Role is not set"
        with open("vip.json", 'r') as f:

              key = json.load(f)

              if f'{ctx.guild.id}' not in key:

                vr = "Role is not set"

    #await ctx.send('')

              elif f'{ctx.guild.id}' in key:
                try:
                   for idk in key[str(ctx.guild.id)]:

                     vr = discord.utils.get(ctx.guild.roles, id=int(idk))

                     vr = f"{v.mention}"
                except:
                     vr = "Role is not set"
        with open("guest.json", 'r') as f:

              key = json.load(f)

              if f'{ctx.guild.id}' not in key:

                gst = "Role is not set"

    #await ctx.send('')

              elif f'{ctx.guild.id}' in key:
                try:
                   for idk in key[str(ctx.guild.id)]:

                     g = discord.utils.get(ctx.guild.roles, id=int(idk))

                     gst = f"{g.mention}"
                except:
                     gst = "role is not set"

        try:

            async with self.bot.db.cursor() as cursor:

                await cursor.execute("SELECT role, trigger FROM customrole WHERE guild = ?", (ctx.guild.id,))

                data = await cursor.fetchall()

                num = 0

                auto = ""

              

                rs = ""

                rs += f"\n[1] **Girls** -> {gr}"

                rs += f"\n[2] **Staff** -> {ofr}"

                rs += f"\n[3] **Friends** -> {fr}"

                rs += f"\n[4] **Guest** -> {gst}"
                rs += f"\n[5] **Vip** -> {vr}"
                rs += f"\n[6] **Mod** -> {modr}"
                rs += f"\n[7] **Bot** -> {botr}"
                rs += f"\n[8] **Artist** -> {artr}"
            if data:
              
              for table in data:

                  trigger = table[1]

                  role = table[0]

                        

                  num += 1

                  ok = discord.utils.get(ctx.guild.roles,id=int(role))
                  auto += f"\n[`{num}`] {trigger} -> {ok.mention}"
                   

                  
                        
              embed = discord.Embed(title="Custom Roles Setup List",description =f" {auto}\n\n**Default Setup** \n{rs}",color = 0x2F3136)
              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)
              embed.add_field(name="Reqrole",value=rr) 
              embed.set_footer(text="Made By Prince",icon_url=self.bot.user.avatar)
              await ctx.reply(embed=embed)

                        

             
                        
 
                  
                  
                  
                  

                   

                    

                

            else:

          #        auto += "loda"

                  embed = discord.Embed(description = f"{rs}", color = 0x2f3136)
                  embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)
                  embed.add_field(name="Reqrole",value=rr)
                  embed.set_footer(text="Made By Prince",icon_url=self.bot.user.avatar)

                  await ctx.reply(embed=embed)

        except Exception as e:

            await ctx.send(e)

    @_setup.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @ignore_check()

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(manage_guild = True)

    async def clear(self, ctx):

        try:

            async with self.bot.db.cursor() as cursor:

                await cursor.execute("DELETE FROM customrole WHERE guild = ?", (ctx.guild.id,))

            embed = discord.Embed(description = f"""<:Icons_correct:1017402689027592222> |   Successfully deleted **all** Custom Roles Setup""", color = 0x2F3136)

            embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

            embed.set_thumbnail(url=ctx.author.display_avatar)

            await ctx.reply(embed=embed)

            await self.bot.db.commit()

        except Exception as e:

            print(e)

    @_setup.command(name="friends",aliases=["fr","frnd","frn"])
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)

    async def setupfriend(self,ctx, role:discord.Role=None):

        if role.permissions.administrator or role.permissions.ban_members or role.permissions.kick_members or role.permissions.manage_channels or role.permissions.mention_everyone or role.permissions.manage_roles:

            await ctx.reply(embed=discord.Embed(title="you can't use role with dangerous perms",color=0x2f3136))

            return

   

        if role.position >= ctx.author.top_role.position:

           await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))
        else:

            with open('friends.json', 'r', encoding='utf-8') as f:

                key = json.load(f)

                key[str(ctx.guild.id)] = [str(role.id)]

            with open('friends.json', 'w', encoding='utf-8') as f:

                json.dump(key, f, indent=4)

                await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated Friends Role To {role.mention}", color=0x2f3136))

    
    @_setup.command(name="guests",aliases=["gst","gt"])
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)

    @blacklist_check()

    async def setupguest(self,ctx, role:discord.Role=None):

        if role.permissions.administrator or role.permissions.ban_members or role.permissions.kick_members or role.permissions.manage_channels or role.permissions.mention_everyone or role.permissions.manage_roles:

            await ctx.reply(embed=discord.Embed(title="you can't use role with dangerous perms",color=0x2f3136))

            return

     
        if role.position >= ctx.author.top_role.position:

            await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))

        else:

            with open('guest.json', 'r', encoding='utf-8') as f:

                key = json.load(f)

                key[str(ctx.guild.id)] = [str(role.id)]

            with open('guest.json', 'w', encoding='utf-8') as f:

                json.dump(key, f, indent=4)

                await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated Guest Role To {role.mention}", color=0x2f3136))
    
    
    @_setup.command(name="staff", description="set staff role",aliases=["official","team","stf"])
    @ignore_check()

    @commands.has_permissions(manage_roles=True)
    @commands.cooldown(1, 3, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @blacklist_check()

    async def setupofficial(self,ctx, role:discord.Role=None):

        if role.permissions.administrator or role.permissions.ban_members or role.permissions.kick_members or role.permissions.manage_channels or role.permissions.mention_everyone or role.permissions.manage_roles:

            await ctx.reply(embed=discord.Embed(title="you can't use role with dangerous perms",color=0x2f3136))

            return

     

      

    

        if role.position >= ctx.author.top_role.position:

              await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))

        else:

                          

            with open('official.json', 'r', encoding='utf-8') as f:

                key = json.load(f)

                key[str(ctx.guild.id)] = [str(role.id)]

            with open('official.json', 'w', encoding='utf-8') as f:

                json.dump(key, f, indent=4)

                await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated official Role To {role.mention}", color=0x2f3136))   
    
    @_setup.command(name="girls",aliases=["qt","hawties"])
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)

    @blacklist_check()

    async def setupgirl(self,ctx, role:discord.Role=None):

        if role.permissions.administrator or role.permissions.ban_members or role.permissions.kick_members or role.permissions.manage_channels or role.permissions.mention_everyone or role.permissions.manage_roles:

            await ctx.reply(embed=discord.Embed(title="you can't use role with dangerous perms",color=0x2f3136))

            return

     

        if role.position >= ctx.author.top_role.position:

              await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))

        else:

            with open('girl.json', 'r', encoding='utf-8') as f:

                key = json.load(f)

                key[str(ctx.guild.id)] = [str(role.id)]

            with open('girl.json', 'w', encoding='utf-8') as f:

                json.dump(key, f, indent=4)

                await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated girls Role To {role.mention}", color=0x2f3136))
    
    @_setup.command(name="vips",aliases=["vp","viip"], description="set vip role")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @ignore_check()

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)

    @blacklist_check()

    async def setupvip(self,ctx, role:discord.Role=None):

        if role.permissions.administrator or role.permissions.ban_members or role.permissions.kick_members or role.permissions.manage_channels or role.permissions.mention_everyone or role.permissions.manage_roles:

            await ctx.reply(embed=discord.Embed(title="you can't use role with dangerous perms",color=0x2f3136))

            return

    

        if role.position >= ctx.author.top_role.position:

              await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))

        else:

            with open('vip.json', 'r', encoding='utf-8') as f:

                key = json.load(f)

                key[str(ctx.guild.id)] = [str(role.id)]

            with open('vip.json', 'w', encoding='utf-8') as f:

                json.dump(key, f, indent=4)

                await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated vip Role To {role.mention}", color=0x2f3136))
    
    @_setup.command(name="bot",aliases=['bt'], description="set bots role")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @ignore_check()

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(administrator=True)

    async def setupbot(self,ctx, role:discord.Role=None):

        if role.permissions.administrator or role.permissions.ban_members or role.permissions.kick_members or role.permissions.manage_channels or role.permissions.mention_everyone or role.permissions.manage_roles:

            await ctx.reply(embed=discord.Embed(title="you can't use role with dangerous perms",color=0x2f3136))

            return

        if role.position >= ctx.author.top_role.position:

              await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))

        else:

            with open('bot.json', 'r', encoding='utf-8') as f:

                key = json.load(f)

                key[str(ctx.guild.id)] = [str(role.id)]

            with open('bot.json', 'w', encoding='utf-8') as f:

                json.dump(key, f, indent=4)

                await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated bot Role To {role.mention}", color=0x2f3136))
  
    @_setup.command(name="modss",aliases=['moderate','moderator'], description="set mods role")
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)

    async def setupmod(self,ctx, role:discord.Role=None):

        if role.permissions.administrator or role.permissions.ban_members or role.permissions.kick_members or role.permissions.manage_channels or role.permissions.mention_everyone or role.permissions.manage_roles:

            await ctx.reply(embed=discord.Embed(title="you can't use role with dangerous perms",color=0x2f3136))

            return

        if role.position >= ctx.author.top_role.position:

              await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))

        else:

            with open('mod.json', 'r', encoding='utf-8') as f:

                key = json.load(f)

                key[str(ctx.guild.id)] = [str(role.id)]

            with open('mod.json', 'w', encoding='utf-8') as f:

                json.dump(key, f, indent=4)

                await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated mod Role To {role.mention}", color=0x2f3136)) 

    @_setup.command(name="artists",aliases=['art','arts'])

    @commands.has_permissions(manage_roles=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    @ignore_check()

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @blacklist_check()

    async def setupartist(self,ctx, role:discord.Role=None):

        if role.permissions.administrator or role.permissions.ban_members or role.permissions.kick_members or role.permissions.manage_channels or role.permissions.mention_everyone or role.permissions.manage_roles:

            await ctx.reply(embed=discord.Embed(title="you can't use role with dangerous perms",color=0x2f3136))

            return

     

        if role.position >= ctx.author.top_role.position:

              await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))

        else:

            with open('artist.json', 'r', encoding='utf-8') as f:

                key = json.load(f)

                key[str(ctx.guild.id)] = [str(role.id)]

            with open('artist.json', 'w', encoding='utf-8') as f:

                json.dump(key, f, indent=4)

                await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated Artist Role To {role.mention}", color=000000))

    @_setup.command(name="reqrole",aliases=['reqr','rqr'])
    @ignore_check()
    @commands.cooldown(1, 3, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)

    @blacklist_check()

    async def setupreqrole(self,ctx, role:discord.Role=None):

        if role.permissions.administrator or role.permissions.ban_members or role.permissions.kick_members or role.permissions.manage_channels or role.permissions.mention_everyone or role.permissions.manage_roles:

            await ctx.reply(embed=discord.Embed(title="you can't use role with dangerous perms",color=0x2f3136))

            return

        if role.position >= ctx.author.top_role.position:

              await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))

        else:

            with open('reqrole.json', 'r', encoding='utf-8') as f:

                key = json.load(f)

                key[str(ctx.guild.id)] = [str(role.id)]

            with open('reqrole.json', 'w', encoding='utf-8') as f:

                json.dump(key, f, indent=4)
                await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated req Role To {role.mention}", color=0x2f3136))

       
         

         

        

        
          

             

     

          

               

             

        

              
        @commands.Cog.listener()

        async def on_message(self,message):  

            async with self.bot.db.cursor() as cursor:

                    await cursor.execute("SELECT role, trigger FROM customrole WHERE guild = ?", (message.guild.id,))

                    data = await cursor.fetchall()

                      

                    if data:

                        for table in data:

                            trigger = table[1]

                            role = table[0]

                            if message.author.bot:

                                pass

                            else:

                                try:

                                   if trigger.lower() in  message.content.split()[0].lower():

                                     mem = message.mentions

                  

                                     op = mem[0].id

                                     member = message.guild.get_member(int(op))

                                     with open("reqrole.json", "r") as f:

                                       op = json.load(f)

                                       if f'{message.guild.id}' not in op:

                                         return await message.channel.send(embed=discord.Embed(description="<:cross1:1110685242278297600> | There is no **Required Role** for **Custom Roles** Use **setup reqrole**",color=0x2f3136))

                                       elif f'{message.guild.id}' in op:

                                         for S in op[str(message.guild.id)]:

                                           rr = discord.utils.get(message.guild.roles,id=int(S))

                                           if rr not in message.author.roles:

                                             await message.channel.send(embed=discord.Embed(description=f"<:cross1:1110685242278297600> | You must have {rr.mention} to add roles to people", color=0x2f3136))

                                             return

                                     P = discord.utils.get(message.guild.roles,id=int(role))

                                     if P in member.roles:

                                       await member.remove_roles(P)

                                       embed=discord.Embed(description=f"<:ri8:1038487759750438912> Successfully removed {P.mention} From {member.mention}",color=0x2f3136)

                                       embed.set_author(name=message.author,icon_url=message.author.display_avatar)

                                       embed.set_thumbnail(url=message.author.display_avatar)

                                       await message.channel.send(embed=embed)

                                     else:

                                       if P not in member.roles:

                                         await member.add_roles(P)

                                         embed=discord.Embed(description=f"<:ri8:1038487759750438912> Successfully Given {P.mention} To {member.mention}",color=0x2f3136)

                                         embed.set_author(name=message.author,icon_url=message.author.display_avatar)

                                         embed.set_thumbnail(url=message.author.display_avatar)

                                         await message.channel.send(embed=embed)

                                       

                                    

                                except discord.HTTPException:

                                 pass

                                 await self.bot.process_commands(message)              

                
    
    

    

        

                    
        
        

                    

                    

           #         mem = message.mentions

                  

           #         op = mem[0].id

         #           member = message.guild.get_member(int(op))

        #            if member not in message.content.lower():

        #              return await message.channel.send("loas")

                    

                    

                    
     #   @commands.Cog.listener()
    #    async def on_message(self,message):
      #      async with self.bot.db.cursor() as cursor:
      #          await cursor.execute("SELECT role, trigger FROM customrole WHERE guild = ?", (message.guild.id,))
     #           data = await cursor.fetchall()
      #          if data:
      #              for table in data:
        #                trigger = table[1]
        #                role = table[0]
        #                if message.author.bot:
        #                pass
         #           else:
        #                if trigger.lower() in  message.content.split()[0].lower():
      #                      mem = message.mentions
        #                    op = mem[0].id

        #                    member = message.guild.get_member(int(op))
     #                       with open("reqrole.json", "r") as f:
    #                            ok = json.load(f)
     #                           if f'{message.guild.id}' not in ok:
    #                                return await message.channel.send(embed=discord.Embed(description="<:cross1:1110685242278297600> | There is no **Required Role** for **Custom Roles** Use **setup reqrole**",color=0x2f3136))
     #                           elif f'{message.guild.id}' in ok:
                               #     for S in ok[str(message.guild.id)]:
                              #          rr = discord.utils.get(message.guild.roles,id=int(S))
                                  #      if rr not in message.author.roles:
                               #             return await message.channel.send(embed=discord.Embed(description=f"<:cross1:1110685242278297600> | You must have {rr.mention} to add roles to people", color=0x2f3136))
                                #        P = discord.utils.get(message.guild.roles,id=int(role))
                             #           if P in member.roles:
                                   #         await member.remove_roles(P)
                               #             embed=discord.Embed(description=f"<:ri8:1038487759750438912> Successfully removed {P.mention} From {member.mention}",color=0x2f3136)
                                 #           embed.set_author(name=message.author,icon_url=message.author.display_avatar)
                            #                embed.set_thumbnail(url=message.author.display_avatar)
                                 #           await message.channel.send(embed=embed)
                             #           else:
                                                #
                              #                  if P not in member.roles:
                           #                         await member.add_roles(P)
                         #                           embed=discord.Embed(description=f"<:ri8:1038487759750438912> Successfully Given {P.mention} To {member.mention}",color=0x2f3136)
                                                   # embed.set_author(name=message.author,icon_url=message.author.display_avatar)
                               #                     embed.set_thumbnail(url=message.author.display_avatar)
                         #                           await message.channel.send(embed=embed)
                              #                      await self.bot.process_commands(message)
                                                        
                    

                        

                            

                            

                            

                                

                            

                               

                                   
                                    
                                    

                                     

                                     

                               

                                  

                                   

                                       

                                       

                                         

                                       

                                         

                                           

                                           

                                             

                                             

                                   

                                   

                                     

                                     

                                     

                                     

                                    

                                

                                       

                                        

                                         

                                         

                                         

                                         

               #                        else:

    #                                     await message.channel.send("hmm")

         #                       except discord.HTTPException:

           #                      pass

                                 

      

                    

                    

                    

 

async def setup(bot):

    await bot.add_cog(customrole(bot))