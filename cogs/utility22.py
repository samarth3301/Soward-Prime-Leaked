import discord
from discord.ext import commands
current_page = 7

class utility22(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Utility"""
  
    def help_custom(self):
		      emoji = '<:soward_connect:1105849395888537711>  '
		      label = "Utility"
		      description = ""
		      return label, description, current_page

    @commands.group()
    async def __utility__(self, ctx: commands.Context):
        """• `donate`,`embed`,`editembed`,`av`,`roleicon`,`banner`,`afk`,`translate`,`userinfo`,`serverinfo`,`banner user`,`banner server`,`ping`,`uptime`,`find discrim`,`find name`,`find id`,`find playing`,`list boosters`,`list admins`,`list roles`,`list inrole`,`list invc`,`list activedev`,`list mods`,`list early`,`list bots`,`list botdev`,`list bans`,`calculator`,`timer`,`poll`,`suggestion`,`bugreport`,`report`,`enlarge`,`remindme`,`reminders`,`delreminder`,`bookmark`,`bookmarks`,`delbookmark`,`snipe`,`embedsnipe`,`multisnipe`,`multieditsnipe`,`editsnipe`,`nick`,`clearnick`,`vote`,`ar create`,`ar delete`,`ar edit`,`ar show`,`counting`,`setcount`"""
async def setup(bot):
	await bot.add_cog(utility22(bot))