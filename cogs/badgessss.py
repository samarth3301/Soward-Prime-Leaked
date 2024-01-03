import discord
from discord.ext import commands
import json
from prince1.Tools import*


class badge3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.badgesgiver = [980361546918162482,1018139793789563000,984815117730480228,1068967045263261746,1087793230638239869,1068967045263261746,1090957904410071120]
    

    @commands.command(aliases=["addb"])
    @ignore_check()
    async def addbadge(self, ctx, user: discord.Member, *, badge):
      if ctx.author.id in self.badgesgiver:
        with open("badges.json", "r") as f:
          idk = json.load(f)
          if str(user.id) not in idk:
              idk[str(user.id)] = []
              idk[str(user.id)].append(f"{badge}")
              await ctx.reply(embed=discord.Embed(title=f" Added badge {badge} to {user}.",  color=0x42f579))
          elif str(user.id) in idk:
              idk[str(user.id)].append(f"{badge}")
              await ctx.reply(embed=discord.Embed(title=f" Added badge {badge} to {user}.",color=0x42f579))
          with open("badges.json", "w") as f:
            json.dump(idk, f, indent=4)


    
       
    @commands.command(aliases=['rb'])
    @ignore_check()
    async def removebadge(self, ctx, user: discord.User = None):
      if ctx.author.id in self.badgesgiver:
        if user is None:
            await ctx.reply(embed=discord.Embed(title="You must specify a user to remove badge.", color=0x42f579))
            return
        with open('badges.json', 'r') as f:
            badges = json.load(f)
        try:
            if str(user.id) in badges:
                badges.pop(str(user.id))

                with open('badges.json', 'w') as f:
                    json.dump(badges, f, indent=4)

                await ctx.reply(embed=discord.Embed(title=f"Removed badge of {user}", color=0x42f579))
        except KeyError:
            await ctx.reply("This user has no badge.")

async def setup(bot):
    await bot.add_cog(badge3(bot))