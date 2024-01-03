import discord
import os
import asyncio
from discord.ext import commands
import humanfriendly
import datetime
from discord.ext import commands
import aiohttp
from io import BytesIO
from prince1.Tools import*
from prince.bot import Bot


class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.tasks = []

    @commands.command(aliases=['sb'], usage="$softban <member>", help="Soft bans a member from the server.A softban is basically banning the member from the server but then unbanning the member as well.")
    @blacklist_check()
    @ignore_check()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def softban(self, ctx, member: discord.Member, *, reason=None):
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
            await ctx.reply(embed=discord.Embed(title=""""```diff\n - You must have Administrator permission.\n - Your top role should be above my top role. \n```""", color=0x2f3136))
        else:
            if reason is None:
                reason = f" No reason given.\nBanned by "
                await member.ban(reason=reason)
                await member.send(f"you have been banned from {ctx.guild.name} for {reason} by {ctx.author} ")
                await member.unban(reason=reason)
                await ctx.send(embed=discord.Embed(title=f" Sucessfully soft-banned {member}.", color=0x2f3136))

    @commands.command(aliases=['tb'])
    @commands.guild_only()
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tempban(self, ctx, member: discord.Member, time, d, *, reason="No Reason"):
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
            await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
            await ctx.reply(embed=embed)
        else:
            guild = ctx.guild
            embed = discord.Embed(title="Temporarily banned", description=f" {member.mention} has been temporarily banned!", color=0x2f3136, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Reason: ", value=reason, inline=False)
            embed.add_field(name="Time left for the ban:", value=f"{time}{d}", inline=False)
            await ctx.reply(embed=embed)
            await member.send(f'you have been temp banned from {guild} for {reason} by {ctx.author}')
            await guild.ban(user=member)
        if d == "s":
            await asyncio.sleep(int(time))
            await guild.unban(user=member)
        if d == "m":
            await asyncio.sleep(int(time*60))
            await guild.unban(user=member)
        if d == "h":
            await asyncio.sleep(int(time*60*60))
            await guild.unban(user=member)
        if d == "d":
            await asyncio.sleep(time*60*60*24)
            await guild.unban(int(user=member))
            
    @commands.command()
    @blacklist_check()
    @ignore_check()
   # @commands.has_permissions(m_messages=True)
    #@commands.bot_has_permissions(send_messages=True)
    async def vclist(self,ctx):
        ''' Get the list of members in vc you are connected to'''
        if not ctx.message.author.voice:
            await ctx.send(f" | You are not connected to any voice channels")
        else:
            member_list = ctx.message.author.voice.channel.members
            color = 0x42f579
            await lister(ctx,your_list=member_list,color=color,title=f"List of members in {ctx.message.author.voice.channel.name}")
    @commands.group(invoke_without_command=True)
    @blacklist_check()
    @ignore_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def purge1(self, ctx,amount:int=10):
        if amount >1000:
            return await ctx.send(embed=discord.Embed(title="Purge limit exceeded. Please provide an integer which is less than or equal to 1000.", color=0x42f579))
        deleted = await ctx.channel.purge(limit=amount+1)
        return await ctx.send(embed=discord.Embed(title=f" Deleted {len(deleted)-1} message", color=0x42f579), delete_after=5)

    @purge1.command()
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def startswith(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send(embed=discord.Embed(title="Purge limit exceeded. Please provide an integer which is less than or equal to 1000.", color=0x42f579), delete_after=5)
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.content.startswith(key):
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(embeddiscord.Emfbed(title=f" Deleted {len(deleted)}/{amount} message(s) which started with the given keyword", color=0x42f579), delete_after=5)

    @purge1.command()
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def endswith(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send(embed=discord.Embed(title="Purge limit exceeded. Please provide an integer which is less than or equal to 1000.", color=0x42f579), delete_after=5)
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.content.endswith(key):
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(embed=discord.Embed(title=f" Deleted {len(deleted)}/{amount} message(s) which ended with the given keyword", color=0x42f579), delete_after=5)

    @purge1.command()
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def contains(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send(embed=discord.Embed(title="Purge limit exceeded. Please provide an integer which is less than or equal to 1000.", color=0x42f579), delete_after=5)
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if key in m.content:
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(embed=discord.Embed(title=f" Deleted {len(deleted)}/{amount} message(s) which contained the given keyword", color=0x42f579), delete_after=5)



    @purge1.command()
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def invites(self, ctx, amount: int = 10):
        if amount >1000:
            return await ctx.send(embed=discord.Embed(title="Purge limit exceeded. Please provide an integer which is less than or equal to 1000.", color=0x42f579), delete_after=5)
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if "discord.gg/" in m.content.lower():
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(embed=discord.Embed(title=f"Deleted {len(deleted)}/{amount} message(s) which contained invites", color=0x42f579), delete_after=5)

    
      
    

    

    


    @commands.command(name='kick', help="Somebody is breaking rules again and again kick him from the server as punishment", aliases=['k'], usage=" <member> <reason>")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(kick_members=True)
    async def kick1(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
            return await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x42f579))
        if ctx.guild.me.top_role <= member.top_role:
            return await ctx.send(f"<:Wrong:1017402708703064144> | My highest role is below {member}")
        if ctx.author.top_role <= member.top_role:

            await ctx.send(f"<:Wrong:1017402708703064144> | Your highest role is below {member}")
        else:
            if reason is None:
                reason = f"action done by {ctx.author}"
                await member.kick(reason=reason)
                await ctx.send(f"<a:tickright:1106893326545854524> | Successfully kicked {member}")
                await member.send(f":exclamation: | You have been kicked from {ctx.guild.name} for: {reason} by {ctx.author}!")

        
 #   @commands.command(usage="<emoji>")
  #  @blacklist_check()
 #   async def enlarge(self, ctx, emoji: discord.Emoji):
  #      ''' Enlarge any emoji '''
       # url = emoji(self,format='png')
   #     url = emoji.url
   #     await ctx.send(url)
      
    @commands.command(usage=" <role/id>")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def roleall(self,ctx,role:discord.Role,reason=None):
        ''' Gives all the humans any role '''
        reason = f"responsible {ctx.author}"


        await ctx.send(embed=discord.Embed(title=f" Adding {role.name} to all humans!", color=0x42f579))

        humans = [mem for mem in ctx.guild.members if not mem.bot]
        for h in humans:
            await h.add_roles(role, reason=reason)
        await ctx.send(embed=discord.Embed(title=f" Successfully given {role.name} to all members!", color=0x42f579))
            
            


 

    @commands.command(usage="<role/id>")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def giveallbots(self,ctx,role:discord.Role, reason=None):
        ''' Give all bots any role '''
        reason = f"responsible {ctx.author}"

        await ctx.send(embed=discord.Embed(title=f" Adding {role.name} to all bots!", color=0x42f579))

        humans = [mem for mem in ctx.guild.members if mem.bot]
        for h in humans:
            await h.add_roles(role, reason=reason)
        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | Successfully given {role.name} to all bots!", color=0x42f579))

    @commands.command(usage="<role/id>")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def removeallhumans(self,ctx,role:discord.Role, reason=None):
        ''' Removes a role from all human members '''
        reason = f"responsible {ctx.author}"
        await ctx.send(embed=discord.Embed(title=f" Removing {role.name} from all humans!", color=0x42f579))

        humans = [mem for mem in ctx.guild.members if not mem.bot]
        for h in humans:
            await h.remove_roles(role, reason=reason)
        await ctx.send(embed=discord.Embed(title=f" Successfully removed {role.name} from all members!", color=0x42f579))

    @commands.command(usage="<role/id>")
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def removeallbots(self,ctx,role:discord.Role, reason=None):
        ''' Removes a role from all the bots '''
        reason = f"responsible {ctx.author}"
        await ctx.send(embed=discord.Embed(title=f" Removing  {role.name} from all bots!", color=0x42f579))

        humans = [mem for mem in ctx.guild.members if mem.bot]
        for h in humans:
            await h.remove_roles(role, reason=reason)
        await ctx.send(embed= discord.Embed(title=f" Successfully removed {role.name} from all bots!", color=0x42f579))

  
    @commands.command(aliases=['w'], usage="<member> <reason>")
    @blacklist_check()
    @commands.has_permissions(kick_members=True)
    async def warn54(self, ctx, member: discord.Member, * , reason="No Reason Provided!"):
        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | {member.display_name} has been warned for: {reason}", color=0x42f579))
        await member.send(embed=discord.Embed(title=f":exclamation: | You have been warned in {ctx.guild.name} for: {reason}", color=0x42f579))



                   


    @commands.command(usage="<member>")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(manage_messages=True)
    async def vcdeafen(self, ctx, user: discord.Member, * , reason=None):
        await ctx.send(embed=discord.Embed(title=f" {user.display_name} has been deafened, for: {reason}", color=0x42f579))
        await user.edit(deafen = True)

    @commands.command(aliases=["vm"], usage="<member>")
    @ignore_check()
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    async def vcmute(self, ctx, member: discord.Member, * , reason=None):
        await ctx.send(embed=discord.Embed(title=f" {member.display_name} has been muted, for: {reason}", color=0x42f579))
        await member.edit(mute = True)

    @commands.command(usage="<member>")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(manage_messages=True)
    async def vcunmute(self, ctx, member: discord.Member):
        await ctx.send(embed=discord.Embed(title=f" {member.display_name} has been unmuted.", color=0x42f579))
        await member.edit(mute = False)

    @commands.command(usage="<member>")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(manage_messages=True)
    async def vcundeafen(self, ctx, member: discord.Member):
        await ctx.send(embed=discord.Embed(title=f" {member.display_name} has been undeafened.", color=0x42f579))
        await member.edit(deafen = False)

    @commands.command(usage="<emoji>")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(manage_emojis=True)
    async def delemoji(self, ctx, emoji: discord.Emoji):
        await emoji.delete()
        await ctx.send(embed=discord.Embed(title=" emoji has been deleted.", color=0x42f579))

    @commands.command()
    @ignore_check()
    async def emolink(self, ctx, url:str, *, name = None):
        if name == None:
            name == "stolen-emoji"
        if url == discord.Emoji:
            url = discord.Emoji.url
        guild = ctx.guild
        async with aiohttp.ClientSession() as ses:
            async with ses.get(url) as r:
                try:
                    imgOrGif = BytesIO(await r.read())
                    bValue = imgOrGif.getvalue()
                    if r.status in range(200, 299):
                        emoji = await guild.create_custom_emoji(image=bValue, name=name)
                        await ctx.send(f"<:tick_right:1003345911067443241> | Sucessfully added Emoji `:{name}:`")
                        await ses.close()
                    else:
                        await ctx.send(f"<:wrong:1003345816326516756> | Something went wrong | {r.status}")
                except discord.HTTPException:
                    await ctx.send(f"<:wrong:1003345816326516756> | The file is too big.")

    @commands.command()
    @ignore_check()
    async def fban(self,ctx, member:discord.Member):
        await ctx.send(f"<a:tickright:1106893326545854524> | successfully banned **{member}**")

        await member.send(embed=discord.Embed(title=f" You have been banned from {ctx.message.guild.name} for reason: {reason} by {ctx.author}", color=0x42f579))
    @commands.command(name='ban', help="Somebody is breaking rules again and again | ban him from the server as punishment", usage="?ban <member> <reason>")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
            return await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
        if ctx.guild.me.top_role <= member.top_role:

            await ctx.send(f"<:Wrong:1017402708703064144> | My highest role is below {member}")


        else:
            if reason is None:
                reason = f"action done "
            await member.ban(reason=f" {reason} by | {ctx.author}")
            await ctx.send(f"<a:tickright:1106893326545854524> | successfully banned **{member}**")
            await member.send(embed=discord.Embed(title=f" You have been banned from {ctx.message.guild.name} for reason: {reason} by {ctx.author}", color=0x2f3136))
                
                

    
    
    


    
    
    @commands.command(usage="?unban <id>")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int):
        
            user = self.client.get_user(id)
            await ctx.guild.unban(user, reason=f"action done by {ctx.author}")
            await ctx.send(embed=discord.Embed(title=f" {user.name} has been successfully unbanned", color=0x42f579))

    @commands.command()
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(manage_channels=True)
    async def clone(self, ctx, channel: discord.TextChannel, reason=None):
            
                    reason = f"responsible {ctx.author}"
                    await channel.clone(f"action done by {ctx.author}")
                    await ctx.send(f"{channel.name} has been successfully cloned")


               

async def setup(client):
    await client.add_cog(moderation(client))