from discord.ext import commands
import discord
import os
from discord.ext.commands import Cog, Context
from prince1.Tools import *
from humanfriendly import format_timespan
import datetime
class ui(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.client = client
    self.color = discord.Color(0x42f579)
 

  @commands.command(name="userinfo", aliases=["ui"])
  @blacklist_check()
  @ignore_check()
  async def whois(self, ctx: Context, *, member: discord.User=None):
    user = member if member else ctx.author
    guild = ctx.guild
    us = await self.client.fetch_user(user.id)
    if us.public_flags.active_developer:
      op = "<a:ActiveDeveloper:1093545270014394380>"
    else:
        op= ""
    if us.public_flags.hypesquad_brilliance:
      ok = "<:Hypesqued__briliance:1093545559689801789>"
    else:
        ok = ""
    if us.public_flags.hypesquad_balance:
      prince = "<:Hypesquad_Balance:1093551124923031582>"
	  
    else:
        prince = ""
    if us.public_flags.hypesquad_bravery:
      bra = "<:Hypesquad_Bravery:1093553761131180144>"
    else:
        bra = ""
    if us.public_flags.early_supporter:
      er = "<:EARLY_SUPPORTER:1017728098436919356>"
    else:
        er = ""


    
    gl = guild.get_member(user.id)
    badges = ""
    if int(us.public_flags.value) == 0:
      badges+="None"
    else:
      for w in us.public_flags:
        badgexd = w[0]
        badgexdvalue = w[1]
        if badgexdvalue:
          badges+=f"{badgexd.replace('_', ' ')}"
          badges+=", "
      badges.strip(",")
    if us.bot:
      bmt = "Yes"
    else:
      bmt = "No"
    embed = discord.Embed(color=0x2f3136)
    embed.set_author(name=f"{us.name}'s Information", icon_url=us.display_avatar.url)
    embed.set_thumbnail(url=us.display_avatar.url)
    if gl == None:
      embed.add_field(name="__General Information__", value=f"**Name:** {us}\n**ID:** {us.id}\n**Mention:** {us.mention}\n**Bot?:** {bmt}\n**Badges:** {op}{ok}{prince}{bra}{er}\n**Account Created:** <t:{round(us.created_at.timestamp())}:R>")
      if us.banner:
        embed.set_image(url=us.banner.url)
      embed.set_footer(text=f"{us.name} is not in this server.", icon_url=ctx.message.author.display_avatar)
    else:
      embed.add_field(name="__General Information__", value=f"**Name:** {us}\n**ID:** {us.id}\n**Mention:** {us.mention}\n**Bot?:** {bmt}\n**Badges:** {op}{ok}{prince}{bra}{er}\n**Account Created:** <t:{round(us.created_at.timestamp())}:R>\n**Server joined** <t:{round(gl.joined_at.timestamp())}:R>")
      highxd = gl.top_role if gl.top_role else "None"
      try:
        if highxd.id == guild.default_role.id:
          highxd = "None"
      except:
        pass
      mntn = 'None' if highxd == "None" else highxd.mention
      rlsxd = ""
      if len(gl.roles) > 20:
        rlsxd+="Too many roles to show here.(Above 20)"
      else:
        for role in gl.roles:
          if not role.id == guild.default_role.id:
            rlsxd+=f"{role.mention}, "
        rlsxd.strip(",")
      if rlsxd == "":
        rlsxd+="None"
      clr = "#000000" if highxd == "None" else highxd.color
      embed.add_field(name="__Role info__", value=f"**Highest Role:** {mntn}\n**Roles:** {rlsxd.rsplit(',', 1)[0]}\n**Color:** {clr}")
      channelxd = None
      for ch in guild.voice_channels:
        if gl in ch.members:
          channelxd = ch.mention
      bstxd = discord.utils.format_dt(gl.premium_since) if not gl.premium_since is None else "None"
      embed.add_field(name="__Extra__", value=f"**Boosting:** {bstxd}\n**Voice <a:voice:1017402454159147039>:** {channelxd}")
      pxs = ""
      for pm in gl.guild_permissions:
        loml = pm[0]
        xsd = pm[1]
        if xsd:
          pxs += f"{loml.replace('_', ' ')}, "
      if pxs == "":
        pxs+="None"
      embed.add_field(name="__Key Permissions__", value=pxs.rsplit(",", 1)[0])
      vlue = ""
      if gl == guild.owner:
        vlue+="Server Owner"
      if gl.bot:
        vlue+="Server Bot"
      if gl.guild_permissions.administrator:
        if vlue == "":
          vlue+='Server Administrator'
      if gl.guild_permissions.manage_channels or gl.guild_permissions.manage_roles or gl.guild_permissions.kick_members or gl.guild_permissions.ban_members or gl.guild_permissions.manage_guild or gl.guild_permissions.manage_messages:
        if vlue == "":
          vlue+="Server Moderator"
      if vlue == "":
        vlue+="Server Member"
      embed.add_field(name="__Acknowledgements__", value=vlue)
      embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
      embed.timestamp = discord.utils.utcnow()
      if us.banner:
        embed.set_image(url=us.banner.url)
    await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(ui(client))