import discord
from discord.utils import *
import aiohttp
from core import Cog
import json
from prince1.Tools import *
from discord.ext import commands
import asyncio


headers = {'Authorization': 'Bot MTAxMzc3MTQ5NzE1Nzk3MjAwOA.GLxRdo.nqKSG8BrsbgiW7y8esxzGWeivkD6gddY4D7OzA'}

class autorole(Cog):
    def __init__(self, bot):
        self.bot = bot



    @Cog.listener()
    async def on_member_join(self, member):
        data = getVC(member.guild.id)
        arb = data["autorole"]["bots"]
        arh = data["autorole"]["humans"]
        if arb == []:
            return
        else:
            if member.bot != True:
                return
            elif member.bot:
                async with aiohttp.ClientSession(headers=headers, connector=None) as session:
                    for role in arb:
                        try:
                            await asyncio.sleep(2)
                            async with session.put(f"https://discord.com/api/v10/guilds/{member.guild.id}/members/{member.id}/roles/{int(role)}", json={'reason': "Soward Prime | Auto Role"}) as req:
                                print(req.status)
                        except:
                            pass



    @Cog.listener()
    async def on_member_join(self, member):
        data = getVC(member.guild.id)
        arb = data["autorole"]["bots"]
        arh = data["autorole"]["humans"]
        if arh == []:
            return
        else:
            if member.bot:
                return
            elif member.bot != True:
                async with aiohttp.ClientSession(headers=headers, connector=None) as session:
                    for role in arh:
                        try:
                            async with session.put(f"https://discord.com/api/v10/guilds/{member.guild.id}/members/{member.id}/roles/{int(role)}", json={'reason': "Soward Prime | Auto Role"}) as req:
                                print(req.status)
                        except:
                            pass
async def setup(bot):
  await bot.add_cog(autorole(bot))