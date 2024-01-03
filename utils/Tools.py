import json, sys, os
import discord
from discord.ext import commands
from core import Context
import aiohttp
from discord.ui import Select, View, Button
import time

from typing import Any






def DotEnv(query: str):
    return os.getenv(query)








def getpre(guildID):
    with open("prefixes.json", "r") as config:
        data = json.load(config)
    if str(guildID) not in data["guilds"]:
        defaultS = {
           
            "prefix": "?"
          
            
        }
        updatepre(guildID, defaultS)
        return defaultS
    return data["guilds"][str(guildID)]


def updatepre(guildID, data):
    with open("prefixes.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildID)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("prefixes.json", "w") as config:
        config.write(newdata)






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


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)















    









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
