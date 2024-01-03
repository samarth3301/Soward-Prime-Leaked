# This example requires the 'message_content' privileged intents

import os

import discord

from discord.ext import commands

#from prince import *

import asyncio

import os

#os.system("pip install -r requirements.txt")

import sqlite3

import traceback

from contextlib import closing

import discord

import random

from discord.ext import commands

from discord.ext.commands import Context

import ast

import inspect

import re

#from helpers import checks

import aiosqlite

import psutil

from discord.ui import Button,View

from prince.bot import Bot

import json

from discord.utils import get

from prince1.Tools import *

import logging 

from cogs._j2c import vmbuttons

bot = Bot()

#logging.basicConfig(filename='error.log', level=

def read_json():

    with open(f"database.json", "r") as file:

        data = json.load(file)

    return data

def write_json(data):

    with open(f"database.json", "w") as file:

        json.dump(data, file, indent=4)

        file.close()

@bot.event

    

async def on_connect():

    try:

        setattr(bot, "db", await aiosqlite.connect("main.db"))

        async with bot.db.cursor() as cursor:

            await cursor.execute("CREATE TABLE IF NOT EXISTS customrole (trigger TEXT, role INTEGER, guild INTEGER)")

            await cursor.execute("CREATE TABLE IF NOT EXISTS voicemaster (guild_id INTEGER, vc INTEGER, interface INTEGER)")

            await cursor.execute("CREATE TABLE IF NOT EXISTS vcs (user_id INTEGER, voice INTEGER)")

            await bot.db.commit()

            print('connected to database')

            await bot.add_view(vmbuttons())

    except:

        pass

    

        

        

            

            

            

            

            

            

            

            

            

            

            

            

            

            

            

            

            

            

            

            

        

        

        

        

        

        

            

            

           

            

    

         

database = {}

database.update(read_json())

welcm = database["welcm"]

vcids = database["vcids"]

@bot.command(aliases=["greet"])

@commands.has_permissions(manage_channels=True)

async def set_greet(ctx,*,msg=None):

	if msg == None:

		await ctx.send("pls provide msg !!", delete_after=4)

		return

	if not "$$MM$$" in msg:

		await ctx.reply(f"**use member mention \n example:** \n `set_welcome heyy!! $$MM$$ welcome to {ctx.guild.name} server !!`  ")

	else:

		try:

			

			if not str(ctx.guild.id) in welcm.keys():

				welcm.update({f"{ctx.guild.id}":{f"{ctx.channel.id}":f"{msg}"}})

			db = welcm[str(ctx.guild.id)]

			wlcm = ({f"{ctx.channel.id}":f"{msg}"})

			

			db.update(wlcm)

			write_json(database)

			await ctx.send("successful set welcome msg !!", delete_after=4)

			await ctx.message.delete()

		except:

			pass

@bot.command(aliases=["stopgreet"])

@commands.has_permissions(manage_channels=True)

async def stop_greet(ctx):

	if not str(ctx.guild.id) in welcm.keys():

		await ctx.send("in this server not set welcome message !!")

		return

	elif not str(ctx.channel.id) in welcm[str(ctx.guild.id)].keys():

		await ctx.send("welcome message not set in this channel.")

		return

	else:

		try:

			

			db = welcm[str(ctx.guild.id)]

			db.pop(f"{ctx.channel.id}")

			write_json(database)

			await ctx.send("stop welcome message in this channel. ")

			await ctx.message.delete()

		except:

			pass

@bot.event

async def on_member_join(member):

	if str(member.guild.id) in welcm.keys():

		for x in welcm[str(member.guild.id)].keys():

			ch = member.guild.get_channel(int(x))

			msg = welcm[str(member.guild.id)][x]

			m = msg.replace("$$MM$$", f"{member.mention}")

			try:

				await ch.send(m , delete_after=10)

			except:

				pass
owners = [1068967045263261746,984815117730480228,1090957904410071120]
       
@bot.command(aliases=["prm"])

#@commands.is_owner()

async def premium(ctx, type=None, id:int=None):

  if ctx.author.id not in owners:

    

    return

  else:

    if type == None:

      await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | You missed the 'Type' argument", color=0x2f3136),mention_author=False)

      return

    if type == "add":

      if id == None:

        await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | You missed the 'guild_id' argument", color=0x2f3136),mention_author=False)

        return

      else:

        with open ("premium.json","r") as f:

          id = bot.get_guild(id)

          member = json.load(f)

          if str(id.id) in member["guild"]:

            await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | premium already activated in this guild!", color=0x2f3136),mention_author=False)

            return

          else:

            member["guild"].append(str(id.id))

            with open ("premium.json","w") as f:

              json.dump(member,f)

            await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> |  successfully activated premium in {id.name}  !", color=0x2f3136),mention_author=False)

    if type == "remove":

      if id == None:

        await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | You missed the 'guild_id' argument", color=0x2f3136),mention_author=False)

        return

      else:

        with open ("premium.json","r") as f:

          member = json.load(f)
          guild = bot.get_guild(id)
          if str(guild.id) not in member["guild"]:

            await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | this server has no subscribe yet !", color=0x2f3136),mention_author=False)

            return

          else:

            member["guild"].remove(str(guild.id))

            with open ("premium.json","w") as f:

              json.dump(member,f)

            await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> | {guild.name} is successfully removed from premium!", color=0x2f3136),mention_author=False) 

            
            
@commands.cooldown(1, 30, commands.BucketType.user)

@commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

@bot.command()

@blacklist_check()

@commands.guild_only()

@commands.has_permissions(ban_members=True)

async def unbanall(ctx):

      button = Button(label="Yes", style=discord.ButtonStyle.green, emoji="<:Icons_correct:1017402689027592222>")

      button1 = Button(label="No", style=discord.ButtonStyle.red, emoji="<:Wrong:1017402708703064144>")

      async def button_callback(interaction: discord.Interaction):

        a = 0

        if interaction.user == ctx.author:

          if interaction.guild.me.guild_permissions.ban_members:

            await interaction.response.edit_message(content=f"Unbanning All Banned Member(s)", embed=None, view=None)

            async for idk in interaction.guild.bans(limit=None):

              await interaction.guild.unban(user=idk.user, reason="Unbanall Command Executed By: {}".format(ctx.author))

              a += 1

            

            await interaction.channel.send(content=f"<:Icons_correct:1017402689027592222> | Successfully Unbanned {a} Member(s)")

          else:

            await interaction.response.edit_message(content="I am missing ban members permission.\ntry giving me permissions and retry", embed=None, view=None)

        else:

          await interaction.response.send_message("This is not for you ", embed=None, view=None, ephemeral=True)

      async def button1_callback(interaction: discord.Interaction):

        if interaction.user == ctx.author:

          await interaction.response.edit_message(content="Ok I will not unban anyone in this guild", embed=None, view=None)

        else:

          await interaction.response.send_message("This is not for you ", embed=None, view=None, ephemeral=True)

   # if ctx.guild.me.guild_permissions.ban_members:

      embed = discord.Embed(title='Confirmation',

                          color=0x2f3136,

                          description=f'**Are you sure you want to unban everyone in this guild?**')

      view = View()

      button.callback = button_callback

      button1.callback = button1_callback

      view.add_item(button)

      view.add_item(button1)

      await ctx.reply(embed=embed, view=view, mention_author=False)        

        

        

        

@bot.command()

@blacklist_check()

async def roleinfo(ctx, role: discord.Role = None):

  riembed = discord.Embed(title=f"**{role.name}'s Information**", colour=discord.Colour(0x2f3136))

  perms = ""

  if role.permissions.administrator:

            perms += "Administrator, "

  if role.permissions.create_instant_invite:

            perms += "Create Instant Invite, "

  if role.permissions.kick_members:

            perms += "Kick Members, "

  if role.permissions.ban_members:

            perms += "Ban Members, "

  if role.permissions.manage_channels:

            perms += "Manage Channels, "

  if role.permissions.manage_guild:

            perms += "Manage Guild, "

  if role.permissions.add_reactions:

            perms += "Add Reactions, "

  if role.permissions.view_audit_log:

            perms += "View Audit Log, "

  if role.permissions.read_messages:

            perms += "Read Messages, "

  if role.permissions.send_messages:

            perms += "Send Messages, "

  if role.permissions.send_tts_messages:

            perms += "Send TTS Messages, "

  if role.permissions.manage_messages:

            perms += "Manage Messages, "

  if role.permissions.embed_links:

            perms += "Embed Links, "

  if role.permissions.attach_files:

            perms += "Attach Files, "

  if role.permissions.read_message_history:

            perms += "Read Message History, "

  if role.permissions.mention_everyone:

            perms += "Mention Everyone, "

  if role.permissions.external_emojis:

            perms += "Use External Emojis, "

  if role.permissions.connect:

            perms += "Connect to Voice, "

  if role.permissions.speak:

            perms += "Speak, "

  if role.permissions.mute_members:

            perms += "Mute Members, "

  if role.permissions.deafen_members:

            perms += "Deafen Members, "

  if role.permissions.move_members:

            perms += "Move Members, "

  if role.permissions.use_voice_activation:

            perms += "Use Voice Activation, "

  if role.permissions.change_nickname:

            perms += "Change Nickname, "

  if role.permissions.manage_nicknames:

            perms += "Manage Nicknames, "

  if role.permissions.manage_roles:

            perms += "Manage Roles, "

  if role.permissions.manage_webhooks:

            perms += "Manage Webhooks, "

  if role.permissions.manage_emojis:

            perms += "Manage Emojis, "

  if perms is None:

            perms = "None"

  else:

            perms = perms.strip(", ")

          

  riembed.add_field(name='__General info__', value=f"Name: {role.name}\nId: {role.id}\nPosition: {role.position}\nHex: {role.color}\nMentionable: {role.mentionable}\nCreated At: {role.created_at}\nManaged by Integration: {(role.managed)}\n\nmembers in this role: {(len(role.members))}\n\nPermissions: {perms}")

  await ctx.reply(embed=riembed)

async def load_cogs() -> None:  

        await bot.load_extension("jishaku")

        for file in os.listdir("./cogs"):

          if file.endswith(".py"):

            extension = file[:-3]

            try:

                await bot.load_extension(f"cogs.{extension}")

                

               # print(f"Loaded extension '{extension}'")

            except Exception as e:

                tb = traceback.format_exception(type(e), e, e.__traceback__)

                tbe = "".join(tb) + ""

                print(tbe)

#def init_db():

   # with closing(connect_db()) as db:

   #     with open("database/schema.sql", "r") as f:

  #          db.cursor().executescript(f.read())

    #    db.commit()

def source(o):

    s = inspect.getsource(o).split("\n")

    indent = len(s[0]) - len(s[0].lstrip())

    return "\n".join(i[indent:] for i in s)

source_ = source(discord.gateway.DiscordWebSocket.identify)

patched = re.sub(

    r'([\'"]\$browser[\'"]:\s?[\'"]).+([\'"])', 

    r"\1Discord Android\2",  

    source_

)

loc = {}

exec(compile(ast.parse(patched), "<string>", "exec"), discord.gateway.__dict__, loc)

discord.gateway.DiscordWebSocket.identify = loc["identify"]

#def connect_db():

  #  return sqlite3.connect("database/database.db")

#bot.db = connect_db()

if __name__ == '__main__':

 #   init_db()

    asyncio.run(load_cogs())

    bot.run()

    

    

   

    
