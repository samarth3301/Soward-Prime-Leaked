import discord
from discord.ext import commands
current_page = 3

class anti2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Security"""
  
    def help_custom(self):
		      emoji = '<:security:1112071340053241906>'
		      label = "Antinuke"
		      description = ""
		      return label, description, current_page

    @commands.group()
    async def __antinuke__(self, ctx: commands.Context):
        """• `Antinuke enable/disable`,`Antinuke config`,`Antinuke features`,`Antinuke wl add`,`Antinuke wl remove`,`Antinuke whitelist show`,`Antinuke whitelist reset`,`Antinuke channelclean`,`Antinuke roleclean`,`Antinuke recover`,`Antinuke punishment set`,`Antinuke punishment show`,`Antinuke features`"""
async def setup(bot):
	await bot.add_cog(anti2(bot))