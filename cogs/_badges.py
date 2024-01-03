import discord
from discord.ext import commands
import json
from prince1.Tools import *
import datetime
import asyncio 
from datetime import datetime as dt
from prince.custom_checks import voter_only

class badge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name="badge", help="Check what premium badges a user have.", aliases=["badges", "pr"])
    @commands.cooldown(1, 3, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @blacklist_check()
    @ignore_check()
 #   @voter_only()
    
    async def badges(self,ctx, user_: discord.Member=None):
            user_ = user_ or ctx.author
            profile = await self.bot.get_user_profile_(user_.id)
            with open("badges.json", "r") as f:
                    idk = json.load(f)
                    if str(user_.id) not in idk:
                            await ctx.reply(embed=discord.Embed(description=f"{user_} Have no badges join [support server](https://discord.gg/h3NjK3zHn9) to get some badges.\n\n**__Commands Used__**\n{profile.cmds_used}",color=0x2f3136), mention_author=False)
                
                    elif str(user_.id) in idk:
                            embed = discord.Embed(color=discord.Colour(0x2f3136),title="<a:hypesquad:1017430505353904128> Soward Prime Achivement <a:hypesquad:1017430505353904128> ",description=f"{user_.mention} badges\n\n")
                            embed.add_field(name="**__Commands Used__**",value=profile.cmds_used)
                            for bd in idk[str(user_.id)]:
                                    embed.description += f"{bd}\n"
                                    embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)
                                    embed.set_thumbnail(url=user_.display_avatar.url)
                            await ctx.reply(embed=embed) 


    


    

    

    

async def setup(bot):
    await bot.add_cog(badge(bot))