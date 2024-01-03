import discord
from discord.ext import commands
current_page = 2 

class fun1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Fun commands"""
  
    def help_custom(self):
		      emoji = '<:IconHeart:1112376504236650506> '
		      label = "Fun"
		      description = ""
		      return label, description, current_page

    @commands.group()
    async def __Fun__(self, ctx: commands.Context):
        """• `Anyone`,`should-i`,`press-f`,`beer`,`brainsize`,`howcute`,`howhorny`,`howgay`,`howsus`,`firstmessage`,`simpfor`,`reverse`,`mock`,`aesthetic`,`meme`,`fact`,`quote`,`advice`,`ascii`,`dice`,`Feed`,`bite`,`Cuddle`,`wink`,`hug`,`kiss`,`pat`,`slap`,`tickle`,`lick`,`facepalm`,`blush`,`tail`,`cry  `"""
async def setup(bot):
	await bot.add_cog(fun1(bot))