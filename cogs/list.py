import discord
from discord.ext import commands
#from .utils.lister import lister
import reactionmenu
from reactionmenu import ViewMenu, ViewButton
from .op.lister import lister
from prince1.Tools import *
async def boost_lis(ctx, color, listxd, *, title):
  embed_array = []
  t = title
  clr = 0x2f3136
  sent = []
  your_list = listxd
  count = 0
  embed = discord.Embed(color=0x2f3136, description="", title=t)
  embed.set_footer(icon_url=ctx.bot.user.avatar)
  if len(listxd) > 1:
    for i in range(len(listxd)):
      for i__ in range(10):
        if not your_list[i].id in sent:
          count+=1
          if str(count).endswith("0") or len(str(count)) != 1:
            actualcount = str(count)
          else:
            actualcount = f"0{count}"
          embed.description+=f"`[{actualcount}]` | {your_list[i]} [{your_list[i].mention}] - <t:{round(your_list[i].premium_since.timestamp())}:R>\n"
          sent.append(your_list[i].id)
      if str(count).endswith("0") or str(count) == str(len(your_list)):
        embed_array.append(embed)
        embed = discord.Embed(color=0x2f3126, description="", title=t)
        embed.set_footer(icon_url=ctx.bot.user.avatar)
  if len(embed_array) == 0:
    embed_array.append(embed)
  pag = PaginationViewWallah(embed_array, ctx)
  if len(embed_array) == 1:
    await pag.start(ctx, True)
  else:
    await pag.start(ctx)

async def rolis(ctx, color, listxd, *, title):
  embed_array = []
  t = title
  clr = 0x2f3136
  sent = []
  your_list = listxd
  count = 0
  embed = discord.Embed(color=0x2f3136, description="", title=t)
  embed.set_footer(icon_url=ctx.bot.user.avatar)
  if len(listxd) > 1:
    for i in range(len(listxd)):
      for i__ in range(10):
        if not your_list[i].id in sent:
          count+=1
          if str(count).endswith("0") or len(str(count)) != 1:
            actualcount = str(count)
          else:
            actualcount = f"0{count}"
          embed.description+=f"`[{actualcount}]` | {your_list[i].mention} `[{your_list[i].id}]` - {len(your_list[i].members)} members\n"
          sent.append(your_list[i].id)
      if str(count).endswith("0") or str(count) == str(len(your_list)):
        embed_array.append(embed)
        embed = discord.Embed(color=clr, description="", title=t)
        embed.set_footer(icon_url=ctx.bot.user.avatar)
  if len(embed_array) == 0:
    embed_array.append(embed)
  pag = PaginationViewWallah(embed_array, ctx)
  if len(embed_array) == 1:
    await pag.start(ctx, True)
  else:
    await pag.start(ctx)


async def lister_bn(ctx, color, listxd, *, title):
  embed_array = []
  t = title
  clr = 0x2f3136
  sent = []
  your_list = listxd
  count = 0
  embed = discord.Embed(color=clr, description="", title=t)
  embed.set_footer(icon_url=ctx.bot.user.avatar)
  if len(listxd) > 1:
    for i in range(len(listxd)):
      for i__ in range(10):
        if not your_list[i].user.id in sent:
          count+=1
          if str(count).endswith("0") or len(str(count)) != 1:
            actualcount = str(count)
          else:
            actualcount = f"0{count}"
          embed.description+=f"`[{actualcount}]` | {your_list[i].user} [{your_list[i].user.id}]\n"
          sent.append(your_list[i].user.id)
      if str(count).endswith("0") or str(count) == str(len(your_list)):
        embed_array.append(embed)
        embed = discord.Embed(color=clr, description="", title=t)
        embed.set_footer(icon_url=ctx.bot.user.avatar)
  if len(embed_array) == 0:
    embed_array.append(embed)
  pag = PaginationViewWallah(embed_array, ctx)
  if len(embed_array) == 1:
    await pag.start(ctx, True)
  else:
    await pag.start(ctx)

        
async def working_lister(ctx, color, listxd, *, title):
  embed_array = []
  t = title
  clr = 0x2f3136
  sent = []
  your_list = listxd
  count = 0
  idkh=True
  embed = discord.Embed(color=clr, description="", title=t)
  embed.set_footer(icon_url=ctx.bot.user.avatar)
  if idkh:
    for i in range(len(listxd)):
      for i__ in range(10):
        if not your_list[i].id in sent:
          count+=1
          if str(count).endswith("0") or len(str(count)) != 1:
            actualcount = str(count)
          else:
            actualcount = f"0{count}"
          embed.description+=f"`[{actualcount}]` | {your_list[i]} [<@{your_list[i].id}>]\n"
          sent.append(your_list[i].id)
      if str(count).endswith("0") or str(count) == str(len(your_list)):
        embed_array.append(embed)
        embed = discord.Embed(color=clr, description="", title=t)
        embed.set_footer(icon_url=ctx.bot.user.avatar)
  
  if len(embed_array) == 0:
    embed_array.append(embed)
  pag = PaginationViewWallah(embed_array, ctx)
  if len(embed_array) == 1:
    await pag.start(ctx, True)
  else:
    await pag.start(ctx)

class PaginationViewWallah:
  def __init__(self, embed_list, ctx):
    self.elist = embed_list
    self.context = ctx

  def disable_button(self, menu):
    tax = str(menu.message.embeds[0].footer.text).replace(" ", "").replace("Page", "")
    num = int(tax[0])
    if num == 1:
      fis=menu.get_button("2", search_by="id")
      bax = menu.get_button("1", search_by="id")
      
      

  def enable_button(self, menu):
    tax = str(menu.message.embeds[0].footer.text).replace(" ", "").replace("Page", "")
    num = int(tax[0])
    if num != 1:
      fis=menu.get_button("2", search_by="id")
      bax = menu.get_button("1", search_by="id")
      print(bax)
      
    
  async def dis_button(self, menu):
    self.disable_button(menu)

  async def ene_button(self, menu):
    self.ene_button(menu)


  
  async def start(self, ctx, disxd=False):
    style = f"{ctx.bot.user.name} • Page $/&"
    menu = ViewMenu(ctx, menu_type=ViewMenu.TypeEmbed, style=style)
    for xem in self.elist:
      menu.add_page(xem)
    lax = ViewButton(style=discord.ButtonStyle.secondary, label=None,emoji='⏪', custom_id=ViewButton.ID_GO_TO_FIRST_PAGE)
    menu.add_button(lax)
    bax = ViewButton(style=discord.ButtonStyle.secondary, label=None,emoji='◀️', custom_id=ViewButton.ID_PREVIOUS_PAGE)
    menu.add_button(bax)
    bax2 = ViewButton(style=discord.ButtonStyle.secondary, label=None,emoji='⏹️', custom_id=ViewButton.ID_END_SESSION)
    menu.add_button(bax2)
    bax3 = ViewButton(style=discord.ButtonStyle.secondary, label=None,emoji='▶️', custom_id=ViewButton.ID_NEXT_PAGE)
    menu.add_button(bax3)
    sax = ViewButton(style=discord.ButtonStyle.secondary, label=None,emoji='⏩', custom_id=ViewButton.ID_GO_TO_LAST_PAGE)
    menu.add_button(sax)
    if disxd:
      menu.disable_all_buttons()
    menu.disable_button(lax)
    menu.disable_button(bax)
    async def all_in_one_xd(payload):
      
      newmsg = await ctx.channel.fetch_message(menu.message.id)
      tax = str(newmsg.embeds[0].footer.text).replace(f"{ctx.bot.user.name}","").replace(" ", "").replace("Page", "").replace("•","")
      saxl = tax.split("/")
      num = int(saxl[0])
      numw = int(saxl[1])
      if num == 1:
        menu.disable_button(lax)
        menu.disable_button(bax)
      else:
        menu.enable_button(lax)
        menu.enable_button(bax)
      if num == numw:
        menu.disable_button(bax3)
        menu.disable_button(sax)
      else:
        menu.enable_button(bax3)
        menu.enable_button(sax)
      await menu.refresh_menu_items()
    menu.set_relay(all_in_one_xd)
    await menu.start()

class utility5(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tasks = []
      
    @commands.hybrid_group(name="list")
    async def __list_(self, ctx):
      print("list cmd")

    @__list_.command(name="boost", aliases=["boosters", "booster", "bst", "boosted", "bsted", "bost"],description="See a list of boosters in the server")
    @ignore_check()
    async def seggs(self, ctx):
      
      l = []
      ok = {}
      for member in ctx.guild.premium_subscribers:
        wz = sum(m.premium_since < member.premium_since for m in ctx.guild.premium_subscribers if m.premium_since is not None)
        ok[str(wz)] = str(member.id)
      for i in range(len(ctx.guild.premium_subscribers)):
        sure = ok.get(str(i))
        l.append(ctx.guild.get_member(int(sure)))
      await boost_lis(ctx=ctx, listxd=l, color=0x2f3136, title=f" LIST OF BOOSTERS IN {ctx.guild.name} - {int(len(l))}")

    @__list_.command(name="bots",aliases=["botss"],description="Get a list of all bots in a server")
    @ignore_check()
    async def bots(self, ctx):
      loda = []
      for member in ctx.guild.members:
        if member.bot:
          loda.append(member)
      await working_lister(listxd=loda, color=0x2f3136, title=f"BOTS IN {ctx.guild.name} - {int(len(loda))}", ctx=ctx)

    @__list_.command(name="admins",aliases=["admin","administrator","administration"],description="Get a list of all admins of a server")
    @ignore_check()
    async def admins(self, ctx):
      loda = []
      for member in ctx.guild.members:
        if member.guild_permissions.administrator:
          loda.append(member)
      await working_lister(listxd=loda, color=0x2f3135, title=f" ADMINS IN {ctx.guild.name} - {int(len(loda))}", ctx=ctx)

    @__list_.command(name="mods",aliases=["mod","moderator"],description="Get a list of all mods of a server")
    @ignore_check()
    async def mods(self, ctx):
      loda = []
      for member in ctx.guild.members:
        if member.guild_permissions.manage_guild or member.guild_permissions.manage_messages or member.guild_permissions.manage_channels or member.guild_permissions.manage_nicknames or member.guild_permissions.manage_roles or member.guild_permissions.manage_emojis_and_stickers or member.guild_permissions.manage_emojis or member.guild_permissions.moderate_members:
          if not member.guild_permissions.administrator:
            loda.append(member)
      await working_lister(listxd=loda, color=0x2f3136, title=f"MODS IN {ctx.guild.name} - {int(len(loda))}", ctx=ctx)

    @__list_.command(name="early",aliases=["earlybadge","earlysupporter"],description="Get a list of early id in a server")
    @ignore_check()
    async def early(self, ctx):
      loda = []
      for member in ctx.guild.members:
        if member.public_flags.early_supporter:
          loda.append(member)
      
      await working_lister(listxd=loda, color=0x2f3136, title=f"EARLY ID'S IN  {ctx.guild.name} - {int(len(loda))}", ctx=ctx)
               
    @__list_.command(name="botdev",aliases=["developer","botdeveloper"],description="Get a list of bot developer in a server")
    @ignore_check()
    async def botdev(self, ctx):
      loda = []
      for member in ctx.guild.members:
        if member.public_flags.early_verified_bot_developer:
          loda.append(member)
      if loda == []:
        return await ctx.reply("No Bot Developers Found!")
      await working_lister(listxd=loda, color=0x2f3136, title=f"LIST OF DEVELOPER(S) IN {ctx.guild.name} - {int(len(loda))}", ctx=ctx)
   
    @__list_.command(name="inrole", aliases=["inside-role"],description="See a list of members that are in the seperate role")
    @ignore_check()
    async def list_inrole(self, ctx, *,role: discord.Role):
      l = list(role.members)
    
      await working_lister(ctx=ctx, listxd=l, color=0x2f3136, title=f"List of members in {role.name} - {int(len(l))}")
      
                          
    @__list_.command(name="bans", aliases=["ban"],description="See a list of banned user")
    @ignore_check()
    async def list_bans(self, ctx):
      ok = []
      async for idk in ctx.guild.bans(limit=None):
        ok.append(idk)
      await lister_bn(ctx=ctx, listxd=ok, color=0x2f3136, title=f" LIST OF BANNED MEMBERS IN {ctx.guild.name} - {len(ok)}")
           
    
    @__list_.command(name="roles", aliases=["role"],description="See a list of roles in the server")
    @ignore_check()
    async def list_roles(self, ctx):
      l = [r for r in ctx.guild.roles if not r.id == ctx.guild.default_role.id]
      l.reverse()
      await rolis(ctx=ctx, listxd=l, color=0x2f3136, title=f"List of Roles in {ctx.guild.name} - {int(len(l))}")

    
    @__list_.command(name="invc",aliases=["vc","in-vc"],description="See a list of members in a vc")
    @ignore_check()
    async def vclist(self,ctx):
        if not ctx.message.author.voice:
            await ctx.send("❌ | You are not connected to any voice channels")
        else:
            member_list = ctx.message.author.voice.channel.members
            color = 0x2f3136
            await lister(ctx,your_list=member_list,color=color,title=f"List of members in {ctx.message.author.voice.channel.name}")

    @__list_.command(name="activedevs",aliases=["activedev"],description="Get a list of active developer id in a server")
    @ignore_check()
    async def activedeveloper(self, ctx):
      loda = []
      for member in ctx.guild.members:
        if member.public_flags.active_developer:
          loda.append(member)
      
      await working_lister(listxd=loda, color=0x2f3136, title=f" ACTIVE DEVELOPERS ID'S IN {ctx.guild.name} - {int(len(loda))}", ctx=ctx)
async def setup(bot):           
 await bot.add_cog(utility5(bot))