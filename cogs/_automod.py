import discord
import asyncio
from prince.ui import SelfRoleOptionSelecter
from discord.ext import commands
from discord.utils import escape_markdown
from humanfriendly import format_timespan
from typing import Optional, Union

from prince.bot import Bot
from prince.message import wait_for_msg
from prince.time import convert
from prince.random import gen_random_string
from prince.embed import success_embed, error_embed

from prince.ui import Confirm
from config import (
    BADGE_EMOJIS, EMOJIS, RED_COLOR
)
#from prince.custom_checks import voter_only
from prince1.Tools import*
class mod(commands.Cog):
    def __init__(self,client):
        self.client = client
    
         

    @commands.cooldown(2, 15, commands.BucketType.user)
    @ignore_check()
    @commands.has_guild_permissions(kick_members=True)
    @commands.command(help="Warn a user.")
    async def warn(self, ctx: commands.Context, user: discord.Member = None, *, reason='No Reason Provided'):
        custom_prefix = ctx.clean_prefix
        if user is None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.message.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Invalid Usage!",
                f"Please mention a user next time.\nExample: `{custom_prefix}warn @egirl spamming`"
            ))
        if user == ctx.author:
            ctx.command.reset_cooldown(ctx)
            return await ctx.message.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Bruh!",
                "You cannot warn yourself."
            ))
        if user == self.client.user:
            ctx.command.reset_cooldown(ctx)
            return await ctx.message.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Bruh!",
                "You cannot warn me."
            ))
        if user.bot:
            ctx.command.reset_cooldown(ctx)
            return await ctx.message.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Bruh!",
                "You cannot warn bots."
            ))
        if int(ctx.author.top_role.position) <= int(user.top_role.position):
            ctx.command.reset_cooldown(ctx)
            return await ctx.message.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Error!",
                "You cannot warn a mod/admin."
            ))
        if len(reason) > 500:
            ctx.command.reset_cooldown(ctx)
            return await ctx.message.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Too long!",
                "The reason provided was too long, please try again."
            ))
        random_generated_id = gen_random_string(20)
        await self.client.warnings.insert_one({
            "_id": random_generated_id,
            "user_id": user.id,
            "guild_id": ctx.guild.id,
            "moderator": ctx.author.id,
            "reason": reason
        })
        try:
            await user.send(embed=error_embed(
                "You have been warned!",
                f"You were warned from the server: **{escape_markdown(str(ctx.guild))}**"
            ).add_field(name="Moderator:", value=f"{ctx.author.mention} - {escape_markdown(str(ctx.author))}", inline=False
            ).add_field(name="Reason:", value=reason, inline=False
            ).set_footer(text=f"Warn ID: {random_generated_id}"))
        except Exception as e:
            print(e)
        await ctx.message.reply(embed=success_embed(
            f"{EMOJIS['tick_yes']} User Warned!",
            f"**{escape_markdown(str(user))}** has been warned!"
        ).set_footer(text=f"Warn ID: {random_generated_id}"))

    @commands.cooldown(2, 10, commands.BucketType.user)
    @ignore_check()
    @commands.has_guild_permissions(kick_members=True)
    @commands.command(aliases=['removewarn', 'deletewarn', 'removewarning', 'deletewarning', 'delwarning'], help="Delete a warning.")
    async def delwarn(self, ctx: commands.Context, warn_id=None):
        prefix = ctx.clean_prefix
        if warn_id is None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.message.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Invalid Usage!",
                f"Please enter a warn ID.\nExample: `{prefix}delwarn N3vE4g0nN4g1V3y0UUp`"
            ))
        ah_yes = await self.client.warnings.find_one({
            "_id": warn_id,
            "guild_id": ctx.guild.id
        })
        if ah_yes is None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.message.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Not found!",
                "The provided warning ID is Invalid.\nPlease enter a valid warning ID."
            ))
        await self.client.warnings.delete_one({"_id": warn_id})
        return await ctx.message.reply(embed=success_embed(
            f"{EMOJIS['tick_yes']} Warning Removed!",
            f"The warning: `{warn_id}` was deleted!"
        ).add_field(
            name="Some info on the warning:",
            value=f"""
```yaml
User Warned: {self.client.get_user(ah_yes['user_id'])}
Moderator: {self.client.get_user(ah_yes['moderator'])}
Reason: {ah_yes['reason']}
```
            """,
            inline=False
        ))

    @commands.cooldown(1, 15, commands.BucketType.user)
    @ignore_check()
    @commands.has_guild_permissions(kick_members=True)
    @commands.command(aliases=['warnings'], help="Check warnings of a user!")
    async def warns(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author
        ah_yes = self.client.warnings.find({
            "user_id": user.id,
            "guild_id": ctx.guild.id
        })
        uwu = await ah_yes.to_list(length=None)
        if len(uwu) == 0:
            return await ctx.message.reply(embed=success_embed(
                f"{EMOJIS['tick_yes']} Warnings!",
                f"**{escape_markdown(str(user))}** has no warnings."
            ))
        uwu_embed = success_embed(
            f"{EMOJIS['tick_yes']} Warnings",
            f"Warnings of **{escape_markdown(str(user))}**."
        )
        if len(uwu) <= 25:
            for e in uwu:
                uwu_embed.add_field(
                    name=f"Warning ID: `{e['_id']}`",
                    value=f"""
```yaml
Moderator: {self.client.get_user(e['moderator'])}
Reason: {e['reason']}
```
                    """,
                    inline=False
                )
        if len(uwu) > 25:
            i = 0
            for e in uwu:
                if i == 25:
                    break
                uwu_embed.add_field(
                    name=f"Warning ID: `{e['_id']}`",
                    value=f"""
```yaml
Moderator: {self.client.get_user(e['moderator'])}
Reason: {e['reason']}
```
                    """,
                    inline=False
                )
                i += 1
        return await ctx.message.reply(embed=uwu_embed)

    
    
        
        
        




async def setup(client):
    await client.add_cog(mod(client))
