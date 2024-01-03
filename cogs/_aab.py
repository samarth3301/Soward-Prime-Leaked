import discord
from discord.ext import commands
import json
from prince1.Tools import *
#from core.Context import *
import datetime 
class roless(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        guild = discord.Guild

    
    
    

    

  



     

   

        
    

         
            
    

    @commands.command()
   # @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @blacklist_check()
    @ignore_check()
    async def friend(self, ctx, mem:discord.Member=None):
        with open("reqrole.json", "r") as f:

                op = json.load(f)

                if f'{ctx.guild.id}' not in op:

                  return await ctx.send(embed=discord.Embed(description="<:cross1:1110685242278297600> | There is no **Required Role** for **Custom Roles** Use **setup reqrole**",color=0x2f3136))

                elif f'{ctx.guild.id}' in op:

                  for S in op[str(ctx.guild.id)]:

                    P = discord.utils.get(ctx.guild.roles,id=int(S))

                    if P not in ctx.author.roles:

                      await ctx.send(embed=discord.Embed(description=f"<:cross1:1110685242278297600> | You must have {P.mention} to add roles to people", color=0x2f3136))

                      return

                  else:
                      with open("friends.json", 'r') as f:

                        key = json.load(f)

                        if f'{ctx.guild.id}' not in key:

                          await ctx.reply(embed=discord.Embed(title="Friends role is not set!", color=000000))

                        elif f'{ctx.guild.id}' in key:

                          for idk in key[str(ctx.guild.id)]:

                            r = discord.utils.get(ctx.guild.roles, id=int(idk))

                            if r in mem.roles:

                              await mem.remove_roles(r)
                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully removed {r.mention} To {mem.mention}', color=0x2f3136)
                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)
                              embed.set_thumbnail(url=ctx.author.display_avatar)
                              await ctx.reply(embed=embed)
                               
                                

                            elif r not in mem.roles:

                              await mem.add_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Given {r.mention} To {mem.mention}', color=0x2f3136)
                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)
                              embed.set_thumbnail(url=ctx.author.display_avatar)
                              await ctx.reply(embed=embed)
                        
                                        
                                        
                                        
                                  
                                
                                
                                
                                
                                
                                
                                
                               
                              

                       

       
        
                

                

                
                

               

                

                        

                               
                                
                                                                           

                                        
                
                              
                

                    


    @commands.command()
 #   @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @blacklist_check()
    @ignore_check()
    async def guest(self,ctx, mem:discord.Member=None):
        with open("reqrole.json", "r") as f:

             op = json.load(f)

             if f'{ctx.guild.id}' not in op:

                    return await ctx.send(embed=discord.Embed(description="<:cross1:1110685242278297600> | There is no **Required Role** for **Custom Roles** Use **setup reqrole**",color=0x2f3136))

             elif f'{ctx.guild.id}' in op:

               for S in op[str(ctx.guild.id)]:

                 P = discord.utils.get(ctx.guild.roles,id=int(S))

                 if P not in ctx.author.roles:

                   await ctx.send(embed=discord.Embed(description=f"<:cross1:1110685242278297600> | You must have {P.mention} to add roles to people", color=0x2f3136))

                   return

               else:
                   with open("guest.json", 'r') as f:

                        key = json.load(f)

                        if f'{ctx.guild.id}' not in key:

                          await ctx.reply(embed=discord.Embed(title="Guest role is not set!", color=000000))

                        elif f'{ctx.guild.id}' in key:

                          for idk in key[str(ctx.guild.id)]:

                            r = discord.utils.get(ctx.guild.roles, id=int(idk))

                            if r in mem.roles:

                              await mem.remove_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully removed {r.mention} From {mem.mention}', color=0x2f3136)

                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                              embed.set_thumbnail(url=ctx.author.display_avatar)

                              await ctx.reply(embed=embed)

                               

                                

                            elif r not in mem.roles:

                              await mem.add_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Given {r.mention} To {mem.mention}', color=0x2f3136)

                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                              embed.set_thumbnail(url=ctx.author.display_avatar)

                              await ctx.reply(embed=embed)

                                    

                                    

                                    



    @commands.command(aliases=["staff"])
   # @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @blacklist_check()
    @ignore_check()
    async def official(self, ctx, mem:discord.Member=None):
        with open("reqrole.json", "r") as f:

            op = json.load(f)

            if f'{ctx.guild.id}' not in op:

                return await ctx.send(embed=discord.Embed(description="<:cross1:1110685242278297600> | There is no **Required Role** for **Custom Roles** Use **setup reqrole**",color=0x2f3136))

            elif f'{ctx.guild.id}' in op:

              for S in op[str(ctx.guild.id)]:

                P = discord.utils.get(ctx.guild.roles,id=int(S))

            if P not in ctx.author.roles:

                await ctx.send(embed=discord.Embed(description=f"<:cross1:1110685242278297600> | You must have {P.mention} to add roles to people", color=0x2f3136))

                return

            else:
                with open("official.json", 'r') as f:

                        key = json.load(f)

                        if f'{ctx.guild.id}' not in key:

                          await ctx.reply(embed=discord.Embed(title="Staff role is not set!", color=000000))

                        elif f'{ctx.guild.id}' in key:

                          for idk in key[str(ctx.guild.id)]:

                            r = discord.utils.get(ctx.guild.roles, id=int(idk))

                            if r in mem.roles:

                              await mem.remove_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully removed {r.mention} From {mem.mention}', color=0x2f3136)

                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                              embed.set_thumbnail(url=ctx.author.display_avatar)

                              await ctx.reply(embed=embed)

                               

                                

                            elif r not in mem.roles:

                              await mem.add_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Given {r.mention} To {mem.mention}', color=0x2f3136)

                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                              embed.set_thumbnail(url=ctx.author.display_avatar)

                              await ctx.reply(embed=embed)

                                   



 
    @commands.command(aliases=["qt"])
   # @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @blacklist_check()
    @ignore_check()
    async def girl(self, ctx, mem:discord.Member=None):
        with open("reqrole.json", "r") as f:

            op = json.load(f)

            if f'{ctx.guild.id}' not in op:

                return await ctx.send(embed=discord.Embed(description="<:cross1:1110685242278297600> | There is no **Required Role** for **Custom Roles** Use **setup reqrole**",color=0x2f3136))

            elif f'{ctx.guild.id}' in op:

              for S in op[str(ctx.guild.id)]:

                P = discord.utils.get(ctx.guild.roles,id=int(S))

            if P not in ctx.author.roles:

                await ctx.send(embed=discord.Embed(description=f"<:cross1:1110685242278297600> | You must have {P.mention} to add roles to people", color=0x2f3136))

                return
            else:
                

                with open("girl.json", 'r') as f:

                        key = json.load(f)

                        if f'{ctx.guild.id}' not in key:

                          await ctx.reply(embed=discord.Embed(title="Girls role is not set!", color=000000))

                        elif f'{ctx.guild.id}' in key:

                          for idk in key[str(ctx.guild.id)]:

                            r = discord.utils.get(ctx.guild.roles, id=int(idk))

                            if r in mem.roles:

                              await mem.remove_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully removed {r.mention} From {mem.mention}', color=0x2f3136)

                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                              embed.set_thumbnail(url=ctx.author.display_avatar)

                              await ctx.reply(embed=embed)

                               

                                

                            elif r not in mem.roles:

                              await mem.add_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Given {r.mention} To {mem.mention}', color=0x2f3136)

                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                              embed.set_thumbnail(url=ctx.author.display_avatar)

                              await ctx.reply(embed=embed)
                    

                
                

                    

                        

                                 

                                    

        
                            

                                    
                                    

                                    
                                    

                                    

    

    @commands.command()
   # @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @blacklist_check()
    @ignore_check()
    async def vip(self, ctx, mem:discord.Member=None):
        with open("reqrole.json", "r") as f:

                op = json.load(f)

                if f'{ctx.guild.id}' not in op:

                  return await ctx.send(embed=discord.Embed(description="<:cross1:1110685242278297600> | There is no **Required Role** for **Custom Roles** Use **setup reqrole**",color=0x2f3136))

                elif f'{ctx.guild.id}' in op:

                  for S in op[str(ctx.guild.id)]:

                    P = discord.utils.get(ctx.guild.roles,id=int(S))

                    if P not in ctx.author.roles:

                      await ctx.send(embed=discord.Embed(description=f"<:cross1:1110685242278297600> | You must have {P.mention} to add roles to people", color=0x2f3136))

                      return

                  else:
                      

                      with open("vip.json", 'r') as f:

                        key = json.load(f)

                        if f'{ctx.guild.id}' not in key:

                          await ctx.reply(embed=discord.Embed(title="Vip role is not set!", color=000000))

                        elif f'{ctx.guild.id}' in key:

                          for idk in key[str(ctx.guild.id)]:

                            r = discord.utils.get(ctx.guild.roles, id=int(idk))

                            if r in mem.roles:

                              await mem.remove_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully removed {r.mention} From {mem.mention}', color=0x2f3136)

                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                              embed.set_thumbnail(url=ctx.author.display_avatar)

                              await ctx.reply(embed=embed)

                               

                                

                            elif r not in mem.roles:

                              await mem.add_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Given {r.mention} To {mem.mention}', color=0x2f3136)

                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                              embed.set_thumbnail(url=ctx.author.display_avatar)

                              await ctx.reply(embed=embed)
                      

                            

                            

                                    

                                    

                                    
    
                                    

                                    

                                    

                                    

    @commands.command(aliases=["rstaff"])
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @blacklist_check()
    @ignore_check()
    async def rofficial(self, ctx, mem:discord.Member=None):
            with open("official.json", 'r') as f:
                    key = json.load(f)
                    if f'{ctx.guild.id}' not in key:
                            await ctx.reply(embed=discord.Embed(title="Official role is not set!", color=000000))
                    elif f'{ctx.guild.id}' in key:
                            for idk in key[str(ctx.guild.id)]:
                                    r = discord.utils.get(ctx.guild.roles, id=int(idk))
                                    await mem.remove_roles(r)
                                    embed = discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Removed {r.mention} from {mem.mention}', color=0x2f3136)
                                    embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)
                                    embed.set_thumbnail(url=ctx.author.display_avatar)
                                    await ctx.reply(embed=embed)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    @ignore_check()
    async def rfriend(self, ctx, mem:discord.Member=None):
            with open("friends.json", 'r') as f:
                    key = json.load(f)
                    if f'{ctx.guild.id}' not in key:
                            await ctx.reply(embed=discord.Embed(title="Friends role is not set!", color=000000))
                    elif f'{ctx.guild.id}' in key:
                            for idk in key[str(ctx.guild.id)]:
                                    r = discord.utils.get(ctx.guild.roles, id=int(idk))
                                    await mem.remove_roles(r)
                                    embed = discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Removed {r.mention} from {mem.mention}', color=0x2f3136)

                                    embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                                    embed.set_thumbnail(url=ctx.author.display_avatar)

                                    await ctx.reply(embed=embed)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    @ignore_check()
    async def rguest(self, ctx, mem:discord.Member=None):
            with open("guest.json", 'r') as f:
                    key = json.load(f)
                    if f'{ctx.guild.id}' not in key:
                            await ctx.send(embed=discord.Embed(title="Guest role is not set!", color=000000))
                    elif f'{ctx.guild.id}' in key:
                            for idk in key[str(ctx.guild.id)]:
                                    r = discord.utils.get(ctx.guild.roles, id=int(idk))
                                    await mem.remove_roles(r)
                                    embed = discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Removed {r.mention} from {mem.mention}', color=0x2f3136)

                                    embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                                    embed.set_thumbnail(url=ctx.author.display_avatar)

                                    await ctx.reply(embed=embed)

    @commands.command(aliases=["rqt"])
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @blacklist_check()
    @ignore_check()
    async def rgirl(self, ctx, mem:discord.Member=None):
            with open("girl.json", 'r') as f:
                    key = json.load(f)
                    if f'{ctx.guild.id}' not in key:
                            await ctx.send(embed=discord.Embed(title="Girls role is not set!", color=000000))
                    elif f'{ctx.guild.id}' in key:
                            for idk in key[str(ctx.guild.id)]:
                                    r = discord.utils.get(ctx.guild.roles, id=int(idk))
                                    await mem.remove_roles(r)
                                    embed = discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Removed {r.mention} from {mem.mention}', color=0x2f3136)

                                    embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                                    embed.set_thumbnail(url=ctx.author.display_avatar)

                                    await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @blacklist_check()
    @ignore_check()
    async def rvip(self, ctx, mem:discord.Member=None):
            with open("vip.json", 'r') as f:
                    key = json.load(f)
                    if f'{ctx.guild.id}' not in key:
                            await ctx.send(embed=discord.Embed(title="Vip role is not set!", color=000000))
                    elif f'{ctx.guild.id}' in key:
                            for idk in key[str(ctx.guild.id)]:
                                    r = discord.utils.get(ctx.guild.roles, id=int(idk))
                                    await mem.remove_roles(r)
                                    embed = discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Removed {r.mention} from {mem.mention}', color=0x2f3136)

                                    embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                                    embed.set_thumbnail(url=ctx.author.display_avatar)

                                    await ctx.reply(embed=embed)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    @ignore_check()
    async def rbot(self, ctx, mem:discord.Member=None):
            with open("bot.json", 'r') as f:
                    key = json.load(f)
                    if f'{ctx.guild.id}' not in key:
                            await ctx.send(embed=discord.Embed(title="bot role is not set!", color=000000))
                    elif f'{ctx.guild.id}' in key:
                            for idk in key[str(ctx.guild.id)]:
                                    r = discord.utils.get(ctx.guild.roles, id=int(idk))
                                    await mem.remove_roles(r)
                                    embed = discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Removed {r.mention} from {mem.mention}', color=0x2f3136)

                                    embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                                    embed.set_thumbnail(url=ctx.author.display_avatar)

                                    await ctx.reply(embed=embed)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    @ignore_check()
    async def rartist(self, ctx, mem:discord.Member=None):
            with open("artist.json", 'r') as f:
                    key = json.load(f)
                    if f'{ctx.guild.id}' not in key:
                            await ctx.send(embed=discord.Embed(title="artist role is not set!", color=000000))
                    elif f'{ctx.guild.id}' in key:
                            for idk in key[str(ctx.guild.id)]:
                                    r = discord.utils.get(ctx.guild.roles, id=int(idk))
                                    await mem.remove_roles(r)
                                    embed = discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Removed {r.mention} from {mem.mention}', color=0x2f3136)

                                    embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                                    embed.set_thumbnail(url=ctx.author.display_avatar)

                                    await ctx.reply(embed=embed)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    async def rmod(self, ctx, mem:discord.Member=None):
            with open("mod.json", 'r') as f:
                    key = json.load(f)
                    if f'{ctx.guild.id}' not in key:
                            await ctx.send(embed=discord.Embed(title="Mod role is not set!", color=000000))
                    elif f'{ctx.guild.id}' in key:
                            for idk in key[str(ctx.guild.id)]:
                                    r = discord.utils.get(ctx.guild.roles, id=int(idk))
                                    await mem.remove_roles(r)
                                                            


    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    @ignore_check()
   # @commands.has_permissions(administrator=True)
    async def bots(self,ctx, mem:discord.Member=None):
        with open("reqrole.json", "r") as f:

                op = json.load(f)

                if f'{ctx.guild.id}' not in op:

                  return await ctx.send(embed=discord.Embed(description="<:cross1:1110685242278297600> | There is no **Required Role** for **Custom Roles** Use **setup reqrole**",color=0x2f3136))

                elif f'{ctx.guild.id}' in op:

                  for S in op[str(ctx.guild.id)]:

                    P = discord.utils.get(ctx.guild.roles,id=int(S))

                    if P not in ctx.author.roles:

                      await ctx.send(embed=discord.Embed(description=f"<:cross1:1110685242278297600> | You must have {P.mention} to add roles to people", color=0x2f3136))

                      return

                  else:
                      

                      with open("bot.json", 'r') as f:

                        key = json.load(f)

                        if f'{ctx.guild.id}' not in key:

                          await ctx.reply(embed=discord.Embed(title="Bots role is not set!", color=000000))

                        elif f'{ctx.guild.id}' in key:

                          for idk in key[str(ctx.guild.id)]:

                            r = discord.utils.get(ctx.guild.roles, id=int(idk))

                            if r in mem.roles:

                              await mem.remove_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully removed {r.mention} From {mem.mention}', color=0x2f3136)

                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                              embed.set_thumbnail(url=ctx.author.display_avatar)

                              await ctx.reply(embed=embed)

                               

                                

                            elif r not in mem.roles:

                              await mem.add_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Given {r.mention} To {mem.mention}', color=0x2f3136)

                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                              embed.set_thumbnail(url=ctx.author.display_avatar)

                              await ctx.reply(embed=embed)
                      
                            

                            

                                    

                                    

                                    

                                    
                
                                
                                
                                
                                



                                    

                                  

 
    
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    @ignore_check()
   # @commands.has_permissions(administrator=True)
    async def mod(self,ctx, mem:discord.Member=None):
        with open("reqrole.json", "r") as f:

                op = json.load(f)

                if f'{ctx.guild.id}' not in op:

                  return await ctx.send(embed=discord.Embed(description="<:cross1:1110685242278297600> | There is no **Required Role** for **Custom Roles** Use **setup reqrole**",color=0x2f3136))

                elif f'{ctx.guild.id}' in op:

                  for S in op[str(ctx.guild.id)]:

                    P = discord.utils.get(ctx.guild.roles,id=int(S))

                    if P not in ctx.author.roles:

                      await ctx.send(embed=discord.Embed(description=f"<:cross1:1110685242278297600> | You must have {P.mention} to add roles to people", color=0x2f3136))

                      return

                  else:
                      

                      with open("mod.json", 'r') as f:

                        key = json.load(f)

                        if f'{ctx.guild.id}' not in key:

                          await ctx.reply(embed=discord.Embed(title="mod role is not set!", color=000000))

                        elif f'{ctx.guild.id}' in key:

                          for idk in key[str(ctx.guild.id)]:

                            r = discord.utils.get(ctx.guild.roles, id=int(idk))

                            if r in mem.roles:

                              await mem.remove_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully removed {r.mention} From {mem.mention}', color=0x2f3136)

                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                              embed.set_thumbnail(url=ctx.author.display_avatar)

                              await ctx.reply(embed=embed)

                               

                                

                            elif r not in mem.roles:

                              await mem.add_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Given {r.mention} To {mem.mention}', color=0x2f3136)

                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                              embed.set_thumbnail(url=ctx.author.display_avatar)

                              await ctx.reply(embed=embed)
                     

                        

                                    

                                    

                                    

                                    

                                    

                                    
                                
                               
                                                                    

                                    


                                   # await ctx.reply(embed=embed)



    @commands.command()
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    @ignore_check()
    async def arthhggist(ctx, mem:discord.Member=None):
            with open("artist.json", 'r') as f:
                    key = json.load(f)
                    if f'{ctx.guild.id}' not in key:
                            await ctx.reply(embed=discord.Embed(title="Artist role is not set!", color=000000))
                    elif f'{ctx.guild.id}' in key:
                            for idk in key[str(ctx.guild.id)]:
                                    r = discord.utils.get(ctx.guild.roles, id=int(idk))
                                    await mem.add_roles(r)
                                    await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Added {r.mention} To {mem.mention}', color=000000))

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
   # @commands.has_permissions(administrator=True)
    @blacklist_check()
    @ignore_check()
    async def artist(self, ctx, mem:discord.Member=None):
        with open("reqrole.json", "r") as f:

                op = json.load(f)

                if f'{ctx.guild.id}' not in op:

                  return await ctx.send(embed=discord.Embed(description="<:cross1:1110685242278297600> | There is no **Required Role** for **Custom Roles** Use **setup reqrole**",color=0x2f3136))

                elif f'{ctx.guild.id}' in op:

                  for S in op[str(ctx.guild.id)]:

                    P = discord.utils.get(ctx.guild.roles,id=int(S))

                    if P not in ctx.author.roles:

                      await ctx.send(embed=discord.Embed(description=f"<:cross1:1110685242278297600> | You must have {P.mention} to add roles to people", color=0x2f3136))

                      return

                  else:
                      

                      with open("artist.json", 'r') as f:

                        key = json.load(f)

                        if f'{ctx.guild.id}' not in key:

                          await ctx.reply(embed=discord.Embed(title="Artist role is not set!", color=000000))

                        elif f'{ctx.guild.id}' in key:

                          for idk in key[str(ctx.guild.id)]:

                            r = discord.utils.get(ctx.guild.roles, id=int(idk))

                            if r in mem.roles:

                              await mem.remove_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully removed {r.mention} From {mem.mention}', color=0x2f3136)

                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                              embed.set_thumbnail(url=ctx.author.display_avatar)

                              await ctx.reply(embed=embed)

                               

                                

                            elif r not in mem.roles:

                              await mem.add_roles(r)

                              embed= discord.Embed(description=f'<:ri8:1038487759750438912> Successfully Given {r.mention} To {mem.mention}', color=0x2f3136)

                              embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)

                              embed.set_thumbnail(url=ctx.author.display_avatar)

                              await ctx.reply(embed=embed)
                      

                            

                            
                                 

                                    

                                    
                                    

                                    

                                    
                          

        

    @commands.command(aliases=["setup-buyer"], usage="$setupp <role>", help="set participants role")
    @blacklist_check()
    @ignore_check()
    
    @commands.has_permissions(administrator=True)
    async def sethahaup(self, ctx, role:discord.Role=None):
            with open('participate.json', 'r', encoding='utf-8') as f:
                    key = json.load(f)
                    key[str(ctx.guild.id)] = [str(role.id)]
                    with open('participate.json', 'w', encoding='utf-8') as f:
                            json.dump(key, f, indent=4)
                            await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated Participants Role To {role.mention}", color=000000))

    @commands.command()
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    @ignore_check()
    async def buyejehjer(self, ctx, mem:discord.Member=None):
            with open("participate.json", 'r') as f:
                    key = json.load(f)
                    if f'{ctx.guild.id}' not in key:
                            await ctx.reply(embed=discord.Embed(title="Participants role is not set!", color=000000))
                    elif f'{ctx.guild.id}' in key:
                            for idk in key[str(ctx.guild.id)]:
                                    r = discord.utils.get(ctx.guild.roles, id=int(idk))
                                    await mem.add_roles(r)
                                    await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Added {r.mention} To {mem.mention}', color=000000))

async def setup(bot):
    await bot.add_cog(roless(bot))