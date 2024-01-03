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
from prince1.Tools import *
MONGO_URL = "mongodb+srv://SowardPrime:nxtontop@cluster0.8br1ugl.mongodb.net/?retryWrites=true&w=majority"



class EventHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    
            
        
    @commands.Cog.listener() 
    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.client.user:
                return
        try:
            
            if message is not None:
                with open("reaction.json", "r") as f:
                    rxn = json.load(f)
                if str(message.guild.id) not in rxn:
                    return
                else:
                    ans = rxn[str(message.guild.id)][message.content.lower()]
                    
                    
                    return await message.add_reaction(ans)
        except:
            pass

    



  



        
async def setup(client):
    await client.add_cog(EventHandler(client))
