import discord

from discord.ext import commands
from typing import Union, Optional
from prince.embed import error_embed, success_embed
from config import EMOJIS, MAIN_COLOR, SUPPORT_SERVER_LINK
from prince.bot import Bot
from prince.ui import Confirm, Paginator, PaginatorText
from prince.converters import Lower
from prince.flags import StickerFlags
from io import BytesIO
from prince1.Tools import *
from aiohttp import ClientSession
import re 
EMOJI_REGEX = r'<(?P<animated>a?):(?P<name>[a-zA-Z0-9_]{2,32}):(?P<id>[0-9]{18,22})>'
class emojis(commands.Cog, description="Emoji related commands!"):
    def __init__(self, client:Bot):
        self.client = client

    @commands.cooldown(2, 10, commands.BucketType.user)
    @blacklist_check()
    @ignore_check()
    @commands.command(help="Enlarge an emoji.")
    async def enlargejahs(self, ctx, emoji: Union[discord.Emoji, discord.PartialEmoji, str] = None):
        prefix = ctx.clean_prefix
        if emoji is None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Invalid Usage!",
                f"Please enter an emoji to enlarge.\nCorrect Usage: `{prefix}enlarge <emoji>`"
            ))
        if isinstance(emoji, str):
            raise commands.EmojiNotFound(emoji)
        await ctx.reply(emoji.url)

    @commands.cooldown(2, 10, commands.BucketType.user)
    @ignore_check()
    @commands.command(help="Search for emojis!", aliases=['searchemoji', 'findemoji', 'emojifind'])
    @blacklist_check()
    async def emojisearch(self, ctx: commands.Context, name: Lower = None):
        if not name:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(f"Please enter a query!\n\nExample: `{ctx.clean_prefix}emojisearch cat`")
        emojis = [str(emoji) for emoji in self.client.emojis if name in emoji.name.lower() and emoji.is_usable()]
        if len(emojis) == 0:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(f"Couldn't find any results for `{name}`, please try again.")

        paginator = commands.Paginator(prefix="", suffix="", max_size=500)
        for emoji in emojis:
            paginator.add_line(emoji)
        await ctx.reply(f"Found `{len(emojis)}` emojis.")
        if len(paginator.pages) == 1:
            return await ctx.send(paginator.pages[0])
        view = PaginatorText(ctx, paginator.pages)
        await ctx.send(paginator.pages[0], view=view)

    @commands.cooldown(2, 10, commands.BucketType.user)
    @ignore_check()
    @blacklist_check()
    @commands.command(help="Search for stickers!", aliases=['searchsticker', 'findsticker', 'stickerfind'])
    async def stickersearch(self, ctx: commands.Context, name: Lower = None):
        if not name:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(f"Please enter a query!\n\nExample: `{ctx.clean_prefix}stickersearch cat`")
        stickers = [sticker for sticker in self.client.stickers if name in sticker.name.lower()]
        if len(stickers) == 0:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(f"Couldn't find any results for `{name}`, please try again.")
        embeds = []
        for sticker in stickers:
            embeds.append(discord.Embed(
                title=sticker.name,
                description=sticker.description,
                color=MAIN_COLOR,
                url=sticker.url
            ).set_image(url=sticker.url))
        await ctx.reply(f"Found `{len(embeds)}` stickers.")
        if len(embeds) == 1:
            return await ctx.send(embed=embeds[0])
        view = Paginator(ctx, embeds)
        return await ctx.send(embed=embeds[0], view=view)

    @commands.command(help="Steal emojis!", aliases=['steal-emoji', 'stwalemoji'])
    @commands.has_permissions(manage_emojis=True)
    @commands.bot_has_permissions(manage_emojis=True)
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(7, 15, commands.BucketType.user)

  #  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)

    @commands.guild_only()
    async def steal(self, ctx, emojis: commands.Greedy[Union[discord.PartialEmoji, discord.Emoji]] = None):
        ref = ctx.message.reference
        prefix = ctx.clean_prefix
        
        if ref:
            msg = await ctx.fetch_message(ref.message_id)
            emojis = re.findall(EMOJI_REGEX, msg.content)
            stolen_emojis = ""
            fail_emojis = ""
            s = await ctx.send(f"stealing please wait... {EMOJIS['loading']}")
            for emoji in emojis:
                name = emoji[1]
                ext = "gif" if emoji[0] else "png"
                image_url = f"https://cdn.discordapp.com/emojis/{emoji[2]}.{ext}"
                
                async with ClientSession() as session:
                   async with session.get(image_url) as resp:
                        image = await resp.read()
                        try:
                        
                           op = await ctx.guild.create_custom_emoji(name=name, image=image)
                           stolen_emojis += f"{op}"
                        except Exception:
                           fail_emojis += f"`{op.name}` "
                      
        
            await s.edit(content=f"<:Icons_correct:1017402689027592222> | Successfully stole emoji(s), {stolen_emojis}{' and failed to steal '+fail_emojis if len(fail_emojis) > 0 else ''}",embed=None,view=None)
            return
        else:
            if emojis is None:
                return await ctx.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Invalid Usage!",
                f"Please enter some emojis to steal.\n\n**Example:** {prefix}steal :princeop: ..."
            ))
        uploaded_emojis = ""
        failed_emojis = ""

        m = await ctx.reply(f"stealing please wait... {EMOJIS['loading']}")

        for emoji in emojis:
            if isinstance(emoji, discord.PartialEmoji):
                try:
                    emo = await ctx.guild.create_custom_emoji(
                        name=emoji.name,
                        image=await emoji.read(),
                        reason=f"steal command used by {ctx.author} ({ctx.author.id})"
                    )
                    uploaded_emojis += f"{emo} "
                except Exception:
                    failed_emojis += f"`{emoji.name}` "
            else:
                view = Confirm(context=ctx)
                await m.edit(
                    content="",
                    embed=success_embed(
                        "Is this the emoji you wanted?",
                        f"The name `{emoji.name}` corresponds to this emote, do u want to steal this?"
                    ).set_image(url=emoji.url),
                    view=view
                )
                await view.wait()
                if view.value is None:
                    await m.edit(
                        content="",
                        embed=error_embed(
                            "You didn't respond in time.",
                            f"Skipped this emoji. stealing other emojis... {EMOJIS['loading']}"
                        ),
                        view=None
                    )
                elif not view.value:
                    await m.edit(
                        content="",
                        embed=success_embed(
                            f"{EMOJIS['tick_yes']} Alright!",
                            "Skipped that emote."
                        ),
                        view=None
                    )
                else:
                    await m.edit(
                        content="",
                        embed=discord.Embed(
                            title=f"{EMOJIS['tick_yes']} Ok, stealing...",
                            color=MAIN_COLOR
                        ),
                        view=None
                    )
                    try:
                        emo = await ctx.guild.create_custom_emoji(
                            name=emoji.name,
                            image=await emoji.read(),
                            reason=f"steal command used by {ctx.author} ({ctx.author.id})"
                        )
                        uploaded_emojis += f"{emo} "
                    except Exception:
                        failed_emojis += f"`{emoji.name}` "

        await m.edit(
            content=f"I have stealed {uploaded_emojis}{' and failed to steal '+failed_emojis if len(failed_emojis) > 0 else ''}",embed=None,view=None)
                
    @commands.command(help="Create a sticker in your server!", aliases=['makesticker', 'create_sticker', 'make_sticker', 'create-sticker', 'make-sticker'])
    @commands.cooldown(3, 10, commands.BucketType.user)
    @ignore_check()
    @commands.has_permissions(manage_emojis_and_stickers=True)
    @commands.bot_has_permissions(manage_emojis_and_stickers=True)
    async def sticker(self, ctx: commands.Context, emoji:discord.PartialEmoji = None, *, emoji_flags: Optional[StickerFlags] = None):
        if emoji is not None:
            file = discord.File(BytesIO(await emoji.read()), filename=f"{emoji.name}.gif")
        else:
            if len(ctx.message.attachments) == 0:
                ctx.command.reset_cooldown(ctx)
                return await ctx.reply(f"Please mention an emoji/upload a file to make a sticker!\n\nExample: `{ctx.clean_prefix}make-sticker :dance:`")
            else:
                file = await ctx.message.attachments[0].to_file()

        if not emoji_flags:
            name = file.filename.split(".")[0]
            description = f"Uploaded by {ctx.author}"
            emoji = name
        else:
            name = emoji.name if emoji_flags.name is None else emoji_flags.name if len(emoji_flags.name) > 1 else "name"
            description = emoji_flags.description if emoji_flags.description is not None else f"Uploaded by {ctx.author}"
            emoji = emoji_flags.emoji or name

        try:
            sticker = await ctx.guild.create_sticker(
                name=name,
                description=description,
                emoji=emoji,
                file=file,
                reason=f"Command used by {ctx.author}"
            )
            return await ctx.reply(f"{EMOJIS['tick_yes']}Sticker uploaded!", stickers=[sticker])
        except Exception as e:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(f"Sticker upload failed. Error: `{e}`\n\nIf this was unexpected please report it in our support server {SUPPORT_SERVER_LINK}")



            


async def setup(client):
    await client.add_cog(emojis(client))
