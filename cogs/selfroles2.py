import discord
from discord.ext import commands
current_page = 5

class selfroles1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Selfroles commands"""
  
    def help_custom(self):
		      emoji = ' <:ares_eventcolour:1112328254947340429>'
		      label = "Selfroles"
		      description = ""
		      return label, description, current_page

    @commands.group()
    async def __selfroles__(self, ctx: commands.Context):
        """• `selfroles`,`selfroles create`,`selfroles edit`,`selfroles list`,`selfroles delete`"""
async def setup(bot):
	await bot.add_cog(selfroles1(bot))