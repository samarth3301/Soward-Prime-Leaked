import discord
from discord.ext import commands
import json
from prince1.Tools import*
from prince.custom_checks import voter_only

class autoresponse(commands.Cog):
  def __init__(self, client):
    self.client = client

  

  @commands.group(description='show the help menu of autoresponse')
  @ignore_check()
  async def ar(self, ctx):
        ...        
       
  @ar.command(description='count all autoresponses of server')
  @commands.cooldown(1, 5, commands.BucketType.user)
  @ignore_check()
  @commands.has_permissions(administrator=True)
  @blacklist_check()
  #@voter_only()
  async def show(self, ctx):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
        autoresponsenames = []
        if str(ctx.guild.id) in autoresponse:
            for autoresponsecount in autoresponse[str(ctx.guild.id)]:
              autoresponsenames.append(autoresponsecount)
            embed = discord.Embed(color=0x42f579)
            st, count = "", 1
            for autoresponse in autoresponsenames:
                    st += f"*[ {'0' + str(count) if count < 10 else count} ]* Name -> {autoresponse}\n"
                    test = count
                    count += 1
            embed.title = f" autoresponses for {ctx.guild} - {test}"
        embed.description = st
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
        embed.set_footer(text="Made By Prince", icon_url=self.client.user.avatar)
        embed.set_thumbnail(url=self.client.user.avatar)
        await ctx.reply(embed=embed)
  @commands.has_permissions(manage_messages=True)
  @ignore_check()

  @commands.command(

		description="Pins the message you reply to. If you're not replying to a message, it'll pin the message right above yours.",

		extras={

			'permission': 'manage_messages'

		}

	)

  async def pin(self, ctx: commands.Context):

      if ctx.message.reference:

          message = ctx.message.reference.resolved

      else:

          messages = [message async for message in ctx.history(limit=2)]

          messages.remove(ctx.message)

          message = messages[0]

      try:

          await message.pin()

          await ctx.reply("successfully pin the specified message")

		  

      except discord.HTTPException:

          await ctx.reply("Could not pin the specified message.")

  @commands.has_permissions(manage_messages=True)
  @ignore_check()
  @commands.command(

		description="Pins the message you reply to. If you're not replying to a message, it'll pin the message right above yours.",

		extras={

			'permission': 'manage_messages'

		}

	)

  async def unpin(self, ctx: commands.Context):

      if ctx.message.reference:

          message = ctx.message.reference.resolved

      else:

          messages = [message async for message in ctx.history(limit=2)]

          messages.remove(ctx.message)

          message = messages[0]

      try:

          await message.unpin()

          await ctx.reply("successfully unpin the specified medsage")

		  

      except discord.HTTPException:

          await ctx.reply("Could not unpin the specified message.")

	                
    
async def setup(client):
    await client.add_cog(autoresponse(client))