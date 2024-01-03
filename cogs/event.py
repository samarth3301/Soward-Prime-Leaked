import json
import os
import discord
from discord.ext import commands
import json
from prince.bot import Bot
import motor.motor_asyncio as motor
#os.system("pip install httpx")
#os.system("pip install aiohttp")
import aiohttp
import re
import discord
import aiohttp
import sys
import jishaku
import traceback
from discord.ext import commands, tasks
from pymongo import UpdateOne
from prince.embed import success_embed
from prince.ui import DropDownSelfRoleView, ButtonSelfRoleView
import time
from discord.utils import get

MONGO_URL = "mongodb+srv://SowardPrime:nxtontop@cluster0.8br1ugl.mongodb.net/?retryWrites=true&w=majority"



class EventHandler2(commands.Cog):
    def __init__(self, client):
        self.client = client
  
        

         
    @commands.Cog.listener()
    async def on_command(self, ctx):
        channel = self.client.get_channel(1190577053569912862)

        embed = discord.Embed(
            title=f"Command Executed!",
            colour=0x2f3136, timestamp=ctx.message.created_at,
            description=f"**Command:** {ctx.command.name}"
            f"```{ctx.message.content}```\n"
    
            f"in {ctx.channel.mention} of \n"
            f"**{ctx.guild.name}** : {ctx.guild.id}")
        embed.set_author(name=f"{ctx.author} | {ctx.author.id}", icon_url=ctx.author.display_avatar)
        await channel.send(embed=embed)

    @commands.Cog.listener() 
    async def on_message(self, message: discord.Message) -> None:
        
        if message.author.bot:
          
            return
        if message.author == self.client.user:
                return
        try:
            if message is not None:
                with open("autoresponse.json", "r") as f:
                    autoresponse = json.load(f)
                if str(message.guild.id) in autoresponse:
                    ans = autoresponse[str(message.guild.id)][message.content.lower()]
                 
                    return await message.channel.send(ans)
        except:
            pass

    



  



        
async def setup(client):
    await client.add_cog(EventHandler2(client))
