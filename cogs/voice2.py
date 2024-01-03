import discord

from discord.ext import commands

current_page = 1

class voice2(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    """voice commands"""

  

    def help_custom(self):

		      emoji = '<:voice:1112082331004567583> '

		      label = "Voice"

		      description = ""

		      return label, description, current_page

    @commands.group()

    async def __voice__(self, ctx: commands.Context):

        """`j2c setup`,`j2c reset`,`vc kick`,vc kickall`,`vc move`,`vc moveall`,`vc mute`,`vc muteall`,`vc unmute`,`vc unmuteall`,`vc deafen`,`vc deafenall`,`vc undeafen`,`vc undeafenall`,`vcrole humans add`,`vcrole bots add`,`vcrole config`,`vcrole reset`,`vcrole humans remove`,`vcrole bots remove`"""

async def setup(bot):

	await bot.add_cog(voice2(bot))