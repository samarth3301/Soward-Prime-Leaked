from __future__ import annotations

import discord
from discord.ext import menus
from discord.ext import commands
from .paginator import Paginator as SowardPaginator
from discord.ext.commands import Context, Paginator as CmdPaginator
from typing import Any


class FieldPagePaginator(menus.ListPageSource):

    def __init__(self,
                 entries: list[tuple[Any, Any]],
                 *,
                 per_page: int = 10,
                 inline: bool = False,
                 **kwargs) -> None:
        super().__init__(entries, per_page=per_page)
        self.embed: discord.Embed = discord.Embed(
            title=kwargs.get('title'),
            description=kwargs.get('description'),
            color=0x2f3136)
        self.inline: bool = inline

    async def format_page(self, menu: SowardPaginator,
                          entries: list[tuple[Any, Any]]) -> discord.Embed:
        self.embed.clear_fields()

        for key, value in entries:
            self.embed.add_field(name=key, value=value, inline=self.inline)

        maximum = self.get_max_pages()
        if maximum > 1:
            text = f'Soward | Page {menu.current_page + 1}/{maximum}'
            self.embed.set_footer(
                text=text,
                icon_url=
                "https://images-ext-2.discordapp.net/external/4esbAj3OnTCoapLaI21I7XvPXF6ao7k0M8Z1AC3vWHE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png"
            )
            self.embed.timestamp = discord.utils.utcnow()
        return self.embed


class TextPaginator(menus.ListPageSource):

    def __init__(self, text, *, prefix='```', suffix='```', max_size=2000):
        pages = CmdPaginator(prefix=prefix,
                             suffix=suffix,
                             max_size=max_size - 200)
        for line in text.split('\n'):
            pages.add_line(line)

        super().__init__(entries=pages.pages, per_page=1)

    async def format_page(self, menu, content):
        maximum = self.get_max_pages()
        if maximum > 1:
            return f'{content}\nSoward • Page {menu.current_page + 1}/{maximum}'
        return content


class DescriptionEmbedPaginator(menus.ListPageSource):

    def __init__(self,
                 entries: list[Any],
                 *,
                 per_page: int = 10,
                 **kwargs) -> None:
        super().__init__(entries, per_page=per_page)
        self.embed: discord.Embed = discord.Embed(
            title=kwargs.get('title'),
            color=0x2f3136,
        )

    async def format_page(self, menu: SowardPaginator,
                          entries: list[tuple[Any, Any]]) -> discord.Embed:
        self.embed.clear_fields()

        self.embed.description = '\n'.join(entries)
        self.embed.timestamp = discord.utils.utcnow()
        maximum = self.get_max_pages()
        if maximum > 1:
            text = f'Soward • Page {menu.current_page + 1}/{maximum}'
            self.embed.set_footer(
                text=text,
                icon_url=
                "https://images-ext-2.discordapp.net/external/4esbAj3OnTCoapLaI21I7XvPXF6ao7k0M8Z1AC3vWHE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1013771497157972008/35d7b263c98b9e5df51f19914d747394.png"
            )

        return self.embed
