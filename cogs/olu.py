from __future__ import annotations
from discord.ext import commands
from prince1.Tools import *
from discord import *
#from utils.config import OWNER_IDS, No_Prefix
import json, discord
import typing
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator
from utils.Tools import *
from typing import Optional

#Cyg90MAh7a0
class nop(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.loda = [1090957904410071120,1068967045263261746]


    

                
                
    

            

    @commands.group(
        name="np",
        help="Allows you to add someone in no prefix "
    )
 #   @commands.is_owner()
    async def _np(self, ctx):
        pass
        
            

    @_np.command(name="list")
    @commands.is_owner()
    async def np_list(self, ctx):
        with open("nonprefix.json") as f:
            np = json.load(f)
            nplist = np["np"]
            npl = ([await self.client.fetch_user(nplu) for nplu in nplist])
            npl = sorted(npl, key=lambda nop: nop.created_at)
            entries = [
                f"`[{no}]` | [{mem}](https://discord.com/users/{mem.id}) (ID: {mem.id})"
                for no, mem in enumerate(npl, start=1)
            ]
            paginator = Paginator(source=DescriptionEmbedPaginator(
                entries=entries,
                title=f"No Prefix list of Soward Prime - {len(nplist)}",
                description="",
                per_page=10,
                color=0x2f3136),
                                  ctx=ctx)
            await paginator.paginate()

    @_np.command(name="add", help="Add user to no prefix")
    
    async def np_add(self, ctx, user: discord.User):
        with open('nonprefix.json', 'r') as idk:
            if ctx.author.id not in self.loda:
                await ctx.send("you dont have access")
                return



            data = json.load(idk)
        np = data["np"]
        if user.id in np:
            embed = discord.Embed(
                description=
                "**<:Wrong:1017402708703064144> | The mentioned Member is already added**",
                color=0x2f3136)
            await ctx.reply(embed=embed)
            return
        else:
            data["np"].append(user.id)
        with open('nonprefix.json', 'w') as idk:
            json.dump(data, idk, indent=4)
            embed1 = discord.Embed(
                description=
                f"<:Icons_correct:1017402689027592222> | Successfully added {user.mention} to nonprefix",
                color=0x2f3136)
           # embed1.set_thumbnail(url=f"{self.client.user.display_avatar.url}")
            await ctx.reply(embed=embed1)

    @_np.command(name="remove", help="Remove user from no prefix")
    
    async def np_remove(self, ctx, user: discord.User):
        with open('nonprefix.json', 'r') as idk:
            if ctx.author.id not in self.loda:
                await ctx.send("you dont have access")
                return
            data = json.load(idk)
        np = data["np"]
        if user.id not in np:
            embed = discord.Embed(
                description="**{} is not in nonprefix!**".format(user),
                color=0x2f3136)
            await ctx.reply(embed=embed)
            return
        else:
            data["np"].remove(user.id)
        with open('nonprefix.json', 'w') as idk:
            json.dump(data, idk, indent=4)
            embed2 = discord.Embed(
                description=
                f"<:Icons_correct:1017402689027592222> | **Removed {user.mention} from nonprefix **",
                color=0x2f3136)

            await ctx.reply(embed=embed2)

    
            
            
    @commands.hybrid_command(
        name="prefix",
        aliases=["setprefix", "prefixset"],
        help="Allows you to change prefix of the bot for this server")
    @blacklist_check()
   # @ignore_check()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def _prefix(self, ctx: commands.Context, prefix):
        data = getpre(ctx.guild.id)
        data["prefix"] = str(prefix)
        updatepre(ctx.guild.id, data)
        await ctx.reply(embed=discord.Embed(
            description=
            f"<:Icons_correct:1017402689027592222> | Successfully Update Prefix to {prefix}`\nUse `{prefix}help` For More info .",
            color=0x2f3136))


              
                 
            
                
                
                
            

    
            
            
                
            
            
        

               



    
    



    
async def setup(bot):
	await bot.add_cog(nop(bot))