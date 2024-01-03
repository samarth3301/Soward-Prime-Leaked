import discord
from discord.ext import commands
current_page = 4

class ticket2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Ticket"""
  
    def help_custom(self):
		      emoji = '<:ticketpu:1112076027963900007>'
		      label = "Ticket"
		      description = ""
		      return label, description, current_page

    @commands.group()
    async def __Ticket__(self, ctx: commands.Context):
        """• `ticket sendpanel`,`ticket setup`,`ticket close`,`ticket role add`,`ticket role remove`"""
async def setup(bot):
	await bot.add_cog(ticket2(bot))