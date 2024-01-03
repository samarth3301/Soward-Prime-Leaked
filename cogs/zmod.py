import discord
from discord.ext import commands
from core import  Context
from discord.ui import Button, View
import datetime
from typing import Optional
from prince1.Tools import *
from discord.ext.commands import Cog
from datetime import timedelta
intents = discord.Intents.all()
intents.members = True
intents.guilds = True
intents.emojis = True
intents.webhooks = True
intents = intents

class timeout(Cog):
  """Sends a list of usable commands for this server."""
  def __init__(self, client):
    self.client = client
    self.client.sniped_messages = {}

  def convert(self, time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2


    return val * time_dict[unit]
  

    

  #@commands.command(name="timeout", help="Mutes a specific member", aliases=["mute", "stfu"])
  #@blacklist_check()
 # @commands.cooldown(1, 20, commands.BucketType.member)
  #@commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
 # @commands.guild_only()
 # @commands.has_permissions(moderate_members=True)
  #async def _mute(self, ctx, member: discord.Member, duration):
   # ok = duration[:-1]
   # tame = self.convert(duration)
   # till = duration[-1]
  #  if tame == -1:
   #   await ctx.reply(f"You didnt didnt gave time with correct unit\nExamples:\nmute <member> 10m", mention_author=False)
   # elif tame == -2:
    #  await ctx.reply(embed=discord.Embed(title=f"Time must be an integer!", color=0x2f3136))
   # else:
   #   if till.lower() == "d":
    #    t = datetime.timedelta(seconds=tame)
    #    msg = discord.Embed(description=f"<:ri8:1038487759750438912> Successfully Muted {member.mention} For {1} Day(s)".format(member, ok), color=0x2f3136)
   #   elif till.lower() == "m":
    #    t = datetime.timedelta(seconds=tame)
   #     msg = discord.Embed(description=f"<:ri8:1038487759750438912> Successfully Muted {member.mention} For {1} Minute(s)".format(member, ok), color=0x2f3136)
   #   elif till.lower() == "s":
     #   t = datetime.timedelta(seconds=tame)
   #     msg = discord.Embed(description=f"<:ri8:1038487759750438912> Successfully Muted {member.mention} For {1} Second(s)".format(member, ok), color=0x2f3136)
    #  elif till.lower() == "h":
    #    t = datetime.timedelta(seconds=tame)
   #     msg = discord.Embed(description=f"<:ri8:1038487759750438912> Successfully Muted {member.mention} For {1} Hour(s)".format(member, ok), color=0x2f3136)

  #  try:
   #   if member.guild_permissions.administrator:
   #     await ctx.reply(embed=discord.Embed(title="I can't mute administrators",color=0x2f3136))
   #   else:
   #     await member.timeout(discord.utils.utcnow() + t, reason="Muted By: {0}".format(ctx.author))
   #     await ctx.send(embed=msg)
   # except:
   #   await ctx.send("An error occurred")


  
  @commands.command(name = "timeout", description = "Timeouts member",aliases=["mute","stfu"])

   # @commands.describe(member = "Member to timeout.", time = "Time of the timeout.", reason = "Reason to timeout.")

  @commands.cooldown(1, 10, commands.BucketType.user)

  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @ignore_check()

  @commands.guild_only()

  @commands.has_permissions(moderate_members = True)

  async def timeout(self, ctx, member : discord.Member, time: str=None, reason: str = None):

        #check author role

        if ctx.author.top_role <= member.top_role:

            return await ctx.send(f"Your role must be higher than {member.mention}.", delete_after=5)

        #check bot role

        if ctx.guild.me.top_role <= member.top_role:

            return await ctx.send(f"My role must be higher than {member.mention}.", delete_after = 5)

        #time stuff

        if time == None:

            time_string = ""

        else:

            time_string = f"\nTime: {time}"

            get_time = {

            "s": 1, "m": 60, "h": 3600, "d": 86400,

            "w": 604800, "mo": 2592000, "y": 31104000 }

            a = time[-1]

            b = get_time.get(a)

            c = time[:-1]

            try: int(c)

            except: return await ctx.send("Type time and time unit (s,m,h,d,w,mo,y) correctly.", delete_after = 5)

            try: sleep = int(b) * int(c)

              

                

              

                

            except: return await ctx.send("Type time and time unit (s,m,h,d,w,mo,y) correctly.", delete_after =5)

        #timing out

        await member.timeout(timedelta(seconds = sleep), reason =f"{reason} by {ctx.author}")

        #check reason

        if reason == None: reason = f""

        else: reason = f"\nReason: {reason}"

        timeout_embed = discord.Embed(title = "Timeout!", description = f"{member.mention} has been timed out by {ctx.author.mention}{time_string}{reason}", color=0x2f3136)

        await ctx.send(embed = timeout_embed)

        #timeout over message

        await asyncio.sleep(int(sleep))

        timeout_embed = discord.Embed(title = "Timeout over!", description = f"{member.mention}'s timeout is over", colour = discord.Colour.green())

        await ctx.send(embed = timeout_embed)

  @commands.command(name="untimeout", aliases=["unmute", "unshut"], help="Unmutes a member")
  @blacklist_check()
  @ignore_check()
  @commands.cooldown(1, 20, commands.BucketType.member)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(moderate_members=True)
  async def _unmute(self, ctx, member: discord.Member):
    if member.is_timed_out():
      try:
        await member.edit(timed_out_until=None)
        await ctx.reply(embed=discord.Embed(description=f"<:ri8:1038487759750438912> successfully unmuted {member.mention}",color=0x2f3136))

      except Exception as e:
        await ctx.reply(embed=discord.Embed(title="Unable to Remove Timeout:\n```py\n{}```".format(e), color=0x2f3136))
    else:
      await ctx.reply(embed=discord.Embed(title="{} Is Not Muted".format(member.name), color=0x2f3136))

async def setup(client):
    await client.add_cog(timeout(client)) 
