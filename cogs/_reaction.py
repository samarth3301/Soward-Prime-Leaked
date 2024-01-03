import discord
from discord.ext import commands
import json
from prince1.Tools import*
#from prince.custom_checks import voter_only
from discord.ui import *
class autoreaction(commands.Cog,name="reactions"):
  def __init__(self, client):
    self.client = client

  

  @commands.group(description='show the help menu of auto reaction')
    
  async def reaction(self, ctx):
        ...        
   
  
  @reaction.command(description='count all auto reaction of server')
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.has_permissions(administrator=True)
  @blacklist_check()
 # @voter_only()
  async def show(self, ctx):
        with open("reaction.json", "r") as f:
            autoresponse = json.load(f)
        autoresponsenames = []
        if str(ctx.guild.id) in autoresponse:
            for autoresponsecount in autoresponse[str(ctx.guild.id)]:
              autoresponsenames.append(autoresponsecount)
            embed = discord.Embed(color=0x2f3136)
            st, count = "", 1
            for autoresponse in autoresponsenames:
                    st += f"*[ {'0' + str(count) if count < 10 else count} ]* Name -> {autoresponse}\n"
                    test = count
                    count += 1
            embed.title = f" auto reaction for {ctx.guild} - {test}"
        embed.description = st
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
        embed.set_footer(text="Made By Prince", icon_url=self.client.user.avatar)
        embed.set_thumbnail(url=self.client.user.avatar)
        await ctx.reply(embed=embed)

  
  @reaction.command(help="add message reaction",aliases=["add","create"], usage="reaction add <name> <emoji>")
  @commands.cooldown(1, 2, commands.BucketType.user)      
  @commands.has_permissions(administrator=True)
  @blacklist_check()
  async def reaction_create(self, ctx, name , *, message):
    
    with open("reaction.json", "r") as f:
        rxn = json.load(f)
        numbers = []
      
    if str(ctx.guild.id) in rxn:
        for rxncount in rxn[str(ctx.guild.id)]:
          numbers.append(rxncount)
    with open ("premium.json","r") as f:

        member = json.load(f)

        prm = member["guild"]
        if len(numbers) >= 5:
            if str(ctx.guild.id) not in prm:
                embed = discord.Embed(title="This Server Reached Maximum Auto reactions  Which Is (5) Buy Premium for Add More",color=0x2f3136)
                embed.set_thumbnail(url=self.client.user.avatar)
                embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)
                embed.set_footer(text="Made By Prince",icon_url=self.client.user.avatar)
                B = Button(label='Get Premium',emoji="<a:Diamonds:1087431201117179944>" ,style=discord.ButtonStyle.link,url='https://discord.gg/soward')
                view = View()

                view.add_item(B)

                return await ctx.send(embed=embed,view=view)

                

                

                

                

                
                
    if str(ctx.guild.id) in rxn:
        if name in rxn[str(ctx.guild.id)]:
                return await ctx.send(embed=discord.Embed(title=f' The reaction `{name}` is already in the server', color=0x2f3136))
    if str(ctx.guild.id) in rxn:
          rxn[str(ctx.guild.id)][name] = message
    with open("reaction.json", "w") as f:
            json.dump(rxn, f, indent=4)
            return await ctx.reply(embed=discord.Embed(title=f'Created a reaction with the name : `{name}`', color=0x2f3136))

    data = {
            name : message,
        }
    rxn[str(ctx.guild.id)] = data

    with open("reaction.json", "w") as f:
        json.dump(rxn, f, indent=4)
        return await ctx.reply(embed=discord.Embed(title=f' Created a reaction with the name : `{name}`', color=0x2f3136))

  @reaction.command(help="delete auto reaction ",aliases=["del","delete"], usage="reaction delete <name>")
  @commands.cooldown(1, 5, commands.BucketType.user)    
  @commands.has_permissions(administrator=True)
  async def autoreaction_delete(self, ctx, name):
      with open("reaction.json", "r") as f:
        rxn = json.load(f)
            
      if str(ctx.guild.id) in rxn:
            if name in rxn[str(ctx.guild.id)]:
                del rxn[str(ctx.guild.id)][name]
                with open("reaction.json", "w") as f:
                    json.dump(rxn, f, indent=4)
                return await ctx.reply(embed=discord.Embed(title=f'Deleted the `{name}` auto reaction in the server', color=0x2f3136))
            else:
                return await ctx.reply(embed=discord.Embed(title=f'No auto reaction found with the name `{name}`', color=0x2f3136))
      else:
            return await ctx.reply(embed=discord.Embed(title=f'There is no auto reaction in the server', color=0x2f3136))

  @reaction.command(help="edit Auto reaction",aliases=["edit"], usage="reaction edit <name> <new reaction>")
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.has_permissions(administrator=True)
  async def autoreaction_edit(self, ctx, name , *, message):
      with open("reaction.json", "r") as f:
          autoresponse = json.load(f)
      if str(ctx.guild.id) in autoresponse:
          if name in autoresponse[str(ctx.guild.id)]:
              autoresponse[str(ctx.guild.id)][name] = message
              with open("reaction.json", "w") as f:
                    json.dump(autoresponse, f, indent=4)
              return await ctx.send(embed=discord.Embed(title=f'Edited the `{name}` autoresponse', color=0x2f3136))
      else:
          return await ctx.send(embed=discord.Embed(title=f'There is no autoresponses in the server',color=0x2f3136)) 




async def setup(client):
    await client.add_cog(autoreaction(client))