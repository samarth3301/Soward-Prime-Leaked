import discord
from discord.ext import commands
import json
from prince1.Tools import *
from prince.bot import Bot
from discord.ui import Button, View
import discord
from discord.ext import commands
from core.Context import *
from discord.ui import Button, View
import datetime
from typing import Optional
from prince1.Tools import *
from discord.ext.commands import Cog

intents = discord.Intents.all()
intents.members = True
intents.guilds = True
intents.emojis = True
intents.webhooks = True
intents = intents

class hmbc(Cog):
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

  

  @commands.command(name="lock", help="Locks the channel")
  @ignore_check()
  @blacklist_check()
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(manage_channels=True)
  async def _lock(self, ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role,
                                  overwrite=overwrite,
                                  reason=f"Channel Locked By {ctx.author} | ({ctx.author.id})")
    await ctx.reply(embed=discord.Embed(title=f"<:eg_lock:1018057640724660226> | {ctx.channel.mention} has been locked!", color=0x42f579))

  
  @commands.command(name="unlock", help="Unlocks the channel")
  @blacklist_check()
  @ignore_check()
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(manage_channels=True)
  async def _unlock(self, ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role,
                                  overwrite=overwrite,
                                  reason=f"Channel Unlocked By {ctx.author} | ({ctx.author.id})")
    await ctx.reply(embed=discord.Embed(title=f"<:eg_unlock:1018057690154537051> | {ctx.channel.mention} has been unlocked!", color=0x42f579))




async def setup(client):
    await client.add_cog(hmbc(client))