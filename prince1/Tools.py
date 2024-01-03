import json, sys, os

from discord.ext import commands

from core import Context

import aiohttp

#import DotEnv

class NotVoter(commands.CheckFailure):

  pass

def DotEnv(query: str):

  return os.getenv(query)

        

def add_user_to_blacklist(user_id: int) -> None:

    with open("blacklist.json", "r") as file:

        file_data = json.load(file)

        if str(user_id) in file_data["ids"]:

            return

        file_data["ids"].append(str(user_id))

    with open("blacklist.json", "w") as file:

        json.dump(file_data, file, indent=4)

def remove_user_from_blacklist(user_id: int) -> None:

    with open("blacklist.json", "r") as file:

        file_data = json.load(file)

        file_data["ids"].remove(str(user_id))

    with open("blacklist.json", "w") as file:

        json.dump(file_data, file, indent=4)

def blacklist_check():

    def predicate(ctx):

        with open("blacklist.json") as f:

            data = json.load(f)

            if str(ctx.author.id) in data["ids"]:

                return False

            return True

    return commands.check(predicate)

def check_if_message_is_reply(ctx):

    result = ctx.message.reference

    if result is None:

        return 0

    else:

        return 1

def getConfig(guildID):

    with open("test.json", "r") as config:

        data = json.load(config)

    if str(guildID) not in data["guilds"]:

        defaultConfig = {

            "whitelisted": [],
            "punishment": "ban",
            "extraowner": []

        }

        updateConfig(guildID, defaultConfig)

        return defaultConfig

    return data["guilds"][str(guildID)]

def updateConfig(guildID, data):

    with open("test.json", "r") as config:

        config = json.load(config)

    config["guilds"][str(guildID)] = data

    newdata = json.dumps(config, indent=4, ensure_ascii=False)

    with open("test.json", "w") as config:

        config.write(newdata)

def getanti(guildid):

    with open("anti.json", "r") as config:

        data = json.load(config)

    if str(guildid) not in data["guilds"]:

        default = "off"

        updateanti(guildid, default)

        return default

    return data["guilds"][str(guildid)]

def updateanti(guildid, data):

    with open("anti.json", "r") as config:

        config = json.load(config)

    config["guilds"][str(guildid)] = data

    newdata = json.dumps(config, indent=4, ensure_ascii=False)

    with open("anti.json", "w") as config:

        config.write(newdata)

async def check_voter(mem):

  async with aiohttp.ClientSession(headers={"Authorization": DotEnv("top-gg")}) as session:

    async with session.get(f"https://top.gg/api/bots/1013771497157972008/vote/check?userId={str(mem)}") as response:

      vote = await response.json()

      if vote["voted"] == 1 or mem in [743431588599038003, 905396101274828821]:

        response.close()

        return "okay"

      else:

        response.close()

        return "not okay"

def is_voter():

  async def predicate(ctx: Context):

    async with aiohttp.ClientSession(headers={"Authorization": DotEnv("top-gg")}) as session:

      async with session.get(f"https://top.gg/api/bots/1013771497157972008/vote/check?userId={str(ctx.author.id)}") as response:

        vote = await response.json()

        if vote["voted"] == 1 or ctx.author.id in ctx.bot.owner_ids:

          response.close()

          return True

        else:

          response.close()

          raise NotVoter()

  return commands.check(predicate)


def getAfk(memID):

    with open("afk.json", "r") as config:

        data = json.load(config)

    if str(memID) not in data["mem"]:

      defaultConfig = {

            "status": False,

            "reason": "",

            "time": "",

      }

      updateAfk(memID, defaultConfig)

      return defaultConfig

    return data["mem"][str(memID)]

def updateAfk(memID, data):

    with open("afk.json", "r") as config:

        config = json.load(config)

    config["mem"][str(memID)] = data

    newdata = json.dumps(config, indent=4, ensure_ascii=False)

    with open("afk.json", "w") as config:

       config.write(newdata)
    
def getboost(guildid):

    with open("boost.json", "r") as config:

        data = json.load(config)

    if str(guildid) not in data["guilds"]:

        default = "off"

        updateboost(guildid, default)

        return default

    return data["guilds"][str(guildid)]

def updateboost(guildid, data):

    with open("boost.json", "r") as config:

        config = json.load(config)

    config["guilds"][str(guildid)] = data

    newdata = json.dumps(config, indent=4, ensure_ascii=False)

    with open("boost.json", "w") as config:

        config.write(newdata)
        
def updateVC(guildID, data):

    with open("vc.json", "r") as config:

        config = json.load(config)

    config["guilds"][str(guildID)] = data

    newdata = json.dumps(config, indent=4, ensure_ascii=False)

    with open("vc.json", "w") as config:

        config.write(newdata)

def getVC(guildID):

    with open("vc.json", "r") as config:

        data = json.load(config)

    if str(guildID) not in data["guilds"]:

        defaultConfig = {

          

            "autorole": {

                "bots": [],

                "humans": []

            },

            "vcrole": {

                "bots": "",

                "humans": ""

            

            

            }

        }

        updateVC(guildID, defaultConfig)

        return defaultConfig

    return data["guilds"][str(guildID)]


        

    
def add_channel_to_ignore(user_id: int) -> None:

  with open("ignore.json", "r") as file:

    file_data = json.load(file)

    if str(user_id) in file_data["ids"]:

      return

    file_data["ids"].append(str(user_id))

  with open("ignore.json", "w") as file:

    json.dump(file_data, file, indent=4)

def remove_channel_from_ignore(user_id: int) -> None:

  with open("ignore.json", "r") as file:

    file_data = json.load(file)

    file_data["ids"].remove(str(user_id))

  with open("ignore.json", "w") as file:

    json.dump(file_data, file, indent=4)

def ignore_check():

  def predicate(ctx):

    with open("ignore.json") as f:

      data = json.load(f)

      if str(ctx.channel.id) in data["ids"]:

        return False

      return True

  return commands.check(predicate)
        

            

            

              

                

                

               

                

                

                

                

               

            

			

            

        

        

        

    

        
