from discord.ext import commands
from prince.bot import Bot
import discord, requests
import json
#from prince.bot import bot
from discord.ui import View, Button
from discord.ext.commands import Cog
import sqlite3
from ast import literal_eval
import time
from prince1.Tools import*
#from prince1.Tools import is_server_owner

import asyncio
from prince.embed import success_embed, error_embed, edit_msg_multiple_times
from prince.custom_checks import not_opted_out
from prince.confirm import ConfirmationPrompt
from config import (
    DAGPI_KEY, DEFAULT_BANNED_WORDS, EMOJIS, MAIN_COLOR, 
    RED_COLOR, ORANGE_COLOR, PINK_COLOR, CHAT_BID,
    CHAT_API_KEY, PINK_COLOR_2, THINKING_EMOJI_URLS, WEBSITE_LINK, INVISIBLE_COLOR
)
from prince import emote
import humanfriendly
import datetime as datetim
from datetime import datetime
from prince.checks import role_checker
class roles5(Cog):
    def __init__(self, bot):
        self.bot = bot

    

    



    



 
             

    @commands.group(invoke_without_command=True, aliases=["addrole", "giverole"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    @ignore_check()

   # @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.has_guild_permissions(manage_roles=True)
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def role(self,ctx, user: discord.Member=None, *, role: discord.Role=None):
        
        me = ctx.guild.me

        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:

            await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x2f3136))
            
            return

        if ctx.guild.me.top_role <= user.top_role:
            await ctx.reply(embed=discord.Embed(description=f"Error in updating {user.mention}\n my highest role below {user.name}", color=0x2f3136))
            return
        if role.position >= ctx.author.top_role.position:

          await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))
        else:
            if ctx.message.author.guild_permissions.manage_roles:
              guild = ctx.guild
              if role in user.roles:
                  await user.remove_roles(role, reason=f"removed by {ctx.message.author}")
                  await ctx.reply(embed=discord.Embed(description=f"<:ri8:1038487759750438912> updated roles for {user.name}  - {role.name}", color=0x2f3136))
              elif role not in user.roles:
                  await user.add_roles(role, reason=f"added by {ctx.message.author}")
                  await ctx.reply(embed=discord.Embed(description=f"<:ri8:1038487759750438912> updated roles for {user.name} + {role.name}", color=0x2f3136))
    @role.command(name="humans")
    @commands.has_guild_permissions(manage_roles=True)
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def role_humans(self, ctx, *, role: discord.Role):
        """Add a role to all human users."""
        if role.permissions.administrator:
          await ctx.reply(embed=discord.Embed(title="You Can't Use Role With Administrator.", color=0x2f3136))
          return
        if role.permissions.ban_members:
          await ctx.reply(embed=discord.Embed(title="You Can't Use Role with Ban perms", color=0x2f3136))
          return
        if role.permissions.kick_members:
          await ctx.reply(embed=discord.Embed(title="You Can't Use Role with kick perms", color=0x2f3136))
          return
        if role.permissions.mention_everyone:
          await ctx.reply(embed=discord.Embed(title="U Can't Use Role With Mention everyone perms",color=0x2f3136))
          
          return
        if role.permissions.manage_roles:
          await ctx.reply(embed=discord.Embed(title="You Can't Use role with manage_roles pemrs",color=0x2f3136))
          return
        if role.permissions.manage_channels:
          await ctx.reply(embed=discord.Embed(title="You Can't Use Role With Manage_channels Perms",color=0x2f3136))
          return
        if role.position >= ctx.author.top_role.position:

          await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))
          return

        if await role_checker(ctx, role):
            confirmation = ConfirmationPrompt(ctx)
            members = list(filter(lambda x: not x.bot and role not in x.roles, ctx.guild.members))
            await confirmation.confirm(title = "Are You Sure?", description = f"{role.mention} will be added to all {len(members)} members in the server.")    
            if confirmation.confirmed:
                members = list(filter(lambda x: not x.bot and role not in x.roles, ctx.guild.members))
                await confirmation.update(description = f"{emote.loading} | Adding role to {len(members)} humans...")
                reason = f"Action done by {ctx.author} (ID: {ctx.author.id})"
                failed = 0
                for m in members:
                    try:
                        await m.add_roles(role, reason=reason)
                    except:
                        failed += 1
                        continue

                if failed > 0:
                    return await confirmation.update(description = f"I couldn't add roles to {failed} members.")
                await confirmation.update(description = f"{emote.tick} | Successfully added role to {len(members)} members.")
            else:
                await confirmation.update(description = "Not confirmed", hide_author=True, color=0x2f3136)  
 
    @role.command(name="bots")
    @commands.has_guild_permissions(manage_roles=True)
    @ignore_check()
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(manage_roles=True)
    async def role_bots(self, ctx, *, role: discord.Role):
        """Add a role to all bot users."""
        if role.permissions.administrator:
          await ctx.reply(embed=discord.Embed(title="You Can't Use Role With Administrator.", color=0x2f3136))
          return
        if role.permissions.ban_members:
          await ctx.reply(embed=discord.Embed(title="You Can't Use Role with Ban perms", color=0x2f3136))
          return
        if role.permissions.kick_members:
          await ctx.reply(embed=discord.Embed(title="You Can't Use Role with kick perms", color=0x2f3136))
          return
        if role.permissions.mention_everyone:
          await ctx.reply(embed=discord.Embed(title="U Can't Use Role With Mention everyone perms",color=0x2f3136))
          
          return
        if role.permissions.manage_roles:
          await ctx.reply(embed=discord.Embed(title="You Can't Use role with manage_roles pemrs",color=0x2f3136))
          return
        if role.permissions.manage_channels:
          await ctx.reply(embed=discord.Embed(title="You Can't Use Role With Manage_channels Perms",color=0x2f3136))
          return
        if role.position >= ctx.author.top_role.position:

          await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))
          return
        if await role_checker(ctx, role):
            confirmation = ConfirmationPrompt(ctx)
            await confirmation.confirm(title ="Confirmation ",description= f"{role.mention} will be added to all bots in the server.")    
            if confirmation.confirmed:
                members = list(filter(lambda x: x.bot and role not in x.roles, ctx.guild.members))
                await confirmation.update(description = f"{emote.loading} | Adding role to {len(members)} bots...")
                reason = f"Action done by {ctx.author} (ID: {ctx.author.id})"
                failed = 0
                for m in members:
                    try:
                        await m.add_roles(role, reason=reason)
                    except:
                        failed += 1
                        continue

                if failed > 0:
                    return await confirmation.update(description = f"I couldn't add roles to {failed} bots.")
                await confirmation.update(description = f"{emote.tick} | Successfully added role to {len(members)} bots.")
            else:
                await confirmation.update(description = "Not confirmed", hide_author=True, color=0x2f3136)   


    @role.command(name="all")
    @ignore_check()
    @commands.has_permissions(manage_roles=True)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def role_all(self, ctx, *, role: discord.Role):
        """Add a role to everyone on the server"""
        if role.permissions.administrator:
          await ctx.reply(embed=discord.Embed(title="You Can't Use Role With Administrator.", color=0x2f3136))
          return
        if role.permissions.ban_members:
          await ctx.reply(embed=discord.Embed(title="You Can't Use Role with Ban perms", color=0x2f3136))
          return
        if role.permissions.kick_members:
          await ctx.reply(embed=discord.Embed(title="You Can't Use Role with kick perms", color=0x2f3136))
          return
        if role.permissions.mention_everyone:
          await ctx.reply(embed=discord.Embed(title="U Can't Use Role With Mention everyone perms",color=0x2f3136))
          
          return
        if role.permissions.manage_roles:
          await ctx.reply(embed=discord.Embed(title="You Can't Use role with manage_roles pemrs",color=0x2f3136))
          return
        if role.permissions.manage_channels:
          await ctx.reply(embed=discord.Embed(title="You Can't Use Role With Manage_channels Perms",color=0x2f3136))
          return
        if role.position >= ctx.author.top_role.position:

          await ctx.reply(embed=discord.Embed(title="this role above ur top role  u cant add this role", color=0x2f3136))
          return 
        if await role_checker(ctx, role):
            confirmation = ConfirmationPrompt(ctx)
            members = list(filter(lambda x: role not in x.roles, ctx.guild.members))
            await confirmation.confirm(title ="Confirmation ", description = f"{role.mention} will be added to {len(members)} members.")    
            if confirmation.confirmed:
                members = list(filter(lambda x: role not in x.roles, ctx.guild.members))
                await confirmation.update(description = f"{emote.loading} | Adding role to {len(members)} members...")
                reason = f"Action done by {ctx.author} (ID: {ctx.author.id})"
                failed = 0
                for m in members:
                    try:
                        await m.add_roles(role, reason=reason)
                    except:
                        failed += 1
                        continue

                if failed > 0:
                    return await confirmation.update(description = f"I couldn't add roles to {failed} members.")
                await confirmation.update(description = f"{emote.tick} | Successfully added role to {len(members)} members.")
            else:
                await confirmation.update(description = "Not confirmed", hide_author=True, color=0x2f3136)


    @commands.group(invoke_without_command=True, aliases=["removerole", "takerole", "remove"])
   # @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.cooldown(1, 3, commands.BucketType.user)
    @ignore_check()
    @commands.has_guild_permissions(manage_roles=True)
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def rrole(self, ctx, members: commands.Greedy[discord.Member], role: discord.Role):
        """Remove a role from one or multiple users."""
        if await role_checker(ctx, role):
            reason = f"Action done by {ctx.author} (ID: {ctx.author.id})"
            failed = []
            for m in members:
                if role in m.roles:
                    try:
                        await m.remove_roles(role, reason=reason)
                    except:
                        failed.append(str(m))
                        continue

            if len(failed) > 0:
                return await ctx.error(f"I couldn't remove roles from:\n{', '.join(failed)}")
            await ctx.reply(embed=discord.Embed(description=f'{emote.tick} | Successfully Removed {role.mention} from {len(members)} Members'))

    @rrole.command(name="humans") 
    @ignore_check()
    @commands.has_guild_permissions(manage_roles=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def rrole_humans(self, ctx, *, role: discord.Role):
        """Remove a role from all human users."""
        me = ctx.guild.me

        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:

            await ctx.reply(embed=discord.Embed(title=""""```diff\n - You must have Administrator permission.\n - Your top role should be above my top role. \n```""", color=0x42f579))
        else:
            if await role_checker(ctx, role):
                confirmation = ConfirmationPrompt(ctx)
                await confirmation.confirm(title ="Confirmation", description = f"{role.mention} will be removed from all human users in the server.")    
            if confirmation.confirmed:
                members = list(filter(lambda x: not x.bot and role in x.roles, ctx.guild.members))
                await confirmation.update(description = f"{emote.loading} | Removing role from {len(members)} humans...")
                reason = f"Action done by {ctx.author} (ID: {ctx.author.id})"
                failed = 0
                for m in members:
                    try:
                        await m.remove_roles(role, reason=reason)
                    except:
                        failed += 1
                        continue

                if failed > 0:
                    return await confirmation.update(description = f"I couldn't remove roles to {failed} members.")
                await confirmation.update(description = f"{emote.tick} | Successfully removed role to {len(members)} members.")
            else:
                await confirmation.update(description = "Not confirmed", hide_author=True, color=0x2f3136)


    @rrole.command(name="bots")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @ignore_check()
    @commands.has_guild_permissions(manage_roles=True)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def rrole_bots(self, ctx, *, role: discord.Role):
        """Remove a role from all the bots."""
        if await role_checker(ctx, role):
            confirmation = ConfirmationPrompt(ctx)
            await confirmation.confirm(title = "Confirmation", description = f"{role.mention} will be removed from all bot users in the server.")    
            if confirmation.confirmed:
                members = list(filter(lambda x: x.bot and role in x.roles, ctx.guild.members))
                await confirmation.update(description = f"{emote.loading} | Removing role from {len(members)} bots...")
                reason = f"Action done by {ctx.author} (ID: {ctx.author.id})"
                failed = 0
                for m in members:
                    try:
                        await m.remove_roles(role, reason=reason)
                    except:
                        failed += 1
                        continue

                if failed > 0:
                    return await confirmation.update(description = f"I couldn't remove roles to {failed} members.")
                await confirmation.update(description = f"{emote.tick} | Successfully removed role to {len(members)} members.")
            else:
                await confirmation.update(description = "Not confirmed", hide_author=True, color=0x2f3136)


    @rrole.command(name="all")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @ignore_check()
    @commands.has_guild_permissions(manage_roles=True)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def rrole_all(self, ctx, *, role: discord.Role):
        """Remove a role from everyone on the server."""
        me = ctx.guild.me

        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:

            await ctx.reply(embed=discord.Embed(title=""""```diff\n - You must have Administrator permission.\n - Your top role should be above my top role. \n```""", color=0x42f579))
        else:
            if await role_checker(ctx, role):
                confirmation = ConfirmationPrompt(ctx)
                await confirmation.confirm(title = "Confirmation", description = f"{role.mention} will be removed from everyone in the server.")    
            if confirmation.confirmed:
                members = list(filter(lambda x: role in x.roles, ctx.guild.members))
                await confirmation.update(description = f"{emote.loading} | Removing role from {len(members)} members...")
                reason = f"Action done by {ctx.author} (ID: {ctx.author.id})"
                failed = 0
                for m in members:
                    try:
                        await m.remove_roles(role, reason=reason)
                    except:
                        failed += 1
                        continue

                if failed > 0:
                    return await confirmation.update(description = f"I couldn't remove roles to {failed} members.")
                await confirmation.update(description = f"{emote.tick} | Successfully removed role to {len(members)} members.")
            else:
                await confirmation.update(description = "Not confirmed", hide_author=True, color=0x2f3136)
async def setup(bot):
    await bot.add_cog(roles5(bot))