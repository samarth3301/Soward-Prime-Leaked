import discord
import logging
from discord.ext import commands
import motor.motor_asyncio as mongodb
#from .ticket import createTicket, closeTicket
import json
#from ._verification import verificationb
from prince1.Tools import*
class ready(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.color = 0x2f3136




    @commands.Cog.listener()
    async def on_shard_ready(self, shard_id):
        logging.info("Shard #%s is ready" % (shard_id))

    @commands.Cog.listener()
    async def on_shard_connect(self, shard_id):
        logging.info("Shard #%s has connected" % (shard_id))

    @commands.Cog.listener()
    async def on_shard_disconnect(self, shard_id):
        logging.info("Shard #%s has disconnected" % (shard_id))

    @commands.Cog.listener()
    async def on_shard_resume(self, shard_id):
        logging.info("Shard #%s has resumed" % (shard_id))

   # @commands.Cog.listener()
  #  async def on_guild_join(self, guild): #when the bot joins the guild
    #        with open('prefixes.json', 'r') as f: #read the prefix.json file
     #               prefixes = json.load(f) #load the json file
   #                 prefixes[str(guild.id)] = '?'#default prefix
 #                   with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
  #                          json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater

 #   @commands.Cog.listener()
 #   async def on_guild_remove(self,guild): #when the bot is removed from the guild
   #         with open('prefixes.json', 'r') as f: #read the file
    #                prefixes = json.load(f)
   #                 prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from
   #                 with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
   #                         json.dump(prefixes, f, indent=4)

async def setup(client):
    await client.add_cog(ready(client))