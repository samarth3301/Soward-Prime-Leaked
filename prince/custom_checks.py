

import discord
from typing import Union
from discord.ext import commands
from config import TOP_GG_TOKEN, BOT_MOD_ROLE, SUPPORTER_ROLE, OWNERS, SOWARD_PREMIUM_ROLE

import aiohttp

from prince.classes import Profile


class NotVoted(commands.CheckFailure):
    pass


class NotBotMod(commands.CheckFailure):
    pass

class NotPremium(commands.CheckFailure):

	pass

class OptedOut(commands.CheckFailure):
    pass


class PrivateCommand(commands.CheckFailure):
    pass


class ComingSoon(commands.CheckFailure):
    pass


async def check_voter(user_id):
    async with aiohttp.ClientSession() as s:
        async with s.get(f'https://top.gg/api/bots/1013771497157972008/check?userId={user_id}', headers={'Authorization': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEwMTM3NzE0OTcxNTc5NzIwMDgiLCJib3QiOnRydWUsImlhdCI6MTY3ODI4NzY5OH0.CVQjrFrhE2BFTxd-i77fy7eye2lpt3NOdWqTYJGPMyQ"}) as r:
            pain = await r.json()
            if pain['voted'] == 1:
                return True
            else:
                return False


async def check_supporter(ctx):
    guild = ctx.bot.get_guild(EPICBOT_GUILD_ID)
    if guild not in ctx.author.mutual_guilds:
        return False
    member = guild.get_member(ctx.author.id)
    role = guild.get_role(SUPPORTER_ROLE)
    if not member:
        return False
    if role not in member.roles:
        return False
    return True


def voter_only():
    async def predicate(ctx):
        thing = await check_voter(ctx.author.id)
        if not thing:
            raise NotVoted('this command is confined only to my voters.\nPlease vote me [here](https://top.gg/bot/1013771497157972008/vote) to unlock command.')
        return True
    return commands.check(predicate)


def bot_mods_only():
    async def predicate(ctx: commands.Context):
        guild = ctx.bot.get_guild(EPICBOT_GUILD_ID)
        if guild not in ctx.author.mutual_guilds:
            raise NotBotMod('h')
        member = guild.get_member(ctx.author.id)
        role = guild.get_role(BOT_MOD_ROLE)
        if not member:
            raise NotBotMod('h')
        if role in member.roles:
            return True
        else:
            raise NotBotMod('h')
    return commands.check(predicate)


def not_opted_out():
    async def predicate(ctx: commands.Context):
        user_profile: Profile = await ctx.bot.get_user_profile_(ctx.author.id)
        if not user_profile.snipe:
            raise OptedOut('h')
        else:
            return True
    return commands.check(predicate)


def mutual_guild(guild_id: int):

    async def predicate(ctx: commands.Context):
        person: Union[discord.Member, discord.User] = ctx.author
        if guild_id not in [guild.id for guild in person.mutual_guilds]:
            raise PrivateCommand('h')
        return True

    return commands.check(predicate)

def premium_only():

    async def predicate(ctx: commands.Context):

        guild = ctx.bot.get_guild(EPICBOT_GUILD_ID)

        if guild not in ctx.author.mutual_guilds:

            raise NotPremium('this command only for premium user join support server and buy premium')

        member = guild.get_member(ctx.author.id)

        role = guild.get_role(SOWARD_PREMIUM_ROLE)

        if not member:

            raise NotPremium('this command only for premium user join support server and buy premium')

        if role in member.roles:

            return True

        else:

            raise NotPremium('this command only for premium user join support server and buy premium')

    return commands.check(predicate)


def coming_soon():
    def predicate(ctx):
        if ctx.author.id in OWNERS:
            return True
        raise ComingSoon()
    return commands.check(predicate)
