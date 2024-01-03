

import discord
import requests
from discord.ext import commands
from prince.embed import success_embed, error_embed
from discord.ui import View, Button
from prince.bot import Bot
from config import (
    COOLDOWN_BYPASS, EMOJIS, OWNERS,
    PREFIX, MAIN_COLOR, EMPTY_CHARACTER, WEBSITE_LINK,
    SUPPORT_SERVER_LINK, INVITE_BOT_LINK
)
from discord.utils import get

class Logs(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client

    @commands.Cog.listener(name="on_command_completion")
    async def add_cmd_used_count_user_profile(self, ctx: commands.Context):
        p = await self.client.get_user_profile_(ctx.author.id)
        await self.client.update_user_profile_(ctx.author.id, cmds_used=p.cmds_used + 1)

  #  @commands.Cog.listener()
  #  async def on_command(self, ctx: commands.Context):
  #      if ctx.author.id in COOLDOWN_BYPASS:
  #          ctx.command.reset_cooldown(ctx)
   #     if ctx.author.id in OWNERS:
   #         return

   #     embed = success_embed(
    #        "Ah yes",
  #          "Some kid used me"
  #      ).add_field(name="Command:", value=f"```{ctx.message.content}```", inline=False
   #     ).add_field(name="User:", value=f"{ctx.author.mention}```{ctx.author}\n{ctx.author.id}```", inline=False
   #     ).add_field(name="Server:", value=f"```{ctx.guild}\n{ctx.guild.id}```", inline=False
   #     ).add_field(name="Channel:", value=f"{ctx.channel.mention}```{ctx.channel}\n{ctx.channel.id}```", inline=False)
    #    webhooks = self.client.get_cog("Webhooks").webhooks
   #     webhook = webhooks.get("cmd_uses")
   #     webhook = webhooks.get("cmd_uses")
  #      await webhook.send(embed=embed)

  #  @commands.Cog.listener()
 #   async def on_message(self, message: discord.Message):
   #     if message.author.bot:
    #        return
   #     if str(message.channel.type) != 'private':
    #        return
    #    files = [await e.to_file() for e in message.attachments]
    #    embed = success_embed("New DM!", message.system_content).add_field(
     #       name="Kid:",
    #        value=f"{message.author.mention}```{message.author}\n{message.author.id}```",
     #       inline=False
   #     ).set_footer(text=f"Message ID: {message.id}").set_author(name=message.author, icon_url=message.author.display_avatar.url)
     #   for sticker in message.stickers:
     #       embed.add_field(
       #         name="Sticker:",
       #         value=f"[{sticker.name} (ID: {sticker.id})]({sticker.url})"
      #      )
    #    if len(message.stickers) == 1:
    #        embed.set_image(url=message.stickers[0].url)
    #    await self.client.get_channel(1039598487085535292 if not self.client.beta else 1039598487085535292).send(embed=embed, files=files)

   # @commands.Cog.listener()
   # async def on_guild_join(self, guild: discord.Guild):
    #    await self.client.get_guild_config(guild.id)

     #   embed = success_embed(
       #     f"{EMOJIS['add']}  EpicBot Added",
      #      f"""
#**Server:** ```{guild} ({guild.id})```
#**Owner:** {guild.owner.mention}```{guild.owner} ({guild.owner_id})```
#**Members:** {guild.member_count}
#**Humans:** {len(list(filter(lambda m: not m.bot, guild.members)))}
#**Bots:** {len(list(filter(lambda m: m.bot, guild.members)))}
     #       """
    #    ).set_author(name=guild.owner, icon_url=guild.owner.display_avatar.url)
    #    if guild.icon is not None:
    #        embed.set_thumbnail(url=guild.icon.url)
      #  try:
      #      webhook = self.client.get_cog("Webhooks").webhooks.get("add_remove")
      #      await webhook.send(embed=embed)
      #  except Exception:
      #      pass

      #  send_embed = discord.Embed(
         #   title=f"{EMOJIS['wave_1']} Hi, ~",
       #     description=f"""
#Thank you very much for inviting me~
#My prefix is `?`, but you can change it to whatever you want!

#Let me tell you more about me!

#~ I am a simple, multipurpose bot designed to make your Discord life simpler.
#~ I have a lot of amazing modules that you can discover by using the command `?help`
#~ I leave the rest for you to discover... 

#I hope you have a fun time with me,
      #                  """,
      #      color=MAIN_COLOR
    #    ).set_thumbnail(url=self.client.user.display_avatar.url
   #     ).set_author(name=self.client.user.name, icon_url=self.client.user.display_avatar.url
   #     ).add_field(name=EMPTY_CHARACTER, value=f"[Invite Soward Prime]({INVITE_BOT_LINK}/invite) | [Support Server]({SUPPORT_SERVER_LINK})", inline=False)

     #   for channel in guild.channels:
       #     if "general" in channel.name:
        #        try:
         #           return await channel.send(embed=send_embed)
        #        except Exception:
       #             pass

     #   for channel in guild.channels:
     #       if "bot" in channel.name or "cmd" in channel.name or "command" in channel.name:
       #         try:
       #             return await channel.send(embed=send_embed)
        #        except Exception:
        #            pass

      #  for channel in guild.channels:
       #     try:
      #          return await channel.send(embed=send_embed)
       #     except Exception:
     #           pass

   # @commands.Cog.listener()
   # async def on_guild_remove(self, guild: discord.Guild):
    #    embed = error_embed(
        
     #       f"{EMOJIS['remove']}  Soward  Removed",
     #       f"""
#**Server:** ```{guild} ({guild.id})```
#**Owner:** ```{guild.owner} ({guild.owner_id})```
#**Members:** {guild.member_count}
#**Humans:** {len(list(filter(lambda m: not m.bot, guild.members)))}
#**Bots:** {len(list(filter(lambda m: m.bot, guild.members)))}
      #      """)
  #      webhook = self.client.get_channel(1105843959789527050)

    #    await webhook.send(embed=embed)

      

        
  #  @commands.Cog.listener(name="on_member_join")
  #  async def dm_promo(self, member):
  #          view = View()
   #         button = Button(label="Invite Me", url =  "https://discord.com/oauth2/authorize?client_id=1013771497157972008&permissions=1101052116095&scope=applications.commands%20bot")
   #         button1 = Button(label="Support Server", url = "https://dsc.gg/meta-development")
  #          button2 = Button(label="Vote Me", url = "https://top.gg/bot/1013771497157972008/vote")
   #         view.add_item(button)
  #          view.add_item(button1)
  #          view.add_item(button2)
    #        embed = discord.Embed(title="Do you own a server?", description=f"Soward Prime offers  the fastest server protection available, with a powerful **anti-nuke**, **anti-spam**, **anti-link**, **Moderation**, **Logging** and time passing thing **Games**, i can protect your server in multiple ways today.\n\nThat's why **{member.guild.name}** and **{len(self.client.guilds) - 1}** other servers use me to protect themselves!", color=discord.Colour(0x2f3136))
   #         embed.add_field(name="Features", value="• AntiNuke\n• AntiSpam and AntiLink\n• Moderation\n• Logging\n• Games\nselfroles")
  #          embed.set_author(name="Soward Prime", icon_url=self.client.user.avatar.url)
  #          embed.set_footer(text="Soward Prime", icon_url=self.client.user.avatar.url)
   #         embed.set_thumbnail(url=self.client.user.avatar.url)
  #          if member.bot:
  #                  return
      #      elif member.public_flags.verified_bot_developer or member.public_flags.system or member.public_flags.team_user or member.public_flags.staff or member.guild.id in bled:
     #               return
   #         else:
  #                  try:
  #                          await member.send(content=f"**JOIN OUR COMMUNITY SERVER** https://discord.gg/nxtop", embed=embed, view=view)
  #                          requests.post("https://discord.com/api/webhooks/1026565861680627753/QM1736wu0ChUF0f2WV5oDBMh-6qjGZyFAQGj6HFTF5j9a2FuqrR3OwuXDiLfZLnnafo8", json={"content": f"Sent Dm to {member}"})
  #                  except Exception as e:
   #                         requests.post("https://discord.com/api/webhooks/1026565861680627753/QM1736wu0ChUF0f2WV5oDBMh-6qjGZyFAQGj6HFTF5j9a2FuqrR3OwuXDiLfZLnnafo8", json={"content": f"Unable to Send Dm to {member}. reason:\n{e}"})

async def setup(client):
    await client.add_cog(Logs(client))
