
from discord import ButtonStyle, CategoryChannel, Embed, ForumChannel, HTTPException, Interaction, StageChannel, Colour, SelectOption
import datetime
import io
import json
from .input import ChannelSelectPrompt
import discord
#import mystbin
from discord.ext import commands

from . import style

conversion_table = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}


def dec_to_hexa(decimal: int) -> str:
    """
    Convert a decimal number to hexadecimal
    """
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16

    if len(hexadecimal) < 6:
        hexadecimal = "0" * (6 - len(hexadecimal)) + hexadecimal

    return "#" + hexadecimal


class CustomEmbedFieldModal(discord.ui.Modal):
    """
    Embed Modal to edit a field
    """

    def __init__(self, select: discord.ui.Select, field: int) -> None:
        """
        Init the modal
        """
        super().__init__(title=f"Edit Field {field}")
        self.select = select
        self.field = field
        self.field_title = discord.ui.TextInput(
            label="Title",
            style=discord.TextStyle.long,
            placeholder="The Field's Title",
            default=select.view.embed.fields[field].name,
            max_length=256,
            min_length=1,
            required=True,
        )
        self.description = discord.ui.TextInput(
            label="Description",
            style=discord.TextStyle.long,
            placeholder="The Field's Description",
            default=select.view.embed.fields[field].value,
            max_length=1024,
            min_length=1,
            required=False,
        )
        self.inline = discord.ui.TextInput(
            label="Inline",
            style=discord.TextStyle.long,
            placeholder="True or False",  # No point in a default since it's shorter than 6 chars
            max_length=5,
            min_length=1,
            required=True,
        )
        self.add_item(self.field_title)
        self.add_item(self.description)
        self.add_item(self.inline)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        """
        On_submit, do stuff
        """
        embed: discord.Embed = self.select.view.embed
        embed.set_field_at(
            index=self.field,
            name=self.field_title.value,
            value=self.description.value,
            inline=self.inline.value.lower() == "true",
        )
        await interaction.response.edit_message(embed=embed, view=self.select.view)




    
                


class CustomEmbedSendModal(discord.ui.Modal, title="Send Embed"):
    """
    Send Modal to send embed to a different or same channel
    """

    channel_input = discord.ui.TextInput(
        label="Channel",
        style=discord.TextStyle.long,
        placeholder="Channel ID",
        max_length=4000,
        min_length=1,
        required=True,
    )

    def __init__(self, view: discord.ui.View) -> None:
        """
        Init the modal
        """
        super().__init__()
        self.view = view

    async def on_submit(self, interaction: discord.Interaction) -> None:
        """
        On_submit, do stuff
        """
        channel: discord.TextChannel = self.view.ctx.bot.get_channel(
            int(self.channel_input.value)
        ) or await self.view.ctx.bot.fetch_channel(int(self.channel_input.value))

        if channel:
            if channel.permissions_for(self.view.ctx.me).send_messages:
                await channel.send(embed=self.view.embed)
                embed = discord.Embed(
                    title="Sent Embed",
                    description="""Sent successfully!""",
                    timestamp=discord.utils.utcnow(),
                    color=style.Color.GREEN,
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                embed = discord.Embed(
                    title="Error",
                    description="""I don't have permissions to send messages in that channel!""",
                    timestamp=discord.utils.utcnow(),
                    color=style.Color.RED,
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(
                title="Error",
                description="""This channel doesn't exist!""",
                timestamp=discord.utils.utcnow(),
                color=style.Color.RED,
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)


class CustomEmbedFieldDropdown(discord.ui.Select):
    """
    A Select for editing embed fields
    """

    def __init__(self, embed: discord.Embed) -> None:
        """
        Init the embed creation select
        """

        options = []

        if len(embed.fields) == 0:
            options.append(
                discord.SelectOption(label="No Fields", value="no_fields")
            )

        for count, field in enumerate(embed.fields):
            options.append(
                discord.SelectOption(
                    label=f"Edit Field {count + 1}",
                    description=field.title,
                    
                    value=str(count),
                )
            )

        super().__init__(
            placeholder="Choose a Field to Edit",
            min_values=1,
            max_values=1,
            options=options,
            row=1,
        )

    async def callback(self, interaction: discord.Interaction) -> None:
        """
        Select a Property to edit
        """
        if self.values[0] == "no_fields":
            embed = discord.Embed(
                title="Error",
                description="""There are no fields to edit""",
                timestamp=discord.utils.utcnow(),
                color=style.Color.RED,
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_modal(
                CustomEmbedFieldModal(self, int(self.values[0]))
            )


class CustomEmbedAuthorModal(discord.ui.Modal):
    """
    Custom Embed author modal
    """

    def __init__(self, view: discord.ui.View) -> None:
        """
        Init the modal
        """
        super().__init__(title="Edit Author")
        self.view = view
        self.name = discord.ui.TextInput(
            label="Name",
            style=discord.TextStyle.long,
            placeholder="Author Name",
            default=self.view.embed.author.name,
            max_length=256,
            min_length=1,
            required=True,
        )
        self.url = discord.ui.TextInput(
            label="URL",
            style=discord.TextStyle.long,
            placeholder="Author URL (Optional)",
            default=self.view.embed.author.url,
            max_length=4000,
            min_length=1,
            required=False,
        )
        self.icon_url = discord.ui.TextInput(
            label="Icon URL (Optional)",
            style=discord.TextStyle.long,
            placeholder="The URL for the Icon",
            default=self.view.embed.author.icon_url,
            max_length=4000,
            min_length=1,
            required=False,
        )
        self.add_item(self.name)
        self.add_item(self.url)
        self.add_item(self.icon_url)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        """
        On_submit, do stuff
        """
        self.view.embed.set_author(
            name=self.name.value, url=self.url.value, icon_url=self.icon_url.value
        )
        for child in self.view.children:
            if isinstance(child, discord.ui.Button) and child.label == "Remove Author":
                child.disabled = False
        await interaction.response.edit_message(embed=self.view.embed, view=self.view)


class opModal(discord.ui.Modal):
    """
    Custom Embed author modal
    """

    def __init__(self, view: discord.ui.View) -> None:
        """
        Init the modal
        """
        super().__init__(title="Webhook")
        self.view = view
        self.name = discord.ui.TextInput(
            label="Name",
            style=discord.TextStyle.long,
            placeholder="enter name for webhook",
            default="Soward Prime",
            max_length=256,
            min_length=1,
            required=True,
        )
        self.url = discord.ui.TextInput(
            label="icon_url",
            style=discord.TextStyle.long,
            placeholder="url_dalo_re",
            max_length=256,
            min_length=1,
            required=False,
		)
        
        self.add_item(self.name)
        self.add_item(self.url)
        

    async def on_submit(self, interaction: discord.Interaction) -> None:
        """
        On_submit, do stuff
        """
        op = await interaction.channel.create_webhook(name=self.name)
        await interaction.response.send_message("successfully sent embed", ephemeral=True)
        
        await op.send(embed=self.view.embed,avatar_url=self.url)



class CustomEmbedBaseModal(discord.ui.Modal):
    """
    Custom embed base modal
    """

    def __init__(self, view: discord.ui.View) -> None:
        """
        Init the modal
        """
        super().__init__(title="Edit Base")
        self.view = view
        self.embed_title = discord.ui.TextInput(
            label="Title",
            style=discord.TextStyle.long,
            placeholder="Title",
            default=self.view.embed.title,
            max_length=256,
            min_length=1,
            required=True,
        )
        self.url = discord.ui.TextInput(
            label="Title URL",
            style=discord.TextStyle.long,
            placeholder="Title URL (Optional)",
            default=self.view.embed.url,
            max_length=4000,
            min_length=1,
            required=False,
        )
        self.description = discord.ui.TextInput(
            label="Description",
            style=discord.TextStyle.long,
            placeholder="Description (Optional)",
            default=self.view.embed.description,
            max_length=4000,
            min_length=1,
            required=False,
        )
        self.color = discord.ui.TextInput(
            label="Color",
            style=discord.TextStyle.long,
            placeholder="Hex Color (Optional)",
            default=dec_to_hexa(
                self.view.embed.color.value if self.view.embed.color else 0
            ),
            max_length=7,
            min_length=1,
            required=False,
        )
        self.timestamp = discord.ui.TextInput(
            label="Timestamp",
            style=discord.TextStyle.long,
            placeholder="Timestamp (Optional)",
            default=str(int(self.view.embed.timestamp.timestamp())),
            max_length=10,
            min_length=1,
            required=False,
        )
        self.add_item(self.embed_title)
        self.add_item(self.url)
        self.add_item(self.description)
        self.add_item(self.color)
        self.add_item(self.timestamp)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        """
        On_submit, do stuff
        """
        embed: discord.Embed = self.view.embed
        embed.title = self.embed_title.value
        embed.url = self.url.value
        embed.description = self.description.value
        embed.color = int(self.color.value.replace("#", ""), base=16)
        embed.timestamp = datetime.datetime.fromtimestamp(int(self.timestamp.value))
        await interaction.response.edit_message(embed=self.view.embed, view=self.view)


class CustomEmbedImageModal(discord.ui.Modal):
    """
    Custom Embed Image Modal
    """

    def __init__(self, view: discord.ui.View) -> None:
        """
        Init the modal
        """
        super().__init__(title="Edit Image")
        self.view = view
        self.image_url = discord.ui.TextInput(
            label="Image URL",
            style=discord.TextStyle.long,
            placeholder="Image URL",
            default=self.view.embed.image.url if self.view.embed.image else None,
            max_length=4000,
            min_length=1,
            required=False,
        )
        self.thumbnail_url = discord.ui.TextInput(
            label="Thumbnail URL",
            style=discord.TextStyle.long,
            placeholder="Thumbnail URL",
            default=self.view.embed.thumbnail.url
            if self.view.embed.thumbnail
            else None,
            max_length=4000,
            min_length=1,
            required=False,
        )
        self.add_item(self.image_url)
        self.add_item(self.thumbnail_url)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        """
        On_submit, do stuff
        """
        embed: discord.Embed = self.view.embed
        embed.set_image(url=self.image_url.value)
        embed.set_thumbnail(url=self.thumbnail_url.value)
        await interaction.response.edit_message(embed=self.view.embed, view=self.view)


class CustomEmbedFooterModal(discord.ui.Modal):
    """
    Custom Embed Footer Modal
    """

    def __init__(self, view: discord.ui.View) -> None:
        """
        Init the modal
        """
        super().__init__(title="Edit Footer")
        self.view = view
        self.text = discord.ui.TextInput(
            label="Text",
            style=discord.TextStyle.long,
            placeholder="Text",
            default=self.view.embed.footer.text,
            max_length=2048,
            min_length=1,
            required=True,
        )
        self.icon_url = discord.ui.TextInput(
            label="Icon URL",
            style=discord.TextStyle.long,
            placeholder="Icon URL",
            default=self.view.embed.footer.icon_url,
            max_length=4000,
            min_length=1,
            required=False,
        )
        self.add_item(self.text)
        self.add_item(self.icon_url)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        """
        On_submit, do stuff
        """
        self.view.embed.set_footer(text=self.text.value, icon_url=self.icon_url.value)
        for child in self.view.children:
            if isinstance(child, discord.ui.Button) and child.label == "Remove Footer":
                child.disabled = False
        await interaction.response.edit_message(embed=self.view.embed, view=self.view)


class CustomEmbedView(discord.ui.View):
    """
    Embed view for storing the embed editor
    """

    def __init__(self, ctx: commands.Context, embed: discord.Embed) -> None:
        """
        Create the embed view
        """
        super().__init__(timeout=300)
        self.completed: bool = False
        self.ctx = ctx
        self.embed: discord.Embed = embed
        
        self.add_item(CustomEmbedFieldDropdown(self.embed))

    
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        """
        If the interaction isn't by the user, return a fail.
        """
        if interaction.user != self.ctx.author:
            embed = Embed(description=f"Sorry, but this interaction can only be used by {self.ctx.author.name}.")
            await interaction.response.send_message(embed=embed, ephemeral=True)


            return False
        return True
    
   # @discord.ui.button(
    #    label="Webhook", style=discord.ButtonStyle.blurple, emoji="<:Icon_CreateWebhook:1094173698132545627>", row=0)
   # async def webhook_button(
    #    self, interaction: discord.Interaction, button: discord.Button
   # ) -> None:
    #    """
    #    Import an embed
   #     """
    #    await interaction.response.send_modal(opModal(self))

  #  @discord.ui.button(
  #      label="Export", style=discord.ButtonStyle.blurple, emoji="📤", row=0
  #  )
  #  async def export_button(self, interaction: discord.Interaction, button: discord.Button
  #  ) -> None:
   #     """
  #Export an embed
   #     """
   ##     file = discord.File(
  #          io.StringIO(json.dumps(self.embed.to_dict())), "custom_embed.json"
  #      )
  #      embed = discord.Embed(
  #          title="Exported Successfully",
   #         description="""Exported your embed successfully.""",
   #         timestamp=discord.utils.utcnow(),
   #         color=style.Color.GREEN,
   #     )
 #       await interaction.response.send_message(embed=embed, file=file)



    @discord.ui.button(
        label="Author", style=discord.ButtonStyle.blurple, row=2
    )
    async def author_button(
        self, interaction: discord.Interaction, button: discord.Button
    ) -> None:
        """
        Edit the author
        """
        await interaction.response.send_modal(CustomEmbedAuthorModal(self))

    @discord.ui.button(
        label="Title & Description", style=discord.ButtonStyle.blurple, row=2
	)
    async def base_button(
        self, interaction: discord.Interaction, button: discord.Button
    ) -> None:
        """
        Edit the base
        """
        await interaction.response.send_modal(CustomEmbedBaseModal(self))

    @discord.ui.button(
        label="Image", style=discord.ButtonStyle.blurple, row=2
    )
    async def image_button(
        self, interaction: discord.Interaction, button: discord.Button
    ) -> None:
        """
        Edit the image
        """
        await interaction.response.send_modal(CustomEmbedImageModal(self))

    @discord.ui.button(
        label="Footer", style=discord.ButtonStyle.blurple, row=2
    )
    async def footer_button(
        self, interaction: discord.Interaction, button: discord.Button
    ) -> None:
        """
        Edit the footer
        """
        await interaction.response.send_modal(CustomEmbedFooterModal(self))

    @discord.ui.button(
        label="Add Field",
        style=discord.ButtonStyle.green,
        emoji=style.Emoji.REGULAR.check,
        row=3,
    )
    async def add_field_button(
        self, interaction: discord.Interaction, button: discord.Button
    ) -> None:
        """
        Add a field
        """
        self.embed.add_field(
            name="New Field", value="Put Something here!", inline=False
        )

        if len(self.embed.fields) == 24:
            button.disabled = True
        if len(self.embed.fields) > 0:
            for child in self.children:
                if (
                    isinstance(child, discord.ui.Button)
                    and child.label == "Remove Field"
                ):
                    child.disabled = False
                elif (
                    isinstance(child, discord.ui.Button)
                    and child.label == "Clear Fields"
                ):
                    child.disabled = False

        for child in self.children:
            if (
                isinstance(child, discord.ui.Select)
                and child.placeholder == "Choose a Field to Edit"
            ):
                for option in child.options:
                    if option.label == "No Fields":
                        child.options.remove(option)
                child.options.append(
                    discord.SelectOption(
                        label=f"Edit Field {len(self.embed.fields)}",
                        description="New Field",
                        
                        value=str(len(self.embed.fields) - 1),
                    )
                )

        await interaction.response.edit_message(embed=self.embed, view=self)

    @discord.ui.button(
        label="Remove Field",
        style=discord.ButtonStyle.red,
        emoji=style.Emoji.REGULAR.cancel,
        row=3,
        disabled=True,
    )
    async def remove_field_button(
        self, interaction: discord.Interaction, button: discord.Button
    ) -> None:
        """
        Remove a field
        """
        self.embed.remove_field(len(self.embed.fields) - 1)
        if len(self.embed.fields) < 25:
            for child in self.children:
                if isinstance(child, discord.ui.Button) and child.label == "Add Field":
                    child.disabled = False
        if len(self.embed.fields) == 0:
            button.disabled = True
            for child in self.children:
                if (
                    isinstance(child, discord.ui.Button)
                    and child.label == "Clear Fields"
                ):
                    child.disabled = True

        for child in self.children:
            if (
                isinstance(child, discord.ui.Select)
                and child.placeholder == "Choose a Field to Edit"
            ):
                child.options.pop()
                if len(child.options) == 0:
                    child.options.append(
                        discord.SelectOption(
                            label="No Fields", value="no_fields"
                        )
                    )

        await interaction.response.edit_message(embed=self.embed, view=self)

    @discord.ui.button(
        label="Clear Fields",
        style=discord.ButtonStyle.red,
        emoji=style.Emoji.REGULAR.cancel,
        row=4,
        disabled=True,
    )
    async def clear_fields_button(
        self, interaction: discord.Interaction, button: discord.Button
    ) -> None:
        """
        Clear all fields
        """
        self.embed.clear_fields()
        if len(self.embed.fields) == 0:
            button.disabled = True

        for child in self.children:
            if (
                isinstance(child, discord.ui.Select)
                and child.placeholder == "Choose a Field to Edit"
            ):
                child.options = [
                    discord.SelectOption(
                        label="No Fields", value="no_fields"
                    )
                ]
            elif isinstance(child, discord.ui.Button) and child.label == "Remove Field":
                child.disabled = True

        await interaction.response.edit_message(embed=self.embed, view=self)

    @discord.ui.button(
        label="Remove Author",
        style=discord.ButtonStyle.red,
        emoji=style.Emoji.REGULAR.cancel,
        row=4,
        disabled=True,
    )
    async def remove_author_button(
        self, interaction: discord.Interaction, button: discord.Button
    ) -> None:
        """
        Remove the author
        """
        self.embed.remove_author()
        button.disabled = True
        await interaction.response.edit_message(embed=self.embed, view=self)

    @discord.ui.button(
        label="Remove Footer",
        style=discord.ButtonStyle.red,
        emoji=style.Emoji.REGULAR.cancel,
        row=4,
        disabled=True,
    )
    async def remove_footer_button(
        self, interaction: discord.Interaction, button: discord.Button
    ) -> None:
        """
        Remove the footer
        """
        self.embed.remove_footer()
        button.disabled = True
        await interaction.response.edit_message(embed=self.embed, view=self)

    @discord.ui.button(
        label="Complete",
        style=discord.ButtonStyle.green,
        emoji=style.Emoji.REGULAR.check,
        row=4,
    )
    async def complete_button(
        self, interaction: discord.Interaction, button: discord.Button
    ) -> None:
        """
        Complete the embed
        """
        await interaction.response.edit_message(embed=self.embed, view=None)
        self.completed = True
        self.stop()
    @discord.ui.button(label="Send", style=discord.ButtonStyle.green, row=0)
    async def send_(self, interaction: discord.Interaction, button: discord.Button) -> None:
        """
        This method is a callback function for the `button` interaction. It is triggered when a user clicks on the "send" button. 
        The method creates a `ChannelSelectPrompt` object and sends it as an ephemeral message to the user. It then waits for the user to select a channel.
        If a channel is selected, the method sends the embed to the selected channel and deletes the original interaction message.

        Parameters:
            interaction (discord.Interaction): The interaction object representing the current interaction.
            button (discord.Button): The button object representing the "send" button.
        """
        prompt = ChannelSelectPrompt(
            "Select a channel to send this embed...", True, 1)
        await interaction.response.send_message(view=prompt, ephemeral=True)
        await prompt.wait()
        if prompt.values:
            if not isinstance(prompt.values[0], (StageChannel, ForumChannel, CategoryChannel)):
                await prompt.values[0].send(embed=self.embed)
                
                
                await interaction.message.delete() 