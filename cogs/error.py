import json
from discord.ext import commands
from discord.ui import Button, View
from config import VOTE_LINK
from prince.bot import Bot
import discord
from prince.custom_checks import *
#from core import Context
from utils.Tools import *
class error(commands.Cog):
    def __init__(self, client):
        self.client = client





    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        with open('blacklist.json', 'r') as f:
                data = json.load(f)
 
        if type(error) == commands.MissingRequiredArgument:
            embed=discord.Embed(title=f"```- [] = optional argument\n- <> = required argument\n- Do NOT type these when using commands!```\n\n {ctx.command.help}", description=f"**Aiases**\n{ctx.command.aliases}\n\n**Usage**\n{ctx.command.usage}",color=0x42f579, timestamp=ctx.message.created_at)
            embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.display_avatar)
            embed.set_footer(text="Made By Prince", icon_url="https://images-ext-1.discordapp.net/external/drs16ScOT0hHfzKD1HzUKikCNrI3pp9MIsewAPotJFQ/https/cdn.discordapp.com/emojis/1034899140825583666.gif")
            return await ctx.reply(embed=embed)

        elif type(error) == commands.BotMissingPermissions:
                return await ctx.send(embed=discord.Embed(title=f"The bot is missing Permissions:", description=f" {', '.join(error.missing_perms)}", color=0x42f579))
        elif type(error) == commands.MissingRole:
                return await ctx.reply(
            f"**You are missing the role: {error.missing_role}")
        elif type(error) == commands.BotMissingRole:
                return await ctx.reply(
            f"The bot is lacking the role: {error.missing_role}")
        elif type(error) == commands.CommandNotFound:
                pass  #return await ctx. rep ly("That command does not exist.")
        elif type(error) == commands.CheckFailure:
                pass 

        elif type(error) == commands.BadArgument:
                return await ctx.reply(embed=discord.Embed(title="Error!", description=error, color=0x42f579), delete_after=5)
        else:
                await ctx.reply(embed=discord.Embed(title="Error!", description=error, color=0x42f579), delete_after=5)
      #          if str(ctx.author.id) in data["ids"]:
    #                  embed = discord.Embed(title="<a:Error:1018257469274861688>", description="you Are blacklisted from using my commands!", color=discord.Colour(0xFF1B1B))
                raise error
    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        channel = self.client.get_channel(1105843874481590304)
        embed = discord.Embed(title="soward prime added !!", color=0x42f579, description=f"**server name**: {guild.name}\n guild owner {guild.owner}  \n total servers: {len(self.client.guilds)}\n members {guild.member_count}\n server id {guild.id}")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        channel = self.client.get_channel(1105843959789527050)
        embed = discord.Embed(title="Soward prime removed !!", color=0x42f579, description=f"**server name**: {guild.name}\n guild owner {guild.owner}  \n total servers: {len(self.client.guilds)}\n members {guild.member_count}\n server id {guild.id}")
        await channel.send(embed=embed)
 
    @commands.Cog.listener()

    async def on_message(self, message):

        with open('blacklist.json', 'r') as f:

             bled = json.load(f)

        if str(message.author.id) in bled["ids"]:

            return

        

        idk = getpre(message.guild.id)

   

     

        idkprefix = idk["prefix"]

        

        #if self.client in message.content:

       # if str("<@1013771497157972008>") in message.content:

        if message.author == self.client.user or message.author.bot:

            return 

        if message.content.lower() in [f'<@{self.client.user.id}>', f'<@!{self.client.user.id}>']:

       

    

          b = Button(label='invite me',style=discord.ButtonStyle.link,url=f"https://discord.com/oauth2/authorize?client_id={self.client.user.id}&permissions=8&scope=applications.commands%20bot")            

          b2 = Button(label='support', style=discord.ButtonStyle.link, url='https://discord.gg/2drmzef4kV')

          view = View()

          view.add_item(b)

          view.add_item(b2)

          author = message.author

          embed = discord.Embed(title='**Soward Prime**', description=f'**My Prefix For This Server Is {idkprefix} **', color=0x2f3136)

          embed.set_thumbnail(url=author.display_avatar.url)

          await message.channel.send(embed=embed, view=view)
async def setup(client):
    await client.add_cog(error(client))