import discord
from discord.ext import commands,tasks
#from cogs.utils.emoji import tick,cross,online,dnd,idle,offline
import math
from disputils import BotEmbedPaginator
import asyncio
import re
from prince1.Tools import*
from discord.ui import Button, View
#from prince.bot import Bot
from prince.embed import error_embed
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


time_regex = re.compile(r"(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h":3600,"s":1,"m":60,"d":86400}


def convert(argument):
    args = argument.lower()
    matches = re.findall(time_regex, args)
    time = 0
    for key,value in matches:
        try:
            time += time_dict[value] * float(key)
        except KeyError:
            raise commands.BadArgument(
                f"{value} is an invalid time key! h|m|s|d are valid arguments"
            )
        except ValueError:
            raise commands.BadArgument(f"{key} is not a number!")
    return round(time)

class Role(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.group(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    @ignore_check()
    @commands.bot_has_permissions(manage_roles=True)
    @blacklist_check()
    async def rolhjes(self,ctx):
        ''' Roles manager category '''
        if ctx.invoked_subcommand is None:
            helper = str(ctx.invoked_subcommand) if ctx.invoked_subcommand else str(ctx.command)
            await ctx.send(f"{ctx.author.name} The correct way of using this command is ")
            await ctx.send_help(helper)

    @commands.command()
    @ignore_check()

    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @blacklist_check()
    async def give(self,ctx,user:discord.Member,role:discord.Role):
        if role.position >= ctx.author.top_role.position:

            await ctx.reply(embed=discord.Embed(title="this role above ur top role u can't add this role .", color=0x2f3136, timestamp=ctx.message.created_at))
            return
            
        if role.permissions.administrator or role.permissions.kick_members or role.permissions.ban_members or role.permissions.manage_server:
            b = Button(label='Yes', style=discord.ButtonStyle.green)
            b2 = Button(label='No', style=discord.ButtonStyle.red)
            view = View()
            
            view.add_item(b)
            view.add_item(b2)
            async def b_callback(interaction: discord.Interaction):
                await user.add_roles(role)
                done=discord.Embed(title=f" <:ri8:1038487759750438912>  Role {role.name} given to {user.name}", color=0x42f579, timestamp=ctx.message.created_at)
                await interaction.response.edit_message(embed=done,view=None)
            
            
            main_msg=embed=discord.Embed(title="<a:Attention:1049046621209510008>**Dangerous Permission Detected**", description="The mentioned role contain dangerous permissions. Do you still want to procced to update the roles of the mentioned user?",color=000000, timestamp=ctx.message.created_at)
            cancel=discord.Embed(title="cancelled", color=000000, timestamp=ctx.message.created_at)
            async def b2_callback(interaction: discord.Interaction):
                  await interaction.response.edit_message(content="",view=None,embed=cancel)
            b.callback = b_callback
            b2.callback = b2_callback
            await ctx.send(embed=main_msg, view=view)
                           
                
                
        else:
            await user.add_roles(role)
            await ctx.reply(embed=discord.Embed(title=f" <:ri8:1038487759750438912> Role {role.name} given to {user.name}", color=0x42f579))

    @commands.command(aliases=["temprole","tpr"], usage="temprole <role> <time> <member>")
    @ignore_check()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    @blacklist_check()
    async def temp(self,ctx,role:discord.Role,time,*,user:discord.Member):
        '''`Temporarily give a role to any member` '''
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
            await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x42f579))
        else:
            seconds = convert(time)
            await user.add_roles(role,reason=None)
            await ctx.reply(embed= discord.Embed(title=f"<:ri8:1038487759750438912> | {role.name} added to user {user.name}", color=0x42f579))
            await asyncio.sleep(seconds)
            await user.remove_roles(role, reason=f"action done by {ctx.author}")


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @ignore_check()
    @blacklist_check()
    async def removhhge(self,ctx,user:discord.Member,role:discord.Role):
        ''' <:icons_text1:1004454337705152582>`Remove a role from any member` '''
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
            await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x42f579))
        else:
            await user.remove_roles(role, reason=f"action done by {ctx.author}")
            await ctx.reply(embed=discord.Embed(title=f"<:ri8:1038487759750438912> Role {role.name} removed from {user.name}", color=0x42f579))
    

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @ignore_check()
    @blacklist_check()
    async def deleterole(self,ctx,role:discord.Role):
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
            await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x42f579))
        else:
            await role.delete(reason=f"action done by {ctx.author}")
            await ctx.send(embed=discord.Embed(title=f"<:ri8:1038487759750438912> Role {role} deleted", color=0x42f579))


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @ignore_check()
    @blacklist_check()
    async def createrole(self,ctx,*,name):
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
            await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x42f579))
        else:
            await ctx.guild.create_role(name=name,reason=f"action done by {ctx.author}",color=discord.Color.default())
            await ctx.reply(embed=discord.Embed(title=f"<:ri8:1038487759750438912> Role {name} created successfully!", color=0x42f579))
        
        


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @ignore_check()
    @blacklist_check()
    async def rename(self,ctx,role:discord.Role,*,newname):
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
            await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x42f579))
        else:
            await role.edit(name=newname, reason=f"action done by {ctx.author}")
            await ctx.send(embed=discord.Embed(title=f"<:ri8:1038487759750438912> Role {role.name} has been renamed to {newname}", color=0x42f579))

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @ignore_check()
    @blacklist_check()
    async def color(self,ctx,role:discord.Role,color):
        ''' <:icons_text1:1004454337705152582>`Changes the color of any role` '''
        if role is None:
            return await ctx.send(f"No role named {role} found in this server.")
        if not color.startswith("0x"):
            color = "0x"+color
        color = int(color,0)
        await role.edit(color=color)
        await ctx.send(f"<:ri8:1038487759750438912> Role {role.name}'s color has been changed to {color}")

    @commands.command()
    @blacklist_check()
    @ignore_check()
    @commands.bot_has_permissions(manage_roles=True)
    # @commands.has_permissions(manage_roles=True)
    async def rolem(self,ctx,*,role:discord.Role):
        ''' <:icons_text1:1004454337705152582>`Gives the list of members having specified role` '''
        role_name = role.name
        if role is None:
            return await ctx.send(f"{cross} No role named {role_name} found in this server.")
        member_list = []
        status_list = []
        for member in role.members:
            member1 = discord.utils.escape_markdown(str(member),as_needed=False,ignore_links=True)
            member_list.append(member1)
            status_list.append(member.status)
        # print(status_list)
        emoji_list = []
        for status in status_list:
            if "online" in status:
                emoji_list.append(online)
            elif "offline" in status or "invisible" in status:
                emoji_list.append(offline)
            elif "idle" in status:
                emoji_list.append(idle)
            elif "do_not_disturb" in status or "dnd" in status:
                emoji_list.append(dnd)
        if len(role.members) != 0:
            e = discord.Embed(
                description=" ",
                color=0x2f3136
                )
     #   e.add_field(name=f"Members with role {role} - [{len(role.members)}]",value="\n".join(f"{emote} | {name}" for emote,name in data_dict.items)
            # TODO - Make the embed paginated to remove the error of max characters

            nums = len(emoji_list)
            pages = math.ceil(nums / 15)
            if nums <= 25:
                e.add_field(name=f"Members with role {role}",value="\n".join(f"`[{count+1}]` {emoji_list[count]} | {member_list[count]}" for count in range(0,len(emoji_list))))
                await ctx.send(embed=e)
            elif nums > 25:
                # LOGIC HERE -
                # for ex - 100 members in role 
                # pages = 100 / 25 = 4
                # 25 * 1 = 25, 25*2 = 50,25*3 = 75, 25*4 = 100
                # 25(I),26-50(II),51-75(III)
                # print(pages)
                page = [i for i in range(1,pages+1)]
                counts = []
                first_num = 0
                for i in page:
                    if first_num == 0:
                        last_num = (i*15) -1
                    else:
                        last_num = (i*15) -1
                    # last_num = (i*25) - 1
                    if first_num > len(emoji_list):
                        first_num = len(emoji_list)
                    elif last_num > len(emoji_list):
                        last_num = len(emoji_list)
                    l = [first_num,last_num]
                    counts.append(l)
                    if last_num == len(emoji_list) or first_num == len(emoji_list):
                        break
                    first_num = last_num + 1
                    
                # print(counts)
                # [[0,25],[26,50],[51,75]] # ---> FIRST LIST INDEX WILL NOT WORK
                # [[0,24],[25,50]]
                embeds = []
                for l in counts:
                    first_num = l[0]
                    last_num = l[1]
                    # print(first_num)
                    # print(last_num)
                    em = discord.Embed(description=" ",color=discord.Color.orange()).add_field(name=f"Members with role {role} - [{len(emoji_list)}]",value="\n".join(f"`[{count+1}]` {emoji_list[count]} | {member_list[count]}" for count in range(first_num,last_num)))
                    embeds.append(em)
                
                paginator = BotEmbedPaginator(ctx,embeds)
                await paginator.run()
            else:
                pass
        else:
            await ctx.send(f"There are no members with role {role_name}")





async def setup(client):
   await client.add_cog(Role(client))
   print(OKGREEN+"[STATUS OK] Role cog is ready!")