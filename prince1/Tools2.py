import json, sys, os

from discord.ext import commands

from core import Context

import aiohttp

#import DotEnv



 



def updateDB(guildID, data):

    with open("welcome.json", "r") as config:

        config = json.load(config)

    config["guilds"][str(guildID)] = data

    newdata = json.dumps(config, indent=4, ensure_ascii=False)

    with open("welcome.json", "w") as config:

        config.write(newdata)

def getDB(guildID):

    with open("welcome.json", "r") as config:

        

        data = json.load(config)

    if str(guildID) not in data["guilds"]:

        defaultConfig = {

            "welcome": {

                "autodel": 0,

                "channel": [],

                "color": "",

                "embed": False,

                "footer": "",

                "image": "",

                "message": "{user.mention} Welcome To {server.name}",

                "ping": False,

                "title": "",

                "thumbnail": ""

            

			}

            

        }

        updateDB(guildID, defaultConfig)

        return defaultConfig

    return data["guilds"][str(guildID)]
















    

     

    

     

         

      

      

     

    



    

        

   

    

    

      

