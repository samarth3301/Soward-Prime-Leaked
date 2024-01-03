import discord
from discord.ext import commands
import json
from prince1.Tools import *
import json
import time 
import datetime
start_time = time.time()
import asyncio
from typing import Optional
from discord.ui import Button, View
from prince.bot import Bot
from prince1.Tools import *
class prince(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.owner = [1018139793789563000,984815117730480228,866577524917534720,840661651900596255,971454244282597396]
        
        
    @commands.command(help="create autoresponse!",aliases=["ar-create"], usage="$ar-create <name> <trigger>")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    async def autoresponse_create(self, ctx, name , *, message):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
        numbers = []
        if str(ctx.guild.id) in autoresponse:
            for autoresponsecount in autoresponse[str(ctx.guild.id)]:
              numbers.append(autoresponsecount)
            if len(numbers) >= 20:
                return await ctx.send(embed=discord.Embed(title=f'You can\'t add more than 20 autoresponses in a server', color=0x2f3136))
        if str(ctx.guild.id) in autoresponse:
            if name in autoresponse[str(ctx.guild.id)]:
                return await ctx.send(embed=discord.Embed(title=f' The autoresponse `{name}` is already in the server', color=0x2f3136))
        if str(ctx.guild.id) in autoresponse:
            autoresponse[str(ctx.guild.id)][name] = message
            with open("autoresponse.json", "w") as f:
              json.dump(autoresponse, f, indent=4)
            return await ctx.reply(embed=discord.Embed(title=f'Created a autoresponse with the name : `{name}`', color=0x2f3136))

        data = {
            name : message,
        }
        autoresponse[str(ctx.guild.id)] = data

        with open("autoresponse.json", "w") as f:
            json.dump(autoresponse, f, indent=4)
            return await ctx.reply(embed=discord.Embed(title=f' Created a autoresponse with the name : `{name}`', color=0x2f3136))
  
    @commands.command(help="delete autoresponse!",aliases=["ar-delete"], usage="$ar-delete <name>")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()    
    @commands.has_permissions(administrator=True)
    async def autoresponse_delete(self, ctx, name):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
            
        if str(ctx.guild.id) in autoresponse:
            if name in autoresponse[str(ctx.guild.id)]:
                del autoresponse[str(ctx.guild.id)][name]
                with open("autoresponse.json", "w") as f:
                    json.dump(autoresponse, f, indent=4)
                return await ctx.reply(embed=discord.Embed(title=f'Deleted the `{name}` autoresponse in the server', color=0x42f579))
            else:
                return await ctx.reply(embed=discord.Embed(title=f'No autoresponse found with the name `{name}`', color=0x42f579))
        else:
            return await ctx.reply(embed=discord.Embed(title=f'There is no autoresponses in the server', color=0x42f579))

    @commands.command(help="edit Autoresponse",aliases=["ar-edit"], usage="$ar-edit <name> <new trigger>")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def autoresponse_edit(self, ctx, name , *, message):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
        if str(ctx.guild.id) in autoresponse:
            if name in autoresponse[str(ctx.guild.id)]:
                autoresponse[str(ctx.guild.id)][name] = message
                with open("autoresponse.json", "w") as f:
                    json.dump(autoresponse, f, indent=4)
                return await ctx.send(embed=discord.Embed(title=f'Edited the `{name}` autoresponse', color=0x2f3136))
        else:
            return await ctx.send(embed=discord.Embed(title=f'There is no autoresponses in the server', color=0x2f3136))

    

    @commands.command(help="hide voice channel", usage="$vchide <channel id>")
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    async def vchide(self, ctx, channel: discord.VoiceChannel = None):
        ch = channel or ctx.author.voice.channel
        overwrite = ch.overwrites_for(ctx.guild.default_role)
        overwrite.view_channel = False
        overwrite.connect = False
        await ch.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.reply(embed=discord.Embed(title=f'<:ri8:1038487759750438912> | {ch.mention} is now hidden from the default role.', color=0x42f579))

    @commands.command()
    @commands.is_owner()
    async def guild(self,ctx, id: int):
            guild = self.bot.get_guild(id)
            guildname = guild.name
            guildid = guild.id
            guildowner = guild.owner.name
            guildmembers = guild.member_count
            embed = discord.Embed(title=f"guild info",description=f"```guild =  {guild.name}\n guild id = {guildid}\n Owner =  {guild.owner}\n members =  {guildmembers}```",color=000000)
            await ctx.reply(embed=embed,mention_author=False)

    @commands.command(aliases=["large"], help="enlarge emoji", usage="$large <emoji>")
    @ignore_check()
    @commands.cooldown(1, 5, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @blacklist_check()
    async def enlarge(self,ctx , emoji: discord.PartialEmoji = None):
            embed = discord.Embed(title = f"Emoji Name | {emoji.name}" , color = 000000)
            embed.set_image(url=  f'{emoji.url}')
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.display_avatar.url}")
            embed.set_footer(text="Made By Prince" , icon_url="https://images-ext-2.discordapp.net/external/XpYSeN_4K1TG8OtzI3R3LE3zXbhvqB1rwgQkKRSs-Ww/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/980361546918162482/aa3b4e68dd27540854c0e0e3f374fe32.png")
            await ctx.send(embed = embed)


    @commands.command(aliases=['mc'], help="show server membercount", usage="$mc")
    @ignore_check()
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    async def membercount(self,ctx):
            user_count = len([x for x in ctx.guild.members if not x.bot])
            online = len(list(filter(lambda m: str(m.status)=="online", ctx.guild.members)))
            idle = len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members)))
            dnd = len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members)))
            offline = len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))
            t_online = [online, idle, dnd]
            Sum = sum(t_online)
            mbed=discord.Embed(title="Membercount", description=f"**Total Members = {ctx.author.guild.member_count}**", color=0x2f3136)
  #          mbed.set_author(name=ctx.guild.name, icon_url=ctx.author.display_avatar.url)
            if ctx.guild.icon:
                    mbed.set_thumbnail(url=ctx.guild.icon)
                    mbed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar.url)
                    await ctx.send(embed=mbed)

        
    @commands.command(aliases=['fuckoff'], usage="$hackban <user>", help="ban someone with id")
    @ignore_check()
    @commands.cooldown(1, 5, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @blacklist_check()
    async def hackban(self,ctx, userid="Nonexd",reason="None specified"):
            me = ctx.guild.me
            if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
                    await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
            else:
                    user = await self.bot.fetch_user(int(userid))
                    await ctx.guild.ban(user,reason=reason)
                    embed=discord.Embed(title="Soward", description=f"\n<:Icons_correct:1017402689027592222> | Banned :  {user.name}#{user.discriminator}\n ID -{userid}", color=0x42f579,timestamp=ctx.message.created_at)
                    embed.set_footer(text="Soward")
                    await ctx.send(embed=embed)



    @commands.command(aliases=["uphshwh"])
    @commands.cooldown(1, 5, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @blacklist_check()
    async def upjjsjsjstime(self,ctx):
            current_time = time.time()
            difference = int(round(current_time - start_time))
            uptime = str(datetime.timedelta(seconds=difference))
            await ctx.reply(embed=discord.Embed(title=uptime, color=0x42f579))
 
    @commands.command(help="close ticket", usage="$close")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    async def close(self,ctx, channel: discord.TextChannel = None):
            channel = channel or ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            await ctx.reply(f'<:Icons_correct:1017402689027592222> | Successfully closed {ctx.channel.mention}', mention_author=False)

    @commands.command(help="Add user to ticket")
    @ignore_check()
    @commands.cooldown(1, 5, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    async def adduser(self,ctx, member: discord.Member, channel=None):
            channel = channel or ctx.channel
            guild = ctx.guild
            overwrite = channel.overwrites_for(member)
            overwrite.view_channel = True
            await ctx.channel.set_permissions(member, overwrite=overwrite)
            await ctx.reply(f"Successfully added {member.mention} to {channel}", mention_author=False)

    @commands.command(help="delete ticket")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 5, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @ignore_check()
    @commands.guild_only()
    @blacklist_check()
    async def ticdelete(self,ctx):
            await ctx.send(f" | deleting {ctx.channel.mention} in 1sec.")
            await asyncio.sleep(1)
            await ctx.channel.delete()

    @commands.command(aliases=["riuwh"], usage="$ri <role>", help="Show you all information about role!" )
    @blacklist_check()
    async def rohleinfjjo(self, ctx, role: discord.Role = None):
            riembed = discord.Embed(title=f"**{role.name}'s Information**", colour=discord.Colour(0x42f579))
            perms = ""
            if role.permissions.administrator:
                    perms += "Administrator, "
                    if role.permissions.create_instant_invite:
                            perms += "Create Instant Invite, "
                            if role.permissions.kick_members:
                                    perms += "Kick Members, "
                                    if role.permissions.ban_members:
                                            perms += "Ban Members, "
                                            if role.permissions.manage_channels:
                                                    perms += "Manage Channels, "
                                                    if role.permissions.manage_guild:
                                                            perms += "Manage Guild, "
                                                            if role.permissions.add_reactions:
                                                                    perms += "Add Reactions, "
                                                                    if role.permissions.view_audit_log:
                                                                            perms += "View Audit Log, "
                                                                            if role.permissions.read_messages:
                                                                                    perms += "Read Messages, "
                                                                                    if role.permissions.send_messages:
                                                                                            perms += "Send Messages, "
                                                                                            if role.permissions.send_tts_messages:
                                                                                                    perms += "Send TTS Messages, "
                                                                                                    if role.permissions.manage_messages:
                                                                                                            perms += "Manage Messages, "
                                                                                                            if role.permissions.embed_links:
                                                                                                                    perms += "Embed Links, "
                                                                                                                    if role.permissions.attach_files:
                                                                                                                            perms += "Attach Files, "
                                                                                                                            if role.permissions.read_message_history:
                                                                                                                                    perms += "Read Message History, "
                                                                                                                                    if role.permissions.mention_everyone:
                                                                                                                                            perms += "Mention Everyone, "
                                                                                                                                            if role.permissions.external_emojis:
                                                                                                                                                    perms += "Use External Emojis, "
                                                                                                                                                    if role.permissions.connect:
                                                                                                                                                            perms += "Connect to Voice, "
                                                                                                                                                            if role.permissions.speak:
                                                                                                                                                                    perms += "Speak, "
                                                                                                                                                                    if role.permissions.mute_members:
                                                                                                                                                                            perms += "Mute Members, "
                                                                                                                                                                            if role.permissions.deafen_members:
                                                                                                                                                                                    perms += "Deafen Members, "
                                                                                                                                                                                    if role.permissions.move_members:
                                                                                                                                                                                            perms += "Move Members, "
                                                                                                                                                                                            if role.permissions.use_voice_activation:
                                                                                                                                                                                                    perms += "Use Voice Activation, "
                                                                                                                                                                                                    if role.permissions.change_nickname:
                                                                                                                                                                                                            perms += "Change Nickname, "
                                                                                                                                                                                                            if role.permissions.manage_nicknames:
                                                                                                                                                                                                                    perms += "Manage Nicknames, "
                                                                                                                                                                                                                    if role.permissions.manage_roles:
                                                                                                                                                                                                                            perms += "Manage Roles, "
                                                                                                                                                                                                                            if role.permissions.manage_webhooks:
                                                                                                                                                                                                                                    perms += "Manage Webhooks, "
                                                                                                                                                                                                                                    if role.permissions.manage_emojis:
                                                                                                                                                                                                                                            perms += "Manage Emojis, "
                                                                                                                                                                                                                                            if perms is None:
                                                                                                                                                                                                                                                    perms = "None"
                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                    perms = perms.strip(", ")
                                                                                                                                                                                                                                                    riembed.add_field(name='__General info__', value=f"Name: {role.name}\nId: {role.id}\nPosition: {role.position}\nHex: {role.color}\nMentionable: {role.mentionable}\nCreated At: {role.created_at}\nManaged by Integration: {(role.managed)}\n\nmembers in this role: {(len(role.members))}\n\nPermissions: {perms}")
                                                                                                                                                                                                                                                    await ctx.reply(embed=riembed, mention_author=False)  

    @commands.command()
    @commands.has_guild_permissions(manage_roles=True)
    @blacklist_check()
    async def unhhwhwhideall(self,ctx):
            author = ctx.message.author
            me = ctx.guild.me
            if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
                    await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x42f579))
                    return
            else:
                    for x in ctx.guild.channels:
                            await x.set_permissions(ctx.guild.default_role,view_channel=True)
                        
                            await ctx.reply(embed=discord.Embed(title="Successfully unhide all channels", description=f"responsible {ctx.author}", color=0x42f579))
                            return
                            pass


    @commands.command()
    @commands.has_guild_permissions(manage_roles=True)
    @blacklist_check()
    async def hidealjajsjjl(self,ctx):
            me = ctx.guild.me
            if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
                    await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x42f579))
                    return
            else:
                    for x in ctx.guild.channels:
                            await x.set_permissions(ctx.guild.default_role,view_channel=False)
                            await ctx.reply(embed=discord.Embed(title="successfully hide all channels", description=f"responsible {ctx.author}", color=0x42f579))
                            return
                            pass





    @commands.command()
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 5, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def hide(self, ctx, channel : discord.TextChannel=None):
            if channel == None:
                    channel = ctx.channel
                    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
                    overwrite.view_channel = False
                    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#({ctx.author.id})")
                    
                    await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> | <#{channel.id}> is now hidden from the default role.", color=0x42f579))

    @commands.command()
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 5, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def unhide(self,ctx, channel : discord.TextChannel=None):
            if channel == None:
                    channel = ctx.channel
                    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
                    overwrite.view_channel = True
                    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#({ctx.author.id})")
                    await ctx.reply(embed=discord.Embed(title=f'<:Icons_correct:1017402689027592222> | <#{channel.id}> is now visible to the default role.', color=0x42f579))


    @commands.command(aliases=["inv"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @ignore_check()

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    async def invite(self,ctx):
            author = ctx.message.author
            b = Button(label='Invite Me', style=discord.ButtonStyle.link, url='https://discord.com/oauth2/authorize?client_id=1013771497157972008&permissions=1101052116095&scope=applications.commands%20bot')
            view = View()
            view.add_item(b)
            embed = discord.Embed(description="click on button below!", color=0x2f3136) 
            embed.set_author(name=f"{author.name}", icon_url=author.display_avatar.url)
            embed.set_thumbnail(url=author.display_avatar.url)
            embed.set_footer(text=f"thanks for using Soward") 
            await ctx.send(embed=embed, view=view)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @blacklist_check()
    async def ping1(self,ctx):
            author = ctx.message.author
            embed = discord.Embed(description=f"<a:th_heartbeat:1017469364712263691> Pong! {round(self.bot.latency * 1000)}ms", color=0x42f579)
            embed.set_author(name=f"{author.name}", icon_url=author.display_avatar.url)
            embed.set_thumbnail(url=author.display_avatar.url)
            embed.set_footer(text=f"requested by {author.name}", icon_url=author.display_avatar.url)
            await ctx.channel.send(embed=embed)

    @commands.command(usage="$embed <message>", help="Create embed")
    @blacklist_check()
    @commands.has_permissions(embed_links=True)
    async def embjejeed(self,ctx,*,mesg=f"Format : embed [words]"):
            await ctx.message.delete()
            embed=discord.Embed(description=mesg,color=0x42f579,timestamp=ctx.message.created_at)
            embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.display_avatar.url) 
            embed.set_footer(text=f"")
            await ctx.send(embed=embed)

    @commands.command(aliases=["channelc"], usage="$addchannel <name>", help="create text channel!")
    @ignore_check()
    @commands.cooldown(1, 5, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    @blacklist_check()
    async def addchannel(self, ctx, *names):
            me = ctx.guild.me
            if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
                    await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
                    return
            else:
                    for name in names:
                            await ctx.guild.create_text_channel(name)
                            await ctx.send(embed=discord.Embed(title=f'<:Icons_correct:1017402689027592222> | {name} has been created', color=0x2f3136))
    

    @commands.command(aliases=['delchannel'], help="delete text channel", usage="$delchannel <channel>")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    @blacklist_check()
    async def deletechannel(self,ctx, *channels: discord.TextChannel):
            me = ctx.guild.me
            if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
                    await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
                    return
            else:
                    for ch in channels:
                            await ch.delete()
                            await ctx.send(embed=discord.Embed(title=f' <:Icons_correct:1017402689027592222> | {ch.name} has been deleted', color=0x2f3136))
            
    @commands.command(aliases=["userbahhnner"])
    @blacklist_check()
    @ignore_check()
    async def bannhhher(self,ctx,  member: discord.Member = None):
       if member == None:
           member = ctx.author
           bannerUser = await self.bot.fetch_user(member.id)
           if not bannerUser.banner:
               await ctx.reply("this user has no banner")
           else:
               embed=discord.Embed(title=f"{member.name}'s banner", color=0x42f579)
               embed.set_footer(text=f"requested by {ctx.author.name}", icon_url=member.display_avatar.url)
               embed.set_image(url=bannerUser.banner)
               await ctx.send(embed=embed)
                        
    @commands.command()
    @blacklist_check()
    async def serverbanhhhner(self, ctx: commands.Context):
            if not ctx.guild.banner:
                    await ctx.send('This server does not have any banner!')
                    embed = discord.Embed(title=f'{ctx.guild.name}\'s Banner', color = 0x42f579)
                    embed.set_image(url=ctx.guild.banner)
                    await ctx.send(embed=embed)                 
    @commands.command(aliases=["prjjejeefix"], usage="$prefix <new prefix>", help="change server Prefix!")
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    async def setnnnnbprefix(self, ctx, prefixx):
            with open("prefixes.json", "r") as f:
                    idk = json.load(f)
                    if len(prefixx) > 5:
                            await ctx.reply(embed=discord.Embed(color=discord.Colour(0x42f579), description=f'<:Wrong:1017402708703064144> | Prefix Cannot Exceed More Than 5 Letters'))
                    elif len(prefixx) <= 5:
                            idk[str(ctx.guild.id)] =  prefixx
                            await ctx.reply(embed=discord.Embed(color=discord.Colour(0x42f579), description=f'<:Icons_correct:1017402689027592222> | Updated Server Prefix To `{prefixx}`'))
                            with open("prefixes.json", "w") as f:
                                    json.dump(idk, f, indent=4)             
 


  
    @commands.command(aliases=["nonnnpre"])
  #  @commands.is_owner()
    async def nphhahsh(self, ctx, type=None, mem: discord.Member = None):
            if ctx.author.id in self.owner:
         #           await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | You don't have access to this command !", color=0xFF1B1B))
      #              return
      #      else:
                    if type == None:
                            await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | You missed the 'Type' argument", color=0x42f579))
                            return
                    else:
                            if type == "add":
                                    if mem == None:
                                            await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | You missed the 'Member' argument", color=0x42f579))
                                            return
                                    else:
                                            with open ("nonprefix.json","r") as f:
                                                    member = json.load(f)
                                                    if str(mem.id) in member["access"]:
                                                            await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | The mentioned member is already added!", color=0x42f579))
                                                            return
                                                    else:
                                                    
                                                            member["access"].append(str(mem.id))
                                                            with open ("nonprefix.json","w") as f:
                                                                    json.dump(member,f)
                                                                    await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> |  successfully added {mem.name} to noprefix !", color=0x42f579))

    @commands.command(aliases=["npr"])
    @ignore_check()
    async def npremove(self,ctx,mem: discord.Member = None):
        if ctx.author.id in self.owner:
            with open ("nonprefix.json","r") as f:
                    member = json.load(f)
                    member["access"].remove(str(mem.id))
                    with open ("nonprefix.json","w") as f:
                            json.dump(member,f)
                            await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> | {mem.name} is successfully removed from noprefix!", color=0x42f579)) 


    @commands.command(aliases=["blnd"])
    async def blachhbbklisted(self,ctx, type=None, mem: discord.Member = None):
            embed = discord.Embed(title=f"blacklisted Users", description="")
            with open ('blacklist.json', 'r') as i:
                    mem = json.load(i)
                    try:
                            for u in mem["ids"]:
                                    user = await self.bot.fetch_user(u)
                                    embed.description += f"{user.name}\n"
                                    embed.title = "blacklisted users "
                                    await ctx.reply(embed = embed,mention_author=False)
                    except KeyError:
                            await ctx.send("No blacklisted users found")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @blacklist_check()
    @ignore_check()
    async def source(self,ctx):
      embed = discord.Embed(description=f"[soward src](https://github.com/PRINCEOP24/Soward-bot-src.git)", color=0x42f579)
     # embed.set_author(name=f"{user.avatar}")                          
      embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/kHT4vIV2yvQVr_TVRWuSfbSPVzLuI0hjxVULZroCx-E/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1004248513435152484/fa3d59466f44e012f70d541d9d409520.png")
      embed.set_footer(text="enjoy")
      await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    @blacklist_check()
    @ignore_check()
    async def getinv(self,ctx, guild_id: int):
        guild = self.bot.get_guild(guild_id)
        channel = guild.channels[0]
        invitelink = await channel.create_invite(max_age=300)
        await ctx.reply(invitelink)

    

    
    @commands.command()
    @commands.is_owner()
    @ignore_check()
    async def leaveg(self,ctx, *, guild: discord.Guild=None):
      if guild is None:
          await ctx.send("pls provide valid guild")
          return
      else:
          await guild.leave() 
          await ctx.send(f"I left: {guild.name}!")

    @commands.command(name="rolhahe", help="give role and remove role", usage="$role <user> <role>")
    async def _rohhehle(self,ctx, user: discord.Member=None, *, role: discord.Role=None):
      me = ctx.guild.me
      if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
          await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x42f579))
          return
          if ctx.guild.me.top_role <= user.top_role:
              await ctx.reply(embed=discord.Embed(description=f"Error in updating {user.mention}\n my highest role below {user.name}", color=0x42f579))
          return                         
      else:
          if ctx.message.author.guild_permissions.manage_roles:
              guild = ctx.guild
              if role in user.roles:
                  await user.remove_roles(role, reason=f"removed by {ctx.message.author}")
                  await ctx.reply(embed=discord.Embed(description=f"<:ri8:1038487759750438912> updated roles for {user.name}  - {role.name}", color=0x42f579))
              elif role not in user.roles:
                  await user.add_roles(role, reason=f"added by {ctx.message.author}")
                  await ctx.reply(embed=discord.Embed(description=f"<:ri8:1038487759750438912> updated roles for {user.name} + {role.name}", color=0x42f579))
                        

    @commands.command(aliases=["vcmove"])
    @commands.cooldown(1, 5, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    @commands.has_permissions(administrator =  True)
    @blacklist_check()
    @ignore_check()
    async def voicemove(self,ctx, channel : discord.VoiceChannel = None):
        if channel == None:
            await ctx.reply('Mention a channel to move users to!')
        if ctx.author.voice:    
            channell = ctx.author.voice.channel
            members = channell.members
            for m in members:
                await m.move_to(channel)
                await ctx.reply(f"Moved all users to {channel.mention}")
                if ctx.author.voice is None:
                    await ctx.reply('You need to be connected to the channel from where you want to move everyone.')


    @commands.command(aliases=["voicekick"], help="kick someone from vc", usage="$vckick <member>")
    @ignore_check()
    
    @commands.has_permissions(manage_messages=True)
    async def vckick(self, ctx, member: discord.Member, reason="No reason provided"):
            await member.move_to(None)
            await ctx.reply(embed=discord.Embed(title=f' | {member} has been disconnected from vc.', color=0x42f579))
    
async def setup(bot):
    await bot.add_cog(prince(bot))     
