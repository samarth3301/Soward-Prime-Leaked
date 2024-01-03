import discord

import traceback

import json

from discord.ext import commands

from humanfriendly import format_timespan

from config import (

    OWNERS, EMOJIS, MAIN_COLOR, SUPPORT_SERVER_LINK,

    VOTE_LINK, RED_COLOR,SOWARD_PREMIUM_ROLE

)

#from utils.random import gen_random_string

from prince.custom_checks import NotVoted, NotBotMod, OptedOut, PrivateCommand, ComingSoon,NotPremium

from prince.converters import ImportantCategory, InvalidTimeZone, InvalidCategory

#from utils.exceptions import AutomodModuleAlreadyEnabled, AutomodModuleNotEnabled, MusicGone, InvalidUrl

#from utils.bot import EpicBot

from prince.embed import (

    replace_things_in_string_fancy_lemao,

    process_embeds_from_json,

    error_embed, success_embed

)

class ErrorHandling(commands.Cog):

    def __init__(self, client):

        self.client = client

        self.cd_mapping = commands.CooldownMapping.from_cooldown(5, 20, commands.BucketType.user)

        self.nice_spam_idiot = commands.CooldownMapping.from_cooldown(2, 10, commands.BucketType.user)

    

    @commands.Cog.listener()

    async def on_command_error(self, ctx: commands.Context, error):

        bucket_pain = self.nice_spam_idiot.get_bucket(ctx.message)

        retry_after_pain = bucket_pain.update_rate_limit()

        prefix = ctx.clean_prefix

        if retry_after_pain:

            return

    #    if isinstance(error, commands.CommandNotFound):

   #         bucket = self.cd_mapping.get_bucket(ctx.message)

            retry_after = bucket.update_rate_limit()

            if retry_after and ctx.author.id not in OWNERS:

                return await ctx.reply(embed=error_embed(

                    f"{EMOJIS['tick_no']} Calm down!",

                    f"Please try again after **{format_timespan(round(error.retry_after, 2))}**."),

                    delete_after=5

                )

    #        await self.process_custom_cmds(ctx, ctx.invoked_with)
     #   elif isinstance(error, commands.MaxConcurrencyReached):

      #      await ctx.reply("This Command is already going on, let it finish and retry after")
        elif isinstance(error, commands.CommandOnCooldown):

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['tick_no']} Calm down!",

                f"Please try again after **{format_timespan(round(error.retry_after, 2))}**.".format(error.retry_after)),

                delete_after=5

            )

        elif isinstance(error, commands.MaxConcurrencyReached):

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['tick_no']} Limit reached!",

                f"An instance of this command is already running...\nYou can only run `{error.number}` instances at the same time."

            ))

        elif isinstance(error, commands.MissingPermissions):

            if ctx.author.id == 558861606063308822:

                return await ctx.reinvoke()

            ctx.command.reset_cooldown(ctx)

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['tick_no']} Nah bro!",

                "You need **{}** perms to run this command.".format(' '.join(error.missing_permissions[0].split('_')).title())

            ))

        elif isinstance(error, commands.BotMissingPermissions):

            ctx.command.reset_cooldown(ctx)

            if error.missing_permissions[0] == 'send_messages':

                return

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['tick_no']} Error!",

                "I am missing **{}** permissions.".format(' '.join(error.missing_permissions[0].split('_')).title())

            ))

        elif isinstance(error, commands.NSFWChannelRequired):

            ctx.command.reset_cooldown(ctx)

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['tick_no']} Go away horny!",

                "This command can only be used in a **NSFW** channel."

            ))

   #     elif isinstance(error, commands.NotOwner):

        #    await self.client.get_channel(1088105620156194886).send(

         #       embed=discord.Embed(

        #            title="Someone tried to use Owner only command!",

   #                 description=f"```{ctx.message.content}```",

        #            color=MAIN_COLOR

        #        ).add_field(name="User", value=f"{ctx.author.mention}```{ctx.author} ({ctx.author.id})```", inline=False)

      #          .add_field(name="Server", value=f"```{ctx.guild} ({ctx.guild.id})```", inline=False)

      #      )

      #      await ctx.reply(embed=error_embed(

       #         f"{EMOJIS['tick_no']} No!",

       #         "Sowwi cutie but you cannot use this command!~"

     #       ))

        elif isinstance(error, commands.MemberNotFound):

            ctx.command.reset_cooldown(ctx)

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['tick_no']} Not found!",

                "I wasn't able to find **{}**, please try again.".format(error.argument)

            ))

        elif isinstance(error, commands.UserNotFound):

            ctx.command.reset_cooldown(ctx)

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['tick_no']} Not found!",

                "I wasn't able to find **{}**, please try again.".format(error.argument)

            ))

        elif isinstance(error, commands.ChannelNotFound):

            ctx.command.reset_cooldown(ctx)

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['tick_no']} Not found!",

                "No channel named **{}** was found, please try again.".format(error.argument)

            ))

        elif isinstance(error, commands.RoleNotFound):

            ctx.command.reset_cooldown(ctx)

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['tick_no']} Not found!",

                "No role named **{}** was found, please try again.".format(error.argument)

            ))

        elif isinstance(error, commands.EmojiNotFound):

            ctx.command.reset_cooldown(ctx)

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['tick_no']} Not found!",

                f"I wasn't able to find any emoji named: `{error.argument}`."

            ))

        elif isinstance(error, commands.PartialEmojiConversionFailure):

            ctx.command.reset_cooldown(ctx)

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['tick_no']} Not found!",

                f"I wasn't able to find any emoji named: `{error.argument}`."

            ))

        elif isinstance(error, NotVoted):

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['weirdchamp']} Voter only!",

                f"This command is restricted to voters only.\nClick **[here]({VOTE_LINK})** to vote!"

            ))

        elif isinstance(error, NotBotMod):

            ctx.command.reset_cooldown(ctx)

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['tick_no']} No!",

                "Only bot moderators can use this command!"

            ))

        elif isinstance(error, NotPremium):

            ctx.command.reset_cooldown(ctx)

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['tick_no']} **PREMIUM USERS ONLY!**",

                "Only premium user can use this command\n\n join [support server](https://discord.gg/yxXeVEpdbP) for buy premium!"

            ))

        elif isinstance(error, OptedOut):

            ctx.command.reset_cooldown(ctx)

            await ctx.reply(embed=error_embed(

                f"{EMOJIS['tick_no']} No!",

                f"You cannot snipe, because you opted out!\nPlease use `{prefix}optout` to be able to snipe again."

            ))

    #    elif isinstance(error, InvalidTimeZone):

    #        ctx.command.reset_cooldown(ctx)

    #        await ctx.reply(embed=error_embed(

     #           f"{EMOJIS['tick_no']} Invalid Timezone!",

   #             f"Please use a valid timezone.\nClick **[here](https://github.com/nirlep5252/epicbot/tree/main/other/timezones.txt)** to see the list of valid timezones.\n\nYou can also set your timezone using `{ctx.clean_prefix}settimezone <timezone>` for all commands."

   #         ))

     #   elif isinstance(error, InvalidCategory):

        #    ctx.command.reset_cooldown(ctx)

         #   await ctx.reply(embed=error_embed(

            #    f"{EMOJIS['tick_no']} Invalid Category!",

             #   f"The category `{error.category}` is not a valid category!\nPlease use `{prefix}help` to see the list of valid categories."

          #  ))

     #   elif isinstance(error, ImportantCategory):

           # ctx.command.reset_cooldown(ctx)

         #   await ctx.reply(embed=error_embed(

               # f"{EMOJIS['tick_no']} Important Category!",

              #  f"You cannot disable the `{error.category}` category!\nIt has contains the core features of epicbot\nFor more info join our [Support Server]({SUPPORT_SERVER_LINK})."

         #   ))

      #  elif isinstance(error, PrivateCommand):

          #  await ctx.reply(embed=error_embed(

               # f"{EMOJIS['tick_no']} Private Command!",

               # "This command is private and you cannot use it."

           # ))

  #      elif isinstance(error, ComingSoon):

    #       await ctx.reply(embed=success_embed(

    #            "👀 Coming soon!",

    #            f"""
#
#👋 Hey there, EpicBot from the future here.

#This feature is really really epik, but it's not finished yet!

#The devs are working really hard on this!

#If you would like to see the progress consider joining our [**Support Server**]({SUPPORT_SERVER_LINK})

    #            """

     #       ).set_footer(text="Also you look kinda cute today"))

   #     elif isinstance(error, MusicGone):

    #        await ctx.reply(embed=error_embed(

     #           f"{EMOJIS['cry_']} Music unavailable! :(",

   #             f"""
#
#The music system is currently unavailable.
#
#The devs are working hard on remaking it!

#It will be back soon!

#For more info you can join our [**support server**]({SUPPORT_SERVER_LINK})

    #            """

   #         ))

       # elif isinstance(error, InvalidUrl):

           # await ctx.reply(embed=error_embed(

              #  f"{EMOJIS['tick_no']} Invalid URL!",

              #  f"The URL `{error.argument}` is not a valid URL!"

         #   ))

      #  elif isinstance(error, AutomodModuleAlreadyEnabled):

          #  await ctx.reply(embed=error_embed(

              #  f"{EMOJIS['tick_no']} Automod Module is already enabled!",

              #  f"The automod module `{error.module}` is already enabled!"

            #))

     #   elif isinstance(error, AutomodModuleNotEnabled):

         #   await ctx.reply(embed=error_embed(

              #  f"{EMOJIS['tick_no']} Automod Module is not enabled!",

            #    f"The automod module `{error.module}` is not enabled!\nPlease enable it using `{prefix}automod enable {error.module}`."

         #   ))

    #    elif isinstance(error, commands.CheckFailure):

       #     ctx.command.reset_cooldown(ctx)

          #  if not self.client.beta:

          #      await ctx.message.add_reaction('❌')

     #   else:

   #         random_error_id = gen_random_string(10)

      #      ctx.command.reset_cooldown(ctx)

    #        await ctx.reply(embed=error_embed(

      #          f"{EMOJIS['tick_no']} An unknown error occured!",

    #            error

    #        ).set_footer(text=f"ERROR ID: {random_error_id}"))

    #        error_text = "".join(traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__))[:2000]

    #        error_embed_ = discord.Embed(

     #           title="Traceback",

   #             description=("```py\n" + error_text + "\n```"),

     #           color=RED_COLOR

   #         ).add_field(name="Command", value=f"```{ctx.message.content}```", inline=False

     #       ).add_field(name="User", value=f"{ctx.author.mention} ```{ctx.author} ({ctx.author.id})```", inline=False

     #       ).add_field(name="Server", value=f"```{ctx.guild}({ctx.guild.id})```", inline=False

    #        ).set_footer(text=f"ERROR ID: {random_error_id}")

     #       try:

     #           webhooks = self.client.get_channel(1039598487085535292)

        #         =

  #              await webhook.send(embed=error_embed_)

      #      except Exception:

  #              traceback.print_exception(etype=type(error), value=error, tb=error.__traceback__)

async def setup(client):

    await client.add_cog(ErrorHandling(client))

