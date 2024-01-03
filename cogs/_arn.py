import os

import re

import ast

import json

import random

import urllib

import discord

import inspect

import base64

import asyncio

import aiohttp

import datetime

import requests

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
from prince1.Tools import *
from discord.utils import get

class customrole2(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.Cog.listener()

    async def on_ready(self):

        setattr(self.bot, "db", await aiosqlite.connect("main.db"))

        async with self.bot.db.cursor() as cursor:

            await cursor.execute("CREATE TABLE IF NOT EXISTS customrole (trigger TEXT, role INTEGER, guild INTEGER)")

        await self.bot.db.commit()

    

    

      

        

               

            

        

        

      

    

    

    

    

    

           

    @commands.Cog.listener()

    async def on_message(self,message):  

        async with self.bot.db.cursor() as cursor:
                    await cursor.execute("CREATE TABLE IF NOT EXISTS customrole (trigger TEXT, role INTEGER, guild INTEGER)")

        

                    await cursor.execute("SELECT role, trigger FROM customrole WHERE guild = ?", (message.guild.id,))
             #       print(message.guild.id)

                    data = await cursor.fetchall()
                    if isinstance(message.channel, discord.DMChannel) and str(message.author) ==  'user': return 

        

                      

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

                                         return await message.channel.send(embed=discord.Embed(description="<:cross1:1110685242278297600> | There is no **Required Role** for **Custom Roles** Use **setup reqrole**",color=0x2f3136),delete_after=5)

                                       elif f'{message.guild.id}' in op:

                                         for S in op[str(message.guild.id)]:

                                           rr = discord.utils.get(message.guild.roles,id=int(S))

                                           if rr not in message.author.roles:

                                             await message.channel.send(embed=discord.Embed(description=f"<:cross1:1110685242278297600> | You must have {rr.mention} to add roles to people", color=0x2f3136),delete_after=5)

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

                                       

                                    

                                except:
                                    pass
                              #  await self.bot.process_commands(message)



                                    

                                    

      

                    

                    

                    

 

async def setup(bot):

    await bot.add_cog(customrole2(bot))