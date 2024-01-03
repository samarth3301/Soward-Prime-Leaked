import discord
from discord.ext import commands
from discord import app_commands, utils
import os
from datetime import datetime
import aiosqlite
from ._tick import ticket_launcher,confirm
from prince.ticket_view import TicketEmbedView
import json
from discord.ui import *
from prince1.Tools import *
class transcript(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
    
    @discord.ui.button(emoji="<:transcript:1091365540108456046>",label = "Transcript", style = discord.ButtonStyle.blurple, custom_id = "transcript")
    async def transcript(self, interaction: discord.Interaction, button: discord.ui.Button):
      #  await interaction.response.defer()
        if os.path.exists(f"{interaction.channel.id}.md"):
            return await interaction.followup.send(f"A transcript is already being generated!", ephemeral = True)
        with open(f"{interaction.channel.id}.md", 'a') as f:
            f.write(f"# Transcript of {interaction.channel.name}:\n\n")
            async for message in interaction.channel.history(limit = None, oldest_first = True):
                created = datetime.strftime(message.created_at, "%m/%d/%Y at %H:%M:%S")
                if message.edited_at:
                    edited = datetime.strftime(message.edited_at, "%m/%d/%Y at %H:%M:%S")
                    f.write(f"{message.author} on {created}: {message.clean_content} (Edited at {edited})\n")
                else:
                    f.write(f"{message.author} on {created}: {message.clean_content}\n")
            generated = datetime.now().strftime("%m/%d/%Y at %H:%M:%S")
            f.write(f"\n*Generated at {generated} by {interaction.user}*\n*Date Formatting: MM/DD/YY*\n*Time Zone: UTC*")
        with open(f"{interaction.channel.id}.md", 'rb') as f:
            await interaction.followup.send("check dms")
            await interaction.user.send(file = discord.File(f, f"{interaction.channel.name}.md"))
        os.remove(f"{interaction.channel.id}.md")        






# Ticket Class
class Ticket(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    #wakin~
    @commands.Cog.listener()
    async def on_ready(self):
        global selfbot
        selfbot = self.bot.user
        print("Ticket is online.")

    #create ticket command




    
    
                 
			
	
				

    @commands.hybrid_group(name="ticket")
    @commands.has_permissions(administrator=True)
    async def _ticket(self,ctx):
        pass
            
            
            
                

    # add/remove ticket role to sqlite db
    @_ticket.command(name = "role", description = "Adds/Removes a role from the tickets.")
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @app_commands.describe(action = "Do you want to add or remove a current role?", role = "The role you want to add.")
    @app_commands.choices(action = [app_commands.Choice(name = "add role", value = "add"), app_commands.Choice(name = "remove current role", value = "remove")])
    @app_commands.default_permissions(manage_channels = True)
    @app_commands.checks.cooldown(1, 10, key = lambda i: (i.user.id))
    @app_commands.checks.has_permissions(manage_channels = True)
    async def _setup(self, ctx, action: str, role: discord.Role = None):
        async with aiosqlite.connect("db/tickets_role.db") as db: # Open the db
            async with db.cursor() as cursor:
                await cursor.execute("CREATE TABLE IF NOT EXISTS roles (role INTEGER, guild ID)") # Create the table if not exists
                if action == "add": # Add data
                    if role == None: return await ctx.reply("You have to select a role to add it.", ephemeral = True)
                    await cursor.execute("SELECT role FROM roles WHERE guild = ?", (ctx.guild.id,)) # Select role from the same row that has guild.id
                    data = await cursor.fetchone() # Fetch that row
                    if data: # If the row has data (already has a role id)
                        await cursor.execute("UPDATE roles SET role = ? WHERE guild = ?", (role.id, ctx.guild.id,)) # Update it
                    else: # If not
                        await cursor.execute("INSERT INTO roles (role, guild) VALUES (?, ?)", (role.id, ctx.guild.id,)) # Insert it
                    role_embed = discord.Embed(title = "Ticket Role Updated!", description = f"The role **{role}** has been addded to tickets", colour = 0x2f3136)
                    await ctx.reply(embed = role_embed)
                else: # Remove data
                    await cursor.execute("SELECT role FROM roles WHERE guild = ?", (ctx.guild.id,)) # Select role from the same row that has guild.id
                    data = await cursor.fetchone() # Fetch that row
                    if data: # If the row has data (already has a role id)
                        await cursor.execute("DELETE FROM roles WHERE guild = ?", (ctx.guild.id,)) # Delete it
                        role_embed = discord.Embed(title = "Ticket Role Removed!", description = f"The ticket role has been removed.", colour = 0x2f3136)
                        await ctx.reply(embed = role_embed)
                    else: # If not
                        await ctx.reply("I didn't find a ticket role for this server.", ephemeral = True)
            await db.commit()

    # transcript
    @_ticket.command(name="setup", description="setup ticket panel")
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def tick(self,ctx):
        with open ("premium.json","r") as f:

            member = json.load(f)

            prm = member["guild"]
        if str(ctx.guild.id) not in prm:
            embed = discord.Embed(title="You are not a premium user! Please buy premium to use this command!",color=0x2f3136)
            embed.set_thumbnail(url=self.bot.user.avatar)
            embed.set_author(name=ctx.author,icon_url=ctx.author.display_avatar)
            

                    

                    

            

            B = Button(label='Get Premium',emoji="<a:Diamonds:1087431201117179944>" ,style=discord.ButtonStyle.link,url='https://discord.gg/soward')

            view = View()

            view.add_item(B)

            return await ctx.send(embed=embed,view=view)
        embed = discord.Embed(title="create ticket panel with this view",color=0x2f3136)
        await ctx.reply(embed=embed, view=TicketEmbedView(ctx,embed))
                   
    @_ticket.command(name = "sendpanel", aliases=["sp"],description = "send ticket panel.",usage="?sendpanel",help="ticket system")
    @ignore_check()
    @app_commands.default_permissions(manage_guild = True)
    @app_commands.checks.cooldown(3, 60, key = lambda i: (i.guild_id))
    @commands.has_permissions(manage_channels = True)
    async def panel(self,ctx:commands.Context,channel:discord.TextChannel):
       
        em = discord.Embed(title="**Ticket**", description=">>> To create a ticket click the <:Ticket:1017405493477638205> button",color = 0x2f3136)
        em.set_footer(text=f"{self.bot.user.name} - Ticketing without clutter",icon_url=self.bot.user.avatar)
   #         em.set_thumbnail(url=self.bot.user.avatar)
        await channel.send(embed=em,view=ticket_launcher())
			
        await ctx.reply("done", ephemeral=True)
    
    #close ticket
    @_ticket.command(name = "close", description = "Closes the ticket.")
    @ignore_check()
    @app_commands.checks.has_permissions(manage_channels = True)
    async def close(self, ctx):
        if "ticket-for-" in ctx.channel.name:
            embed = discord.Embed(title = "> Are you sure that you want to close this ticket?", color = discord.Colour.blurple())
            await ctx.reply(embed = embed, view = confirm(), ephemeral = True)
        else:
            await ctx.send("> This isn't a ticket!", ephemeral = True)
    @_ticket.command(name="transcript",aliases=["trs"])
    @ignore_check()
    
    async def transcript(self,ctx):
        embed = discord.Embed(description="Click on button below",color=0x2f3136)

        await ctx.reply(embed=embed, view=transcript())
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Ticket(bot))