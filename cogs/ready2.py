import discord
import logging
from discord.ext import commands
import motor.motor_asyncio as mongodb

class ready5(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.color = 0x2f3136
        self.connection = mongodb.AsyncIOMotorClient("mongodb+srv://Sowardprime:nxtontop@cluster0.aoy4vww.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.connection["serverss"]["data"]
    @commands.Cog.listener()

    async def on_ready(self):

        for server in self.client.guilds:

            data = await self.db.find_one({"guild": server.id})

            if data == None:

                await self.db.insert_one(

                    {

                        "guild": server.id,

                        "log-channel": None,

                        "delete-after" : None,

                        "joinvc": {

                            "channelid": None,

                            "enabled": False

                        },

                        "vcrole": {

                            "roleid": None,

                            "enabled": False

                        },

                        "autorole": [],

                        "humans": [],

                        "bots": [],

                        "welcome": {

                            "message": None,

                            "channel": None,

                            "enabled": False,

                            "embed": False,

                            "title": None,

                            "description": None,

                            "thumbnail": None,

                            "image": None

                        }

                    }

                )

    @commands.Cog.listener()

    async def on_guild_join(self, guild):

        await self.db.insert_one(

            {

                "guild": guild.id,

                "log-channel": None, 

                "delete-after" : None,

                "joinvc": {

                    "channelid": None,

                    "enabled": False

                },

                "vcrole": {

                    "roleid": None,

                    "enabled": False

                },

                "autorole": [],

                "humans": [],

                "bots": [],

                "welcome": {

                    "message": None,

                    "channel": None,

                    "enabled": False,

                    "embed": False,

                    "title": None,

                    "description": None,

                    "thumbnail": None,

                    "image": None

                }

            }

        )

          

    
        

    

async def setup(client):
    await client.add_cog(ready5(client))