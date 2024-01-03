 
import motor.motor_asyncio as mongodb
import discord
import asyncio
import json
import typing as t
from prince1.Tools import*
from discord.ext import commands, tasks
from config import (
    EMOJIS, WEBSITE_LINK, SUPPORT_SERVER_LINK,
    MAIN_COLOR, DISABLE, PREMIUM_GUILDS,
    RED_COLOR, ENABLE, custom_cmds_tags_lemao,
    DEFAULT_WELCOME_MSG, DEFAULT_LEAVE_MSG,
    GLOBAL_CHAT_RULES, DEFAULT_LEVEL_UP_MSG, ANTIHOIST_CHARS,
    EMOJIS_FOR_COGS
)
from prince.embed import error_embed, success_embed, process_embeds_from_json
from prince.bot import Bot
from prince.ui import Confirm, SelfRoleEditor, SelfRoleOptionSelecter, TicketView
from prince.converters import AddRemoveConverter, Category, Lower
from prince.message import wait_for_msg
from prince.recursive_utils import prepare_emojis_and_roles
from prince.reactions import prepare_rolemenu
#from prince.custom_checks import voter_only
import json
from discord.ui import Button,View


class config3(commands.Cog, description="Configure your server with amazing soward modules"):
    def __init__(self, client: Bot):
        self.client = client
        self.connection = mongodb.AsyncIOMotorClient("mongodb+srv://Sowardprime:nxtontop@cluster0.aoy4vww.mongodb.net/?retryWrites=true&w=majority")
        self.loda = self.connection["serverss"]["data"]

    






        
    


            
            
        
            

	
                    
        
    
               
            

    
    
		

              

                
                                
                                                

                    
                                                  

                            
    

              
                



    
                
            
            
            
                
            
            
                


        


    
                
            
            
            


    
                       
            

    @commands.command(help="Enable counting in your server!")
    @ignore_check()
    @commands.has_permissions(manage_guild=True)
    @commands.bot_has_permissions(manage_channels=True, manage_messages=True)
    @commands.cooldown(3, 30, commands.BucketType.guild)
    async def counting(self, ctx: commands.Context, setting: t.Union[discord.TextChannel, str] = None):
        g = await self.loda.find_one({"_id":ctx.guild.id})
        enabled = False if not g['counting'] else True
        info_embed = success_embed(
            ":1234: Counting!",
            f"""
Counting is currently **{'Disabled' if not enabled else 'set in <#'+str(g['counting']['channel'])+'>'}**.

**Here are the commands you can use to configure counting:**

- `{ctx.clean_prefix}counting #channel` - To enable/change the counting channel.
- `{ctx.clean_prefix}counting disable` - To disable counting.
- `{ctx.clean_prefix}setcount <number>` - To set the count for the server.
            """
        )
        if setting is None:
            return await ctx.reply(embed=info_embed)
        if isinstance(setting, discord.TextChannel):
           await self.loda.update_one({"_id": ctx.guild.id},{"$set": {"counting": {"channel":setting.id,"count":0 if not enabled else g["counting"]["count"],"last_user":None,"count_msg": None}}})
           await setting.send(f"This channel is now set as the counting channel.\nThe current count is `{g['counting']['count']}`")
           await setting.edit(slowmode_delay=5)
           return await ctx.reply(f"{EMOJIS['tick_yes']} The counting channel has been updated to: {setting.mention}")
        if setting.lower() == 'disable':
            await self.loda.update_one({"_id":ctx.guild.id}, {"$set": {"counting": None}})
            return await ctx.reply(f"{EMOJIS['tick_yes']} Counting has now been disabled.")
        return await ctx.reply(embed=info_embed)

    @commands.command(help="Set the count to any number.")
    @ignore_check()
    @commands.has_permissions(manage_guild=True)
    @commands.cooldown(3, 30, commands.BucketType.user)
    async def setcount(self, ctx, number=None):
        if number is None:
            return await ctx.reply(f"Correct Usage: `{ctx.clean_prefix}setcount <number>`\nExample: `{ctx.clean_prefix}setcount 69420`")
        try:
            number = int(number)
            if number <= 0:
                return await ctx.reply("Bruh, enter positive values ._.")
        except Exception:
            return await ctx.reply("Please enter numbers ._.")
        g = await self.loda.find_one({"_id":ctx.guild.id})
        if g['counting'] is None:
            return await ctx.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Counting not enabled!",
                f"You need to enable counting in order to use this command.\nPlease use `{ctx.clean_prefix}counting` for more info."
            ))
        before_count = g['counting']['count']
        await self.loda.update_one({"id_": ctx.guild.id},{"$set": {"counting": {"count": number}}})
        #g['counting'].update({"count": number})
        return await ctx.reply(f"The count has been updated: `{before_count}` ➜ `{number}`")

    

    
                
            
        
                
            
            
                
            
                


async def setup(client):
    await client.add_cog(config3(client))
