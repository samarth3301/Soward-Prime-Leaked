import discord
from discord.ext import commands
current_page = 8

class swagat1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Welcome"""
  
    def help_custom(self):
		      emoji = '<a:welcome:1112077724354363392>'
		      label = "Welcome"
		      description = ""
		      return label, description, current_page

    @commands.group()
    async def __welcome__(self, ctx: commands.Context):
        """• `Autorole humans add`,`Autorole humans remove`,`Autorole bots add`,`Autorole bots remove`,`welcome channel add`,`welcome channel remove`,`welcome message`,`welcome embed`,`welcome ping`,`welcome title add`,`welcome title Remove`,`welcome image add`,`welcome image remove`,`welcome thumbnail add`,`welcome thumbnail remove`,`welcome footer add`,`welcome footer remove`,`welcome ping on`,`welcome ping off`,`welcome test`"""
async def setup(bot):
	await bot.add_cog(swagat1(bot))