import discord
from discord.ext import commands
current_page = 1

class moderation2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Moderation"""
  
    def help_custom(self):
		      emoji = '<:Moderation:1112080205725581412> '
		      label = "Moderation"
		      description = ""
		      return label, description, current_page

    @commands.group()
    async def __Moderation__(self, ctx: commands.Context):
        """• `steal`,`addsticker`,`roleicon`,`unbanall`,`ban`, `purge bot`, `purge`,`purge all`,`purge user`,`purge reaction`,`purge images`,`purge bots`,`purge mentions`,`purge files`,`purge embeds`,`purge invites`,`nuke`, `deafen`,`addchannel`, `delchannel`, `delemoji`, `delrole`, `give`, `hide`, `hideall`, `kick`, `lock`, `lockall`, `mute`, `nick`, `role all`, `role bots`, `role humans`, `role`, `rrole bots`, `rrole humans`,`rrole`, `temprole`,`createrole`,`deleterole`,`rename`,`softban`, `steal`, `temprole`, `unban`, `unbanall`, `undeafen`, `unhide`, `unhideall`, `unlock`, `unlockall`, `unmute`,`vckick`, `vclist`, `vcmute`, `slowmode`, `vcunmute`, `warns`, `warn delete`, `warn`,`hackban`,`color`"""
async def setup(bot):
	await bot.add_cog(moderation2(bot))