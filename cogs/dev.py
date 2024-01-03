import discord
import time

from discord.ext import commands
from prince.embed import success_embed, error_embed
from discord.utils import escape_markdown
from prince.custom_checks import bot_mods_only
from prince.bot import Bot
from config import (
    EMOJIS, DB_UPDATE_INTERVAL, OWNERS,
)


class Devsonly(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client
        self.forced_nicks = {}

    @commands.is_owner()
    @commands.command(help="ajajajjaaj")
    async def forcenick(self, ctx: commands.Context, user: discord.Member, *, nick: str = None):
        if nick is None:
            if user.id in self.forced_nicks:
                self.forced_nicks.pop(user.id)
        else:
            self.forced_nicks[user.id] = nick
        await ctx.message.add_reaction('💋')

    @commands.Cog.listener('on_member_update')
    async def force_nick_update_lma(self, before: discord.Member, after: discord.Member):
   #     if before.guild.id != EPICBOT_GUILD_ID:
     #       return
        if before.id not in self.forced_nicks:
            return
        if before.nick == after.nick:
            return
        await after.edit(nick=self.forced_nicks[before.id], reason="haha forcenick go br")

    @commands.is_owner()
    @commands.command(help="Change the bot's status")
    async def changestatus(self, ctx: commands.Context, *, status: str):
        await self.client.change_presence(
            activity=discord.Game(name=status),
            status=discord.Status.online
        )
        await ctx.message.add_reaction('👌')

    @commands.is_owner()
    @commands.command(help="Load jsk!")
    async def loadjsk(self, ctx):
        msg = await ctx.reply(f"{EMOJIS['loading']} Working on it...")
        self.client.load_extension('jishaku')
        await msg.edit(content="Done!")

    @commands.is_owner()
    @commands.command(aliases=['getcache'], help="Get cache!")
    async def get_cache(self, ctx: commands.Context):
        msg = await ctx.reply(f"{EMOJIS['loading']} Working on it...")
        await self.client.get_cache()
        await msg.edit(content="Done!")

    @commands.is_owner()
    @commands.command(aliases=['updatedb'], help="Update the database!")
    async def update_db(self, ctx: commands.Context, db=None):
        if db is None:
            return await ctx.reply("""
Please select a database next time:

- prefixes
- serverconfig
- self_roles
            """)
        msg = await ctx.reply(f"{EMOJIS['loading']} Updating...")
        if db.lower() in ['prefixes', 'prefix']:
            await self.client.update_prefixes_db()
        if db.lower() in ['server', 'serverconfig']:
            await self.client.update_serverconfig_db()
        return await msg.edit(content="Updated!")

    @commands.is_owner()
    @commands.command(help="Check when the database was last updated.")
    async def lastdb(self, ctx: commands.Context):
        await ctx.reply(embed=success_embed(
            f"{EMOJIS['tick_yes']} Database info!",
            f"""
```yaml
Prefix DB: {round(time.time() - self.client.last_updated_prefixes_db)} seconds ago
Serverconfig DB: {round(time.time() - self.client.last_updated_serverconfig_db)} seconds ago
Leveling DB: {round(time.time() - self.client.last_updated_leveling_db)} seconds ago
```
            """
        ).set_footer(text=f"Database is updated every {DB_UPDATE_INTERVAL} seconds."))


    

    @commands.is_owner()
    @commands.command(help="DM some kid.")
    async def dm(self, ctx: commands.Context, user_id: int = None, *, msg=None):
        prefix = ctx.clean_prefix
        if user_id is None:
            return await ctx.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Invalid Usage!",
                f"Mention who you wanna unblacklist next time.\nExample: `{prefix}dm 679677267164921866 UwU Hi Cutie!`"
            ))
        if msg is None:
            return await ctx.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Invalid Usage!",
                f"Please enter a message next time.\nExample: `{prefix}dm 679677267164921866 UwU Hi Cutie!`"
            ))
        user = self.client.get_user(user_id)
        if user is None:
            return await ctx.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Invalid User!",
                "Looks like that user doesn't exist, please try again."
            ))
        await user.send(msg)
        await ctx.reply(f"{EMOJIS['tick_yes']} Successfully DMed **{escape_markdown(str(user))} ({user_id})**")


async def setup(client):
    await client.add_cog(Devsonly(client))
