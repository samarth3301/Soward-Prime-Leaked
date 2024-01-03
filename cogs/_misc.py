import discord
import time
import humanfriendly

from prince.embed import error_embed, success_embed
from discord.ext import commands
from config import EMOJIS, MAIN_COLOR, WEBSITE_LINK, SUPPORT_SERVER_LINK, start_time, SUGGESTION_CHANNEL, BUG_REPORT_CHANNEL
from prince.bot import Bot
from prince1.Tools import *

class misc(commands.Cog, description="Commands mostly related to the bot!"):
    def __init__(self, client: Bot):
        self.client = client

    @commands.cooldown(1, 5, commands.BucketType.user)
    @ignore_check()
  #  @commands.is_owner()
    @commands.command(category="misc", help="Check bot's ping.")
    async def pihhhheng(self, ctx):
        time1 = time.perf_counter()
        msg = await ctx.message.reply(embed=discord.Embed(title=f"Pinging... {EMOJIS['loading']}", color=MAIN_COLOR))
        time2 = time.perf_counter()

        db_time1 = time.perf_counter()
   #     await self.client.prefixes.find_one({"_id": ctx.guild.id})
        db_time2 = time.perf_counter()

        shard_text = ""
        for shard, latency in self.client.latencies:
            shard_text += f"Shard {shard}" + ' ' * (3 - len(str(shard))) + f': {round(latency*1000)}ms\n'

        embed = success_embed(
            "<a:th_heartbeat:1017469364712263691>  Pong!",
            f"""
**Basic:**
```yaml
API      : {round(self.client.latency*1000)}ms
Bot      : {round((time2-time1)*1000)}ms
Database : {round((db_time2-db_time1)*1000)}ms
```
**Shards:**
```yaml
{shard_text}
```
            """
        ).set_thumbnail(url=self.client.user.display_avatar.url)
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
        await msg.edit(embed=embed)

    



    @commands.cooldown(1, 2, commands.BucketType.user)
    @ignore_check()
    @commands.command(category="misc", help="Join Soward Prime support server.")
    async def support(self, ctx):
        await ctx.message.reply("https://discord.gg/soward")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(category="misc", help="Check Prince's uptime.",aliases=["up"])
    async def uptime(self, ctx):
        await ctx.message.reply(embed=discord.Embed(
            title="Uptime",
            description=f"I have been up for **{humanfriendly.format_timespan(round(time.time()-start_time))}**",
            color=MAIN_COLOR
        ))

    

    

    @commands.cooldown(3, 120, commands.BucketType.user)
    @commands.command(category="misc", help="Submit a suggestion!")
    @ignore_check()
    async def suggest(self, ctx, *, suggestion=None):
        prefix = ctx.clean_prefix

        if suggestion is None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.message.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Incorrect Usage!",
                f"Please use it like this: `{prefix}suggest <suggestion>`"
            ))

        user_profile = await self.client.get_user_profile_(ctx.author.id)
        stuff = {"suggestions_submitted": user_profile.suggestions_submitted + 1}
        await self.client.update_user_profile_(ctx.author.id, **stuff)

        files = []
        for file in ctx.message.attachments:
            files.append(await file.to_file())

        embed = success_embed("Suggestion!", suggestion
                ).set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url
                ).set_footer(text=f"User ID: {ctx.author.id} | Guild ID: {ctx.guild.id}")

        msg = await self.client.get_channel(SUGGESTION_CHANNEL).send(embed=embed, files=files)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
        await ctx.reply(embed=success_embed(
            f"{EMOJIS['tick_yes']} Suggestion submitted!",
            f"Thank you for submitting the suggestion!\nYou have suggested a total of `{user_profile.suggestions_submitted + 1}` suggestions!"
        ))

    @commands.cooldown(2, 7200, commands.BucketType.user)
    @ignore_check()
    @commands.command(category="misc", aliases=['bug'], help="Report a buggie >~<")
    async def bugreport(self, ctx, *, bug=None):
        prefix = ctx.clean_prefix
        if bug is None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.message.reply(embed=error_embed("Incorrect Usage", f"Please use it like this: `{prefix}bug <bug>`"))
        user_profile = await self.client.get_user_profile_(ctx.author.id)
        stuff = {"bugs_reported": user_profile.bugs_reported + 1}
        await self.client.update_user_profile_(ctx.author.id, **stuff)
        embed = discord.Embed(
            title="Bug",
            description=f"""
```
{bug}
```
            """,
            color=MAIN_COLOR
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
        embed.set_footer(text=f"User ID: {ctx.author.id} | Guild ID: {ctx.guild.id}")
        await self.client.get_channel(BUG_REPORT_CHANNEL).send(embed=embed)
        await ctx.reply(embed=success_embed(
            f"{EMOJIS['tick_yes']} Bug submitted!",
            f"Thank you for submitting the bug!\nYou have reported a total of `{user_profile.bugs_reported + 1}` bugs"
        ))


async def setup(client):
    await client.add_cog(misc(client))
