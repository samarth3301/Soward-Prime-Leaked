import discord
from discord.ext import commands
from disputils import BotEmbedPaginator
import math
#from cogs.utils.color import fetch_color
from reactionmenu import ViewMenu, ViewButton

class PaginationView:
  def __init__(self, embed_list, ctx):
    self.elist = embed_list
    self.context = ctx

  async def start(self, ctx):
    menu = ViewMenu(ctx, menu_type=ViewMenu.TypeEmbed)
    for xem in self.elist:
      menu.add_page(xem)
    bax = ViewButton(style=discord.ButtonStyle.secondary, label=None,emoji='⏪', custom_id=ViewButton.ID_PREVIOUS_PAGE)
    menu.add_button(bax)
    bax2 = ViewButton(style=discord.ButtonStyle.secondary, label=None,emoji='⏹️', custom_id=ViewButton.ID_END_SESSION)
    menu.add_button(bax2)
    bax3 = ViewButton(style=discord.ButtonStyle.secondary, label=None,emoji='⏩', custom_id=ViewButton.ID_NEXT_PAGE)
    menu.add_button(bax3)
    await menu.start()

async def lister(ctx,your_list,color,*,title):
    pages = math.ceil(len(your_list)/15)
    page = [i for i in range(1,pages+1)]
    counts = []
    first_num = 0
    for i in page:
        if first_num == 0:
            last_num = (i*15) -1
        else:
            last_num = (i*15) -1
        if first_num > len(your_list):
            first_num = len(your_list)
        elif last_num > len(your_list):
            last_num = len(your_list)
        l = [first_num,last_num]
        counts.append(l)
        if last_num == len(your_list) or first_num == len(your_list):
            break
        first_num = last_num + 1
                        
    embeds = []
    
    for l in counts:
        first_num = l[0]
        last_num = l[1]
        em = discord.Embed(description=" ",color=color).add_field(name=f"{title} - {len(your_list)}",value="\n".join(f"`[{count+1}]` | {your_list[count-1]} {your_list[count-1].mention}" for count in range(first_num,last_num)))
        embeds.append(em)
    if len(embeds) == 1:
      await ctx.send(embed=embeds[0])
    else:
      paginator = PaginationView(embeds, ctx)
      await paginator.start(ctx)

async def lister_ban(ctx,your_list,color,*,title):
    pages = math.ceil(len(your_list)/15)
    page = [i for i in range(1,pages+1)]
    counts = []
    first_num = 0
    for i in page:
        if first_num == 0:
            last_num = (i*15) -1
        else:
            last_num = (i*15) -1
        if first_num > len(your_list):
            first_num = len(your_list)
        elif last_num > len(your_list):
            last_num = len(your_list)
        l = [first_num,last_num]
        counts.append(l)
        if last_num == len(your_list) or first_num == len(your_list):
            break
        first_num = last_num + 1
                        
    embeds = []
    
    for l in counts:
        first_num = l[0]
        last_num = l[1]
        em = discord.Embed(description=" ",color=color).add_field(name=f"{title} - {len(your_list)}",value="\n".join(f"`[{count+1}]` | {your_list[count]}" if count == 0 else f"`[{count}]` | {your_list[count]}" for count in range(first_num,last_num)))
        embeds.append(em)
    if len(embeds) == 1:
      await ctx.send(embed=embeds[0])
    else:
      paginator = PaginationView(embeds, ctx)
      await paginator.start(ctx)


async def lister_str(ctx, your_list, color, *, title) -> None:
    pages = math.ceil(len(your_list) / 20)
    page = [i for i in range(1, pages + 1)]
    counts = []
    first_num = 0
    for i in page:
        if first_num == 0:
            last_num = (i * 20) - 1
        else:
            last_num = (i * 20) - 1
        if first_num > len(your_list):
            first_num = len(your_list)
        elif last_num > len(your_list):
            last_num = len(your_list)
        l = [first_num, last_num]
        counts.append(l)
        if last_num == len(your_list) or first_num == len(your_list):
            break
        first_num = last_num + 1

    embeds = []

    for l in counts:
        first_num = l[0]
        last_num = l[1]
        em = discord.Embed(description=" ", color=color).add_field(name=f"{title} - [{len(your_list)}]",
                                                                   value="\n".join(
                                                                       f"`[{count + 1}]` {your_list[count]}" for
                                                                       count in range(first_num, last_num)))
        embeds.append(em)

    if len(embeds) == 1:
      await ctx.send(embed=embeds[0])
    else:
      paginator = PaginationView(embeds, ctx)
      await paginator.start(ctx)