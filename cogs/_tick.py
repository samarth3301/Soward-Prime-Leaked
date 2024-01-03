import discord
from discord.ext import commands
from discord import app_commands, utils
import os
from datetime import datetime
import aiosqlite
from prince1.Tools import *
#from prince.ticket_view import TicketEmbedView


class ticket_launcher(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 600, commands.BucketType.member)

    @discord.ui.button(label = "Create Ticket", style = discord.ButtonStyle.green, custom_id = "ticket_button", emoji = "<:Ticket:1017405493477638205>")
    async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        ticket = utils.get(interaction.guild.text_channels, name = f"ticket-for-{interaction.user.name.lower().replace(' ', '-')}-{interaction.user.discriminator}")

        if ticket is not None: await interaction.response.send_message(f"You already have a ticket open at {ticket.mention}!", ephemeral = True)
      #  categ = discord.utils.get(guild.categories, name = "tickets")

        

      #  for ch in categ.channels:

        #    if ch.name == f"ticket-for-{interaction.user.name}":

       #         await interaction.response.send_message("You already have a ticket open.", ephemeral=True)
        else:
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
                interaction.user: discord.PermissionOverwrite(view_channel = True, read_message_history = True, send_messages = True, attach_files = True, embed_links = True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
            }
            async with aiosqlite.connect("db/tickets_role.db") as db:
                async with db.cursor() as cursor:
                    await cursor.execute("CREATE TABLE IF NOT EXISTS roles (role INTEGER, guild ID)") # Create the table if not exists
                    await cursor.execute("SELECT role FROM roles WHERE guild = ?", (interaction.guild.id,))
                    data = await cursor.fetchone()
                    if data: ticket_role = data[0]
                    else: ticket_role = None
            if not ticket_role == None:
                ticket_role = interaction.guild.get_role(ticket_role)
                overwrites[ticket_role] = discord.PermissionOverwrite(view_channel = True, read_message_history = True, send_messages = True, attach_files = True, embed_links = True)
                ticket_sentence = discord.Embed(description=f"Thanks for reaching out! The support Team will be here shortly Please be patient.\n\nClick <a:bx_aPepeExit:1017725711273955338> to close the ticket.",color=0x2f3136)
            else:
                ticket_sentence = discord.Embed(title="**Ticket**",description=f"Thanks for reaching out! The support Team will be here shortly Please be patient.\n\nClick <a:bx_aPepeExit:1017725711273955338> to close the ticket.",color=0x2f3136)
            if interaction.guild.icon:
                 ticket_sentence.set_thumbnail(url=interaction.guild.icon)
                 ticket_sentence.set_footer(text="Made By Prine")
            
            if not ticket_role == None:	
                ok = ticket_role.mention
            else:
                ok = ""
            guild = interaction.guild
            category = discord.utils.get(guild.categories, name = "tickets")
            view = main()
            
            if category is None: #If there's no category matching with the `name`
                category = await guild.create_category("tickets") #Creates the category
            try:
                channel = await interaction.guild.create_text_channel(name = f"ticket-for-{interaction.user.name}-{interaction.user.discriminator}", overwrites = overwrites, reason = f"Ticket for {interaction.user}", category = category,topic=f'{interaction.user}')
            except: return await interaction.response.send_message("Ticket creation failed! Make sure I have `Manage Channels` permissions!", ephemeral = True)
            
            await channel.send(ok,embed=ticket_sentence, view =view)
					
            await interaction.response.send_message(f"I've opened a ticket for you at {channel.mention}!", ephemeral = True)
           # await ticket_sentence.pin(embed=ticket_sentence)

class confirm(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
    @discord.ui.button(label = "Confirm", style = discord.ButtonStyle.red, custom_id = "confirm")
    async def confirm_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try: await interaction.channel.delete()
        except: await interaction.response.send_message("Channel deletion failed! Make sure I have `Manage Channels` permissions!", ephemeral = True)

class main(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
    @discord.ui.button(emoji="<a:bx_aPepeExit:1017725711273955338>",label = "Close Ticket", style = discord.ButtonStyle.red, custom_id = "close")
    async def close(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title = "Are you sure you want to close this ticket?", color = 0x2f3136)
        await interaction.response.send_message(embed = embed, view = confirm(), ephemeral = True)
    @discord.ui.button(emoji="<:transcript:1091365540108456046>",label = "Transcript", style = discord.ButtonStyle.blurple, custom_id = "transcript")
    async def transcript(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
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
            await interaction.followup.send(file = discord.File(f, f"{interaction.channel.name}.md"))
        os.remove(f"{interaction.channel.id}.md")

class transcript(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
    @discord.ui.button(label = "Transcript", style = discord.ButtonStyle.blurple, custom_id = "transcript")
    async def transcript(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
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
            f.write(f"\n*Generated at {generated} by {self.bot}*\n*Date Formatting: MM/DD/YY*\n*Time Zone: UTC*")
        with open(f"{interaction.channel.id}.md", 'rb') as f:
            await interaction.followup.send(file = discord.File(f, f"{interaction.channel.name}.md"))
        os.remove(f"{interaction.channel.id}.md")


 
class tix(commands.Cog):
     def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()
   
         

         

         
         
         

         

      
     

        
      
        
          
async def setup(bot):
	await bot.add_cog(tix(bot))



