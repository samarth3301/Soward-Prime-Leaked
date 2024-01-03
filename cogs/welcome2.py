import discord
from discord.ext import commands
#from core import Cog, Astroz, Context
from prince1.Tools import *
from typing import *
from prince1.Tools2 import *
from prince1 import Cog
class greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        data = getDB(member.guild.id)
        msg = data["welcome"]["message"]
        chan = list(data["welcome"]["channel"])
        emtog = data["welcome"]["embed"]
        emping = data["welcome"]["ping"]
        emimage = data["welcome"]["image"]
        emthumbnail = data["welcome"]["thumbnail"]
    #    emautodel = data["welcome"]["autodel"]
        emtitle = data["welcome"]["title"]
        emcolor = data["welcome"]["color"]
        emfooter = data["welcome"]["footer"]
        user = member
        if chan == []:
            return
        else:
            if "{server.name}" in msg:
              msg = msg.replace("{server.name}", "%s" % (user.guild.name))
            if "{server.member_count}" in msg:
              msg = msg.replace("{server.member_count}", "%s" % (user.guild.member_count))
            if "{user.name}" in msg:
              msg = msg.replace("{user.name}", "%s" % (user))
            if "{user.mention}" in msg:
              msg = msg.replace("{user.mention}", "%s" % (user.mention))
            if "{user.created_at}" in msg:
              msg = msg.replace("{user.created_at}", f"<t:{int(user.created_at.timestamp())}:F>")
            if "{user.joined_at}" in msg:
              msg = msg.replace("{user.joined_at}", f"<t:{int(user.joined_at.timestamp())}:F>")
            if msg == "":
              msg = ""
            else:
              msg = msg
            if emping == "":
                emping = ""
      #      if "{user.name}" in emping:
     #         emping = emping.replace("{user.name}", "%s" % (user))
            if "{user.mention}" in emping:
                emping = emping.replace("{user.mention}", "%s" % (user.mention))				
            else:
                emping = ""
      #      if emautodel == 0:
        #      emautodel = None
       #     else:
       #       emautodel = emautodel
            if emtitle == "":
                emtitle = ""
            if "{user.name}" in emtitle:
              emtitle = emtitle.replace("{user.name}", "%s" % (user))
            if emfooter == "":
                emfooter = "" 
            if "{server.name}" in emfooter:
                emfooter = emfooter.replace("{server.name}", "%s" % (user.guild.name))
            if "{server.member_count}" in emfooter:
                emfooter = emfooter.replace("{server.member_count}",
                                  "%s" % (user.guild.member_count))
            if "{user.name}" in emfooter:
                emfooter = emfooter.replace("{user.name}", "%s" % (user))
			
            
            em = discord.Embed(title=emtitle,description=msg, color=0x2f3136)
            em.set_author(name=user, icon_url=member.avatar.url if member.avatar else member.default_avatar.url)
            em.timestamp = discord.utils.utcnow()
            if emimage == "":
                em.set_image(url="")
            else:
                em.set_image(url=emimage)
            if emthumbnail == "":
                em.set_thumbnail(url="")
            else:
                em.set_thumbnail(url=emthumbnail)
            if user.guild.icon is not None:
            
                em.set_footer(  text=emfooter, icon_url=user.guild.icon)
            if emtog == True:
                for chh in chan:
                    ch = self.bot.get_channel(int(chh))
            try:
                await ch.send(emping, embed=em)
            except:
                pass
            else:
                for chh in chan:
                    ch = self.bot.get_channel(int(chh))
                if emtog == False:
           
                    await ch.send(msg)
            


async def setup(bot):
    await bot.add_cog(greet(bot)) 
					