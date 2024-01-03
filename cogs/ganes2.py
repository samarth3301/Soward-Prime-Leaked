import discord
from discord.ext import commands
current_page = 10

class gamess1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Games commands"""
  
    def help_custom(self):
		      emoji = '<:icons_games:1112078875099398294> '
		      label = "Games"
		      description = ""
		      return label, description, current_page

    @commands.group()
    async def __Games__(self, ctx: commands.Context):
        """• `tictactoe`,`rps`,`t&d`,`wumpus`,`findimposter`"""
async def setup(bot):
	await bot.add_cog(gamess1(bot))