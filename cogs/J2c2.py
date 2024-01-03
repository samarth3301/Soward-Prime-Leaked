import discord
from discord.ext import commands
current_page =  12
from prince1.Tools import *
class j2cc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """J2c commands"""
  
    def help_custom(self):
		      emoji = '<:SOWARD_J2C:1114423746787291156> '
		      label = "Join To Create"
		      description = ""
		      return label, description, current_page

    @commands.group()
    async def __j2x__(self, ctx: commands.Context):
        """• `j2c setup`,`j2c reset`"""
async def setup(bot):
	await bot.add_cog(j2cc(bot))