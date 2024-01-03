import operator
from typing import List, Optional
from prince.classes import Profile
from prince.converters import Lower
import discord
import time
import json
from discord.ext import commands
from config import (
    RANK_CARD_SUBMIT_CHANNEL,
    USER_REPORT_CHANNEL,
    EMOJIS, VOTE_LINK, TOP_GG_TOKEN,
    EMPTY_CHARACTER, MAIN_COLOR, WEBSITE_LINK, SUPPORT_SERVER_LINK,
     PARTNER_ROLE, OWNER_ROLE, BOT_MOD_ROLE,
    STAFF_ROLE, SUPPORTER_ROLE, BOOSTER_ROLE, DESIGN_HELPER_ROLE,
    BADGE_EMOJIS, DEFAULT_BANNED_WORDS,
    PINK_COLOR_2, RED_COLOR, ORANGE_COLOR,INVITE_BOT_LINK, BIG_PP_GANG,NO_PP_GANG
)
#from .leveling import rank_card_templates
from humanfriendly import format_timespan
from prince.custom_checks import check_voter, check_supporter
from prince.bot import Bot
from prince.ui import Confirm, Paginator
from prince.embed import success_embed, error_embed
from prince1.Tools import *

class user(commands.Cog, description="Commands related to the user!"):
    def __init__(self, client: Bot):
        self.client = client
        self.default_vote_dict = {
            "top.gg": 0,
            "bots.discordlabs.org": 0,
            "reminders": False,
            "last_voted": {}
        }



        
    async def get_actions_leaderboard(self, action_type: str) -> List[dict]:
        cursor = self.client.user_profile_db.find({}).sort([(action_type, -1)]).limit(50)
        final = await cursor.to_list(length=None)
        return final        

    async def get_cmnds_leaderboard(self) -> List[dict]:
        cursor = self.client.user_profile_db.find({}).sort([(cmds_used, -1)]).limit(50)
        final = await cursor.to_list(length=None)
        return final

    
    @commands.cooldown(3, 10, commands.BucketType.user)
    @ignore_check()
    @commands.command(aliases=['lb'], help="Check the leaderboard!")
    async def leaderboard(self, ctx, option: Lower = None):
        guild_config = await self.client.get_guild_config(ctx.guild.id)
        prefix = ctx.clean_prefix
        lb_options = ['invites', 'levels', 'messages', 'votes']
        action_options = ['times_simped', 'times_thanked', 'bites', 'blushes', 'cries', 'cuddles', 'facepalms', 'feeds', 'hugs', 'kisses', 'licks', 'pats', 'slaps', 'tail_wags', 'tickles', 'winks','bc']
        options_text = ""
     #   for e in lb_options:
     #       options_text += f"`{e}` "
        for e in action_options:
            options_text += f"`{e.replace('times_simped', 'simps').replace('times_thanked', 'thanks').replace('cmds_used','bc')}` "
        embed = discord.Embed(color=MAIN_COLOR)
        embed.title = "Leaderboard"
        if option is not None:
            embed.title = "Leaderboard" if option not in lb_options else option.title() + " Leaderboard"
        embed.set_thumbnail(url=self.client.user.display_avatar.url)
        embed.add_field(
            name=EMPTY_CHARACTER,
            value=f"[Invite Soward Prime]({INVITE_BOT_LINK}/invite) | [Support Server]({SUPPORT_SERVER_LINK})",
            inline=False
        )
        main = ""
        if option == "thanks":
            option = "times_thanked"
        if option == "simps":
            option = "times_simped"
        if option is None or option == "":
            embed.description = f"Please select an option for the leaderboard.\n\n**Options:** {options_text}"
     #   elif option in ['invites']:
    #        if guild_config['welcome']['channel_id'] is None:
    #            return await ctx.#reply(embed=error_embed(
    #                f"{EMOJIS['tick_no']} Not enabled!",
    #                "Please enable welcome messages to enable invite tracking."
   #             ))
  #          cursor = self.client.invites.find({})
   #         the_whole_fucking_db = await cursor.to_list(length=None)
   #         yes = {}
   #         for e in the_whole_fucking_db:
    #            if "guilds" in e:
   #                 if str(ctx.guild.id) in e['guilds'] and "real" in e['guilds'][str(ctx.guild.id)]:
   #                     yes.update({e['_id']: e['guilds'][str(ctx.guild.id)]['real']})
    #        yes = dict(sorted(yes.items(), key=operator.itemgetter(1), reverse=True))
   #         if ctx.author.id in yes:
   #             main += f"You are rank **#{list(yes).index(ctx.author.id) + 1}** in this server for {option}\n\n"

   #         i = 1
     #       for e in yes:
     #           if i > 10:
     #               break
     #           main += f"`{i}.` <@{e}> - **{yes[e]}** invites\n"
     #           i += 1
     #       if len(yes) == 0:
     #           main = "All members have **0** invites in this guild."
   #         embed.description = main
   #     elif option in ['msgs', 'messages']:
   #         return await ctx.invoke(self.client.get_command('messages_lb'))
   #     elif option in ['levels', 'rank']:
   #         return await ctx.invoke(self.client.get_command('leveling_lb'))
   #     elif option in ['votes']:
   #         return await ctx.invoke(self.client.get_command('vote_lb'))
        elif option in action_options:
            paginator = commands.Paginator(prefix="", suffix="", max_size=500)
            actions = await self.get_actions_leaderboard(option)
            if len(actions) == 0:
                return await ctx.reply("No users found.")
            for i, e in enumerate(actions):
                amount = e.get(option, 0)
                if amount > 0:
                    paginator.add_line(f"`{i + 1}.` <@{e['_id']}> • `{amount}` {option.replace('times_thanked', 'thanks').replace('times_simped', 'simps')}")
            embeds = [success_embed(f"{EMOJIS['tick_yes']} {option.replace('times_thanked', 'thanks').replace('times_simped', 'simps').title()} Leaderboard", page) for page in paginator.pages]
            if len(embeds) == 0:
                return await ctx.reply("No users found.")
            if len(embeds) == 1:
                return await ctx.reply(embed=embeds[0])
            view = Paginator(ctx, embeds=embeds)
            return await ctx.reply(embed=embeds[0], view=view)
        else:
            embed.description = f"Invalid option! Please use `{prefix}leaderboard` to see the available options."

        await ctx.reply(embed=embed) 


    

    




        
    

   
   
       
                    

        
            

            
            
                

        
    @commands.command(help="Thank someone!")
    @ignore_check()
    @commands.cooldown(2, 120, commands.BucketType.user)
    async def thanks(self, ctx: commands.Context, user_: discord.Member = None, *, reason=None):
        prefix = ctx.clean_prefix
        if user_ is None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Please mention a user to thank!",
                f"Correct usage: `{prefix}thank @user`"
            ))
        if user_ == ctx.author:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Bruh!",
                "You cannot thank yourself! Idiot!"
            ))
        if user_.bot:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} You can't thank bots!",
                f"Thank real people! {EMOJIS['vay']}"
            ))

        if reason is None:
            reason = "being an amazing person!"
        if reason.lower().startswith("for "):
            reason = reason[4:]

        user_profile = await self.client.get_user_profile_(user_.id)
        await self.client.update_user_profile_(user_.id, times_thanked=user_profile.times_thanked + 1)

        return await ctx.reply(embed=success_embed(
            f"{EMOJIS['heawt']} Thank you!",
            f"Thank you {user_.mention} for {reason}"
        ).set_footer(text=f"They have been thanked {user_profile.times_thanked + 1} times!"
        ).set_thumbnail(url="https://cdn.discordapp.com/emojis/856078862852161567.png?v=1"))

    async def get_badges(self, user_id: int, user_profile: Profile) -> list:
        guild = self.client.get_guild(938486846453854290)
        if not guild:
            return []
        member = guild.get_member(user_id)
        wew = []
        badge_roles = {
            "owner": OWNER_ROLE,
            "bot_mod": BOT_MOD_ROLE,
            "staff_member": STAFF_ROLE,
            "partner": PARTNER_ROLE,
            "supporter": SUPPORTER_ROLE,
            "booster": BOOSTER_ROLE,
            "designer": DESIGN_HELPER_ROLE,
            # "cutie": VIP_ROLE,
        }

        people_badges = {
            "aw||oo||sh": 671355502399193128,
            "wendo": 478623992337530883,
            "cutevi": 679677267164921866,
            "cat": 344313283714613248,
            "best_streamer": 91090336029347840,
            "very_good_taste": 729765852030828674
        }

        for e in people_badges:
            if user_id == people_badges[e]:
                wew.append(e)

        if member:
            for e in badge_roles:
                if guild.get_role(badge_roles[e]) in member.roles:
                    wew.append(e)

            if int(member.joined_at.strftime("%Y")) < 2021:
                wew.append("early_supporter")

        if user_profile.bugs_reported >= 25:
            wew.append("bug_hunter")
        if user_profile.bugs_reported >= 50:
            wew.append("elite_bug_hunter")

        if user_profile.times_simped >= 25:
            wew.append("samsung_girl")
        if user_profile.times_simped >= 50:
            wew.append("love_magnet")

        if user_profile.times_thanked >= 25:
            wew.append("helper")
        if user_profile.times_thanked >= 50:
            wew.append("savior")
        if user_id in BIG_PP_GANG:
            wew.append("Big_PP")
        if user_id in NO_PP_GANG:
            wew.append("No_PP")

#        voted = await check_voter(user_id)
#        if voted:
#            wew.append("voter")

        return wew

    @commands.command(help="Check your profile!")
    @ignore_check()
    @commands.cooldown(3, 15, commands.BucketType.user)
    async def profile(self, ctx: commands.Context, user_: discord.Member = None):
        if user_ is None:
            user_ = ctx.author

        if user_.bot:
            return await ctx.reply(f"{EMOJIS['tick_no']}Bots don't have profiles.")

        user_profile = await self.client.get_user_profile_(user_.id)

        async with ctx.typing():
            # await ctx.invoke(
            #     self.client.get_command('rank_from_template'),
            #     member=user_,
            #     template=user_profile['rank_card_template'],
            #     reply=False
            # )

            nice = f"""
    {user_profile.description}

    **{'Single 💔' if not user_profile.married_to else 'Married to <@'+str(user_profile.married_to)+'> 💞'}**
    {'**Married at:** <t:' + str(user_profile.married_at) + ':D> <t:' + str(user_profile.married_at) + ':R>' if user_profile.married_to is not None else ''}

    Commands Used: `{user_profile.cmds_used}`
    Bugs reported: `{user_profile.bugs_reported}`
    Suggestions given: `{user_profile.suggestions_submitted}`

    Thanked by **{user_profile.times_thanked}** user{'s' if user_profile.times_thanked != 1 else ''}!
    Simped by **{user_profile.times_simped}** simp{'s' if user_profile.times_simped != 1 else ''}!

    
                 """   
            badge_text = ""
            badge_text2 = ""
            badge_text3 = ""
            badge_text4 = ""
            badge_text5 = ""

            h = await self.get_badges(user_.id, user_profile)

            for e in user_profile.badges:
                h.append(e)

            i = 1

            for e in h:
                hee = BADGE_EMOJIS[e] + f"  {e.title().replace('_', ' ')}\n"
                if e == "Big_PP" or e == "No_PP":
                    hee = BADGE_EMOJIS[e] + f"  {e.replace('_', ' ')}\n"
                pain = 5
                if i <= pain:
                    badge_text += hee
                if i > pain and i <= 2 * pain:
                    badge_text2 += hee
                if i > 2 * pain and i <= 3 * pain:
                    badge_text3 += hee
                if i > 3 * pain and i <= 4 * pain:
                    badge_text4 += hee
                if i > 4 * pain and i <= 5 * pain:
                    badge_text5 += hee
                i += 1

            # f = discord.File("assets/temp/rank.png", filename="rank.png")
            embed = discord.Embed(
                description=nice,
                color=MAIN_COLOR
            ).set_author(name=user_.name, icon_url=user_.display_avatar.url
            )  # .set_image(url="attachment://rank.png")

            embed.add_field(name="Badges:", value=badge_text, inline=True)

            if badge_text2 != "":
                embed.add_field(name=EMPTY_CHARACTER, value=badge_text2, inline=True)
            if badge_text3 != "":
                embed.add_field(name=EMPTY_CHARACTER, value=EMPTY_CHARACTER, inline=True)
                embed.add_field(name=EMPTY_CHARACTER, value=badge_text3, inline=True)
            if badge_text4 != "":
                embed.add_field(name=EMPTY_CHARACTER, value=badge_text4, inline=True)
                embed.add_field(name=EMPTY_CHARACTER, value=EMPTY_CHARACTER, inline=True)
            if badge_text5 != "":
                embed.add_field(name=EMPTY_CHARACTER, value=badge_text5, inline=True)

     #       embed.add_field(
     #           name=EMPTY_CHARACTER,
   #             value=f"Your current rankc#ard template is `{user_profile.rank_card_template}`:",
     #           inline=False
   #         ).set_thumbnail(url=user_.display_avatar.url)

            await ctx.reply(embed=embed)


    @commands.command(help="Edit your profile.", aliases=['eprofile', 'editp'])
    @commands.cooldown(3, 30, commands.BucketType.user)
    @ignore_check()
    async def editprofile(self, ctx: commands.Context, thing=None, *, new_thing=None):
        prefix = ctx.clean_prefix
        info_embed = success_embed(
            "📝  Edit profile",
            f"""
**To edit your profile, you can use the following commands:**

- `editprofile bio <new bio>` - To edit your bio.

            """
        )
        if thing is None:
            return await ctx.reply(embed=info_embed)



        if thing.lower() in ['bio', 'description']:
            if new_thing is None:
                return await ctx.reply(embed=error_embed(f"{EMOJIS['tick_no']} Invalid Usage!", f"Correct Usage: `{prefix}editprofile nick <nickname>`"))
            if len(new_thing) > 250:
                return await ctx.reply(embed=error_embed(f"{EMOJIS['tick_no']} Too long!", "Your bio can't be greater than **250** characters."))
            for word in DEFAULT_BANNED_WORDS:
                if word in new_thing.lower():
                    return await ctx.reply(embed=error_embed(f"{EMOJIS['tick_no']} No Bad Words!", "Your bio cannot contain bad words."))
            await self.client.update_user_profile_(ctx.author.id, description=new_thing)
            return await ctx.reply("Your bio has been updated.")



        

    @commands.command(help="Marry someone... ")
    @ignore_check()
    @commands.cooldown(3, 30, commands.BucketType.user)
    async def marry(self, ctx: commands.Context, user: discord.Member = None, *, proposal_text: str = None):
        if not user:
            return await ctx.reply(f"Correct Usage: `marry @user please marry me uwu`")
        if user.bot:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(f"{EMOJIS['tick_no']}You cannot marry bots.")
        if user == ctx.author:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply("Imagine marrying yourself... Why are you so lonely...")
        user_profile = await self.client.get_user_profile_(ctx.author.id)
        victim_profile = await self.client.get_user_profile_(user.id)
        if user_profile.married_to is not None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(f"{EMOJIS['tick_no']}You are already married to: <@{user_profile.married_to}>\nDon't cheat on them >:(")
        if victim_profile.married_to:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(f"{EMOJIS['tick_no']}{user.mention} is already married to: <@{victim_profile.married_to}>")

        view = Confirm(context=ctx, user=user)
        msg = await ctx.channel.send(
            user.mention,
            embed=discord.Embed(
                title="👉👈",
                description=proposal_text or "W-W-Would you like to marry me?... *blushes*",
                color=PINK_COLOR_2
            ).set_image(url="https://media1.tenor.com/images/58bd69fb056bd54b80c92581f3cd9cf9/tenor.gif?itemid=10799169"
            ).set_author(name=f"{ctx.author.name} 💘 {user.name}", icon_url=ctx.author.display_avatar.url),
            view=view,
            allowed_mentions=discord.AllowedMentions(
                users=True,
                roles=False,
                everyone=False,
                replied_user=False
            )
        )
        await view.wait()
        if view.value is None:
            return await msg.edit(
                content=f"Looks like {user.mention} didn't respond in time... :(",
                embed=None,
                view=None
            )
        elif not view.value:
            return await msg.edit(
                content="You got rejected!",
                embed=discord.Embed(
                    title="💔",
                    description=f"**{user.name}** denied your proposal :(",
                    color=RED_COLOR
                ).set_image(url="https://media1.tenor.com/images/79b965bb99fd58b94d2550b384093e75/tenor.gif?itemid=13668435"
                ).set_author(name=f"{ctx.author.name} 💔 {user.name}", icon_url=ctx.author.display_avatar.url),
                view=None
            )
        await self.client.update_user_profile_(ctx.author.id, married_to=user.id, married_at=round(time.time()))
        await self.client.update_user_profile_(user.id, married_to=ctx.author.id, married_at=round(time.time()))
        return await msg.edit(
            content="WOOOO!!!",
            embed=discord.Embed(
                title="Such a cute couple... >.<",
                description="This is the cutest thing ever!",
                color=PINK_COLOR_2
            ).set_image(url="https://media1.tenor.com/images/d0cd64030f383d56e7edc54a484d4b8d/tenor.gif?itemid=17382422"
            ).set_author(name=f"{ctx.author.name} 💞 {user.name}", icon_url=ctx.author.display_avatar.url),
            view=None
        )

    @commands.command(help="Divorce :C", aliases=['unmarry'])
    @ignore_check()
    @commands.cooldown(3, 30, commands.BucketType.user)
    async def divorce(self, ctx: commands.Context):
        user_profile = await self.client.get_user_profile_(ctx.author.id)
        if not user_profile.married_to:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(f"{EMOJIS['tick_no']}You are not married to anyone.")
        view = Confirm(context=ctx)
        msg = await ctx.reply(embed=discord.Embed(
            title="💔",
            description=f"Do you really want to divorce <@{user_profile.married_to}> :(",
            color=RED_COLOR
        ),
            view=view)
        await view.wait()
        if view.value is None:
            return await msg.edit(content="You didn't answer in time.", embed=None, view=None)
        if not view.value:
            return await msg.edit(content="Ok, I have cancelled the command.", embed=None, view=None)
        time_ = user_profile.married_at
        await self.client.update_user_profile_(ctx.author.id, married_to=None, married_at=None)
        await self.client.update_user_profile_(user_profile.married_to, married_to=None, married_at=None)
        return await msg.edit(
            embed=discord.Embed(
                title="💔",
                description=f"Your marriage lasted **{format_timespan(round(time.time()) - time_)}**",
                color=RED_COLOR
            ).set_image(url="https://media1.tenor.com/images/79b965bb99fd58b94d2550b384093e75/tenor.gif?itemid=13668435"),
            view=None
        )

    

    @commands.command(help="Report a user!")
    @ignore_check()
    @commands.cooldown(2, 600, commands.BucketType.user)
    async def report(self, ctx, user: discord.User = None, *, reason=None):
        if user is None or reason is None:
            prefix = ctx.clean_prefix
            return await ctx.reply(embed=error_embed(
                f"{EMOJIS['tick_no']} Invalid Usage!",
                f"Correct Usage: `{prefix}report @user <reason>`\nExample: `{prefix}report @user abusing soward bug`\n\n**Note:** Spam reports will get you blacklisted."
            ))
        if user == self.client.user:
            return await ctx.reply("Bruh ._.")
        if user.bot:
            return await ctx.reply("You cannot report bots.")
        if user == ctx.author:
            return await ctx.reply(f"Imagine reporting urself... {EMOJIS['bruh']}")

        files = []
        for file in ctx.message.attachments:
            files.append(await file.to_file())

        report_channel = self.client.get_channel(USER_REPORT_CHANNEL)
        await report_channel.send(
            f"<@&{BOT_MOD_ROLE}>",
            embed=discord.Embed(
                title="User Reported",
                description=reason,
                color=ORANGE_COLOR
            ).set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url
            ).add_field(name="Reported User:", value=f"`{user} ({user.id})` {user.mention}", inline=False),
            allowed_mentions=discord.AllowedMentions(
                everyone=False,
                roles=True,
                users=False,
                replied_user=False
            ),
            files=files
        )
        await ctx.reply(f"{EMOJIS['tick_yes']} Your report has been sent. Please be patient for mods to review it.")

    @commands.command(aliases=['opt-out', 'optout', 'nosnipe'], help="Opt out of snipe")
    @ignore_check()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def opt_out(self, ctx):
        user_profile = await self.client.get_user_profile_(ctx.author.id)

        snipe = user_profile.snipe
        await self.client.update_user_profile_(ctx.author.id, snipe=not snipe)

        pain = "\n\nYou also won't be able to use the snipe commands."
        await ctx.reply(embed=success_embed(
            f"{EMOJIS['tick_yes']} Snipe toggled!",
            f"Your messages will {'no longer' if snipe else 'now'} be logged!{pain if snipe else ''}"
        ))


async def setup(client):
    await client.add_cog(user(client))
