import discord
from discord.ext import commands
import json
from prince1.Tools import *
from core.Context import *
from discord import utils
class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    

    

   

    @commands.command(aliases=["config-setup"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    @ignore_check()

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    async def configsetup(self,ctx):
      with open("reqrole.json","r") as f:
          key = json.load(f)
      if f'{ctx.guild.id}' not in key:
        rr = "Reqrole is not set"
      elif f'{ctx.guild.id}' in key:
        for idk in key[str(ctx.guild.id)]:
          xd = discord.utils.get(ctx.guild.roles,id=int(idk))
          rr = f"{xd.mention}"
      with open("girl.json", 'r') as f:
          key = json.load(f)
      if f'{ctx.guild.id}' not in key:
        gr = "Role is not set"
      elif f'{ctx.guild.id}' in key:
        for idk in key[str(ctx.guild.id)]:
          a = discord.utils.get(ctx.guild.roles, id=int(idk))
          gr = f"{a.mention}"
      with open("official.json", 'r') as f:
          key = json.load(f)
      if f'{ctx.guild.id}' not in key:
        ofr = "Role is not set"
        
      elif f'{ctx.guild.id}' in key:
        for idk in key[str(ctx.guild.id)]:
          o = discord.utils.get(ctx.guild.roles, id=int(idk))
          ofr = f"{o.mention}"
      with open("friends.json", 'r') as f:
          key = json.load(f)
      if f'{ctx.guild.id}' not in key:
        fr = "Role is not set"
        
      elif f'{ctx.guild.id}' in key:
        for idk in key[str(ctx.guild.id)]:
          f = discord.utils.get(ctx.guild.roles, id=int(idk))
          fr = f"{f.mention}"
      with open("vip.json", 'r') as f:
          key = json.load(f)
      if f'{ctx.guild.id}' not in key:
        vr = "Role is not set"
        
      elif f'{ctx.guild.id}' in key:
        for idk in key[str(ctx.guild.id)]:
          v = discord.utils.get(ctx.guild.roles, id=int(idk))
          vr = f"{v.mention}"
      with open("guest.json", 'r') as f:
          key = json.load(f)
      if f'{ctx.guild.id}' not in key:
        gt = "Role is not set"
        #await ctx.send('')
      elif f'{ctx.guild.id}' in key:
        for idk in key[str(ctx.guild.id)]:
          g = discord.utils.get(ctx.guild.roles, id=int(idk))
          gt = f"{g.mention}"
      with open("mod.json", 'r') as f:
          key = json.load(f)
      if f'{ctx.guild.id}' not in key:
        modr = "Role is not set"
      elif f'{ctx.guild.id}' in key:
        for idk in key[str(ctx.guild.id)]:
          mr = discord.utils.get(ctx.guild.roles, id=int(idk))
        modr = f"{mr.mention}"
      with open("bot.json", 'r') as f:
          key = json.load(f)
      if f'{ctx.guild.id}' not in key:
        botr = "Role is not set"
      elif f'{ctx.guild.id}' in key:
        for idk in key[str(ctx.guild.id)]:
           br = discord.utils.get(ctx.guild.roles, id=int(idk))
        botr = f"{br.mention}"
      with open("artist.json", 'r') as f:
          key = json.load(f)
      if f'{ctx.guild.id}' not in key:
        artr = "Role is not set"
      elif f'{ctx.guild.id}' in key:
        for idk in key[str(ctx.guild.id)]:
          ar = discord.utils.get(ctx.guild.roles, id=int(idk))
        artr = f"{ar.mention}"
      embed = discord.Embed(title="Custom Role Setup", description=f"Reqrole\n{rr}",color=0x2f3136, timestamp=ctx.message.created_at)
      embed.add_field(name="Girls Role", value=gr)
      embed.add_field(name="Official Role", value= ofr)
      embed.add_field(name="Guest Role", value= gt)
      embed.add_field(name="Friend Role", value= fr)
      embed.add_field(name="Vip Role", value= vr)
      embed.add_field(name="Mod Role", value=modr)
      embed.add_field(name="Bot Role", value=botr)
      embed.add_field(name="Artist Role", value=artr)
      if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon)
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
            embed.set_footer(text="Made By Prince", icon_url=self.bot.user.avatar)
      await ctx.reply(embed=embed)

    
    

    
    
async def setup(bot):
    await bot.add_cog(test(bot))