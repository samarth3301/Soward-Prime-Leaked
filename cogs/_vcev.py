import discord

from discord.ext import commands

#from core import  Cog

from discord.utils import *

from discord import *
from discord.ext.commands import Cog
#from utils.Tools import *

from discord.utils import get

from prince1.Tools import *

class Vcroles22(Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.Cog.listener()

    async def on_voice_state_update(self, member, before, after):

        data = getVC(member.guild.id)

        if member.bot:

            if data["vcrole"]["bots"] == "":

                return

            else:

                if not before.channel and after.channel:

                    r = data["vcrole"]["bots"]

                    br = get(member.guild.roles, id=r)

                    await member.add_roles(br, reason="Soward | VC Roles (Joined VC)")

                elif before.channel and not after.channel:

                    r1 = data["vcrole"]["bots"]

                    br1 = get(member.guild.roles, id=r1)

                    await member.remove_roles(br1, reason="Soward | VC Roles (Left VC)")

        elif member.bot != True:

            if data["vcrole"]["humans"] == "":

                return

            else:

                if not before.channel and after.channel:

                    r2 = data["vcrole"]["humans"]

                    br2 = get(member.guild.roles, id=r2)

                    await member.add_roles(br2, reason="Soward | VC Roles (Joined VC)")

                elif before.channel and not after.channel:

                    r3 = data["vcrole"]["humans"]

                    br3 = get(member.guild.roles, id=r3)

                    await member.remove_roles(br3, reason="Soward | VC Roles (Left VC)")
async def setup(bot):
  await bot.add_cog(Vcroles22(bot))
