
from prince1.Tools import *
import discord
import datetime
import time
import asyncio
import aiohttp
import json
import re
from discord.ui import Button, View
from simpcalc import simpcalc
from config import EMOJIS, MAIN_COLOR, UD_API_KEY, RED_COLOR, WEATHER_API_KEY
from prince.embed import success_embed, error_embed, process_embeds_from_json
from prince.time import convert
from prince.random import gen_random_string
from discord.ext import commands, tasks
from discord.utils import escape_markdown
from prince.ui import Confirm, Paginator
from prince.bot import Bot
from prince.message import wait_for_msg
import typing
from prince.ticket_view import TicketEmbedView
class pollButtons(discord.ui.View):
    def __init__(self, *, timeout = None):
        super().__init__(timeout = timeout)
    @discord.ui.button(label = "Yes", style = discord.ButtonStyle.blurple, emoji = "<a:Soward_yes:1108074934921613443>")
    async def poll_yes_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        global upvotes, downvotes, voted
        if interaction.user in voted:
            await interaction.response.send_message("You've already voted once.", ephemeral = True)
        else:
            upvotes = upvotes + 1
            voted.append(interaction.user)
            emb = discord.Embed(title = poll_title, description = poll_description)
            emb.set_author(name = f"Poll by {poll_author}", icon_url = poll_avatar)
            emb.set_footer(text = f"{upvotes} Yes | {downvotes} No")
            view = pollButtons()
            await interaction.message.edit(embed = emb, view = view)
            await interaction.response.send_message("Voted.", ephemeral = True)
    #no button
    @discord.ui.button(label = "No", style = discord.ButtonStyle.blurple, emoji = "<a:Soward_no:1108074761566826516>")
    async def sugg_downvote(self, interaction: discord.Interaction, button: discord.ui.Button):
        global upvotes, downvotes, voted
        if interaction.user in voted:
            await interaction.response.send_message("You've already voted once.", ephemeral = True)
        else:
            downvotes = downvotes + 1
            voted.append(interaction.user)
            emb = discord.Embed(title = poll_title, description = poll_description)
            emb.set_author(name = f"Poll by {poll_author}", icon_url = poll_avatar)
            emb.set_footer(text = f"{upvotes} Yes | {downvotes} No")
            view = pollButtons()
            await interaction.message.edit(embed = emb, view = view)
            await interaction.response.send_message("Voted.", ephemeral=True)

class poll(commands.Cog, description="Commands that make your Discord experience nicer!"):
    def __init__(self, client: Bot):
        self.client = client
        
        self.regex = re.compile(r"(\w*)\s*(?:```)(\w*)?([\s\S]*)(?:```$)")
        self.guild = discord.Guild






        
    

      


            

   
             



	
    

        
        

                


	
     
    
                

			
                    

    
        
    @commands.command(usage="?poll <title> <description>") 
    @commands.has_permissions(manage_messages=True)
    @ignore_check()
    async def poll(self, ctx, title: str, *,description: str):
        global poll_title, poll_description, poll_author, poll_avatar, upvotes, downvotes, voted
        voted = []
        upvotes = 0
        downvotes = 0
        poll_title = title
        poll_description = description
        poll_author = ctx.author
        poll_avatar = ctx.author.avatar.url
        view = pollButtons()
        emb = discord.Embed(title = poll_title, description = poll_description,color=0x2f3136)
        emb.set_author(name = f"Poll by {poll_author}", icon_url = poll_avatar)
        emb.set_footer(text = f"{upvotes} Yes | {downvotes} No")
        await ctx.send(embed=emb,view=view) 
        
    
            
                
   



async def setup(client):
	await client.add_cog(poll(client))

