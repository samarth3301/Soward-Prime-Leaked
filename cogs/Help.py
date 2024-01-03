antinuke = "<:1041631826625691669:1153679832962580561>"

selfroles = "<:selfrole:1153681348935032913>"

ticket = "<:ticket:1153681365615775804>"

welcome = "<:icons_join:1089768448776753263>"

extra = "<:i_extra:1077506003907657738>"

games = "<:Games:1168125045881708614>"

moderation = "<:Moderation:1168125088235802694>"

voice = "<:voice:1168125151318114386>"

utility = "<:maxz_utilitys:1168125218385047594>"

j2c = "<:SOWARD_J2C:1168125130279501874>"
import discord 
from discord.ui import *
from discord.ext import commands 
from discord.ext.commands import Cog
class HelpView(discord.ui.Select):

    def __init__(self):

        opts = [discord.SelectOption(label="Antinuke"),

           discord.SelectOption(label="Ticket"),

           discord.SelectOption(label="Selfroles"),

           discord.SelectOption(label="Welcome"),        

           discord.SelectOption(label="Extra"), 

           discord.SelectOption(label="Games"), 

           discord.SelectOption(label="Moderation"),

           

           discord.SelectOption(label="Voice"),

           discord.SelectOption(label="Utility"),

           discord.SelectOption(label="Join To Create")

           

               ]

        super().__init__(placeholder="Please select a page.", max_values=1, min_values=1, options=opts)

    

    

    async def callback(self, interaction: discord.Interaction):

        cog = interaction.client.get_cog("anti2")

        title = cog.qualified_name

        

        embed_mod = discord.Embed(title=f"__Antinuke__", description=f"`Antinuke enable/disable`,`Antinuke config`,`Antinuke features`,`Antinuke wl add`,`Antinuke wl remove`,`Antinuke whitelist show`,`Antinuke whitelist reset`,`Antinuke channelclean`,`Antinuke roleclean`,`Antinuke recover`,`Antinuke punishment set`,`Antinuke punishment show`,`Antinuke features`", color=0x2f3136)

        embed_mod.set_author(name=f"{interaction.user}",

                                   icon_url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)

        embed_mod.set_thumbnail(url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024")

        embed_mod.set_footer(icon_url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024", text="Showing Page 1/10")

        if self.values[0] == "Antinuke":

            await interaction.response.edit_message(embed=embed_mod)

        

        cog = interaction.client.get_cog("ticket2")

        title = cog.qualified_name

        

        embed_mod = discord.Embed(title=f"__Ticket__", description=f" `ticket sendpanel`,`ticket setup`,`ticket close`,`ticket role add`,`ticket role remove`", color=0x2f3136)

        embed_mod.set_author(name=f"{interaction.user}",

                                   icon_url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)

        embed_mod.set_thumbnail(url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024")

        embed_mod.set_footer(icon_url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024", text="Showing Page 2/10")

        if self.values[0] == "Ticket":

            await interaction.response.edit_message(embed=embed_mod)

        

   #     cog = interaction.client.get_cog("selfrole1")

     #   title = cog.qualified_name

        

        embed_mod = discord.Embed(title=f"__Selfroles__", description=f"`selfroles`,`selfroles create`,`selfroles edit`,`selfroles list`,`selfroles delete`", color=0x2f3136)

        embed_mod.set_author(name=f"{interaction.user}",

                                   icon_url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)

        embed_mod.set_thumbnail(url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024")

        embed_mod.set_footer(icon_url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024", text="Showing Page 3/10")

        if self.values[0] == "Selfroles":

            await interaction.response.edit_message(embed=embed_mod)

        

    #    cog = interaction.client.get_cog("swagat1")

      #  title = cog.qualified_name

        

        embed_mod = discord.Embed(title=f"__Welcome__", description=f"`Autorole humans add`,`Autorole humans remove`,`Autorole bots add`,`Autorole bots remove`,`welcome channel add`,`welcome channel remove`,`welcome message`,`welcome embed`,`welcome ping`,`welcome title add`,`welcome title Remove`,`welcome image add`,`welcome image remove`,`welcome thumbnail add`,`welcome thumbnail remove`,`welcome footer add`,`welcome footer remove`,`welcome ping on`,`welcome ping off`,`welcome test`", color=0x2f3136)

        embed_mod.set_author(name=f"{interaction.user}",

                                   icon_url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)

        embed_mod.set_thumbnail(url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024")

        embed_mod.set_footer(icon_url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024", text="Showing Page 4/10")

        if self.values[0] == "Welcome":

            await interaction.response.edit_message(embed=embed_mod)

        

      #  cog = interaction.client.get_cog("extra1")

    #    title = cog.qualified_name

        

        embed_mod = discord.Embed(title=f"__Extra__", description=f"`setup add`, `setup delete`,`setup clear`,`setup list`,`setup reqrole`,`setup friends`,`setup vips`,`setup guests`,`setup officials`,`setup girls`,`setup bot`,`setup modss`,`setup artist`,`config-setup`", color=0x2f3136)

        embed_mod.set_author(name=f"{interaction.user}",

                                   icon_url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)

        embed_mod.set_thumbnail(url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024")

        embed_mod.set_footer(icon_url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024", text="Showing Page 5/10")

        if self.values[0] == "Extra":

            await interaction.response.edit_message(embed=embed_mod)

        

      #  cog = interaction.client.get_cog("gamess1")

      #  title = cog.qualified_name

        

        embed_mod = discord.Embed(title=f"__Games__", description=f"`tictactoe`,`rps`,`t&d`,`wumpus`,`findimposter`", color=0x2f3136)

        embed_mod.set_author(name=f"{interaction.user}",

                                   icon_url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)

        embed_mod.set_thumbnail(url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024")

        embed_mod.set_footer(icon_url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024", text="Showing Page 6/10")

        if self.values[0] == "Games":

            await interaction.response.edit_message(embed=embed_mod)

    #    cog = interaction.client.get_cog("moderation2")

    #    title = cog.qualified_name

        

        embed_mod = discord.Embed(title=f"__Moderation__", description=f"`steal`,`addsticker`,`roleicon`,`unbanall`,`ban`, `purge bot`, `purge`,`purge all`,`purge user`,`purge reaction`,`purge images`,`purge bots`,`purge mentions`,`purge files`,`purge embeds`,`purge invites`,`nuke`, `deafen`,`addchannel`, `delchannel`, `delemoji`, `delrole`, `give`, `hide`, `hideall`, `kick`, `lock`, `lockall`, `mute`, `nick`, `role all`, `role bots`, `role humans`, `role`, `rrole bots`, `rrole humans`,`rrole`, `temprole`,`createrole`,`deleterole`,`rename`,`softban`, `steal`, `temprole`, `unban`, `unbanall`, `undeafen`, `unhide`, `unhideall`, `unlock`, `unlockall`, `unmute`,`vckick`, `vclist`, `vcmute`, `slowmode`, `vcunmute`, `warns`, `warn delete`, `warn`,`hackban`,`color`", color=0x2f3136)

        embed_mod.set_author(name=f"{interaction.user}",

                                   icon_url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)

        embed_mod.set_thumbnail(url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024")

        embed_mod.set_footer(icon_url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024", text="Showing Page 7/10")

        if self.values[0] == "Moderation":

            await interaction.response.edit_message(embed=embed_mod)

   #     cog = interaction.client.get_cog("voice2")

    #    title = cog.qualified_name

        

        embed_mod = discord.Embed(title=f"__Voice__", description=f"`j2c setup`,`j2c reset`,`vc kick`,vc kickall`,`vc move`,`vc moveall`,`vc mute`,`vc muteall`,`vc unmute`,`vc unmuteall`,`vc deafen`,`vc deafenall`,`vc undeafen`,`vc undeafenall`,`vcrole humans add`,`vcrole bots add`,`vcrole config`,`vcrole reset`,`vcrole humans remove`,`vcrole bots remove`", color=0x2f3136)

        embed_mod.set_author(name=f"{interaction.user}",

                                   icon_url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)

        embed_mod.set_thumbnail(url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024")

        embed_mod.set_footer(icon_url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024", text="Showing Page 8/10")

        if self.values[0] == "Voice":

            await interaction.response.edit_message(embed=embed_mod)

    #    cog = interaction.client.get_cog("utility22")

    #    title = cog.qualified_name

        

        embed_mod = discord.Embed(title=f"__Utility__", description=f"`donate`,`embed`,`editembed`,`av`,`roleicon`,`banner`,`afk`,`translate`,`userinfo`,`serverinfo`,`banner user`,`banner server`,`ping`,`uptime`,`find discrim`,`find name`,`find id`,`find playing`,`list boosters`,`list admins`,`list roles`,`list inrole`,`list invc`,`list activedev`,`list mods`,`list early`,`list bots`,`list botdev`,`list bans`,`calculator`,`timer`,`poll`,`suggestion`,`bugreport`,`report`,`enlarge`,`remindme`,`reminders`,`delreminder`,`bookmark`,`bookmarks`,`delbookmark`,`snipe`,`embedsnipe`,`multisnipe`,`multieditsnipe`,`editsnipe`,`nick`,`clearnick`,`vote`,`ar create`,`ar delete`,`ar edit`,`ar show`,`counting`,`setcount`", color=0x2f3136)

        embed_mod.set_author(name=f"{interaction.user}",

                                   icon_url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)

        embed_mod.set_thumbnail(url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024")

        embed_mod.set_footer(icon_url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024", text="Showing Page 9/10")

        if self.values[0] == "Utility":

            await interaction.response.edit_message(embed=embed_mod)

     #   cog = interaction.client.get_cog("j2cc")

      #  title = cog.qualified_name

        

        embed_mod = discord.Embed(title=f"__Join To Create__", description=f"`j2c setup`,`j2c reset`", color=0x2f3136)

        embed_mod.set_author(name=f"{interaction.user}",

                                   icon_url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)

        embed_mod.set_thumbnail(url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024")

        embed_mod.set_footer(icon_url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024", text="Showing Page 10/10")

        if self.values[0] == "Join To Create":

            await interaction.response.edit_message(embed=embed_mod)

class dropdown(discord.ui.View):

    def __init__(self, *, timeout=None):

        super().__init__() 

        self.add_item(HelpView())
        
class help(Cog):

    def __init__(self, bot):

        self.bot = bot        

    @commands.command(name="help", aliases=["h"],  help="Shows you the help command of the bot.")

    @commands.cooldown(1, 10, commands.BucketType.user)

    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()

    async def help_command(self, ctx):

        loda = discord.Permissions.all()

        inv = discord.utils.oauth_url(self.bot.user.id, permissions=loda)

        embed = discord.Embed(

        

        description=f"• Global prefix is `?`\n• Total commands: `{len(set(self.bot.walk_commands()))}`\n• [Get Soward](https://discord.com/api/oauth2/authorize?client_id=1013771497157972008&permissions=8&scope=bot) | [Support Server](https://discord.gg/sDwvP73UxS)\n• Type `?help <command | module>` for more info!",

          color=0x2f3136

       )

        embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)

        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024")

        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png?size=1024", text="Made By Prince")

        embed.add_field(name="__Main__", value=f"{antinuke} Antinuke\n{ticket} Ticket\n{selfroles} Selfroles\n{welcome} Welcome\n{extra} Extra", inline=True)

        embed.add_field(name="__Extra__", inline=True, value=f"{games} Games\n{moderation} Moderation\n{voice} Voice\n{utility} Utility\n{j2c} Join To Create")

        embed.timestamp = discord.utils.utcnow()

        b = discord.ui.Button(label="Invite Soward", style=discord.ButtonStyle.link, url=inv)

        b1 = discord.ui.Button(label="Support Server", style=discord.ButtonStyle.link, url="https://discord.gg/sDwvP73UxS")

        b2 = discord.ui.Button(label="Vote Me", style=discord.ButtonStyle.link, url="https://top.gg/bot/1013771497157972008/vote")

        view = View()

        view.add_item(HelpView())

        view.add_item(b)

        view.add_item(b1)

        view.add_item(b2)

        await ctx.reply(embed=embed, view=view, mention_author=True)        
        
        
async def setup(bot):

    await bot.add_cog(help(bot))
    
        
        
        
        