import discord
from discord.ext import commands
current_page =  9

class extra1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """extra commands"""
  
    def help_custom(self):
		      emoji = '<:soward_connect:1105849395888537711> '
		      label = "Custom Roles"
		      description = ""
		      return label, description, current_page

    @commands.group()
    async def __Extra__(self, ctx: commands.Context):
        """• `setup add`, `setup delete`,`setup clear`,`setup list`,`setup reqrole`,`setup friends`,`setup vips`,`setup guests`,`setup officials`,`setup girls`,`setup bot`,`setup modss`,`setup artist`,`config-setup`"""
async def setup(bot):
	await bot.add_cog(extra1(bot))