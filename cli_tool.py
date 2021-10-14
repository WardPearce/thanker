import click
import asyncio

from typing import Optional, TextIO
from thanker import Thanker, GroupBy

loop = asyncio.get_event_loop()


@click.command()
@click.option("--packages", type=str, default="",
              help="List of packages to thank, seperated by a comma")
@click.option("--requirements", type=click.Path(exists=True, readable=True),
              help="Used to load a requirements from a requirements file",
              default=None)
@click.option("--gratitude_level", type=int, default=None,
              help="Basically the depth of requirements we should go to")
@click.option("--layout", type=str,
              default="- [{name}]({package_url}) by {author}",
              help=" The layout of the thanks, can be any pypi info parameter")
@click.option("--display", default=True, type=bool,
              help="If the output should be displayed in console")
@click.option("--save", type=click.File(mode="w+"), default=None,
              help="File to save thanks to")
@click.option("--group_by", default=None, type=str,
              help="Pypi parameter to group requirements by")
@click.option("--group_by_layout", default="Created by {author}\n{__layout__}",
              type=str, help="Layout for group by")
def cli(packages: str, gratitude_level: Optional[int], layout: str,
        display: bool, save: TextIO, requirements: Optional[str],
        group_by: Optional[str], group_by_layout: str) -> None:
    thanker = Thanker(
        packages=packages.split(","),
        gratitude_level=gratitude_level
    )

    async def run_thanks() -> str:
        async with thanker as thanks:
            if requirements:
                await thanks.load_from_requirements(requirements)

            return await thanks.style(
                layout=layout,
                group_by=GroupBy(
                    group=group_by,
                    layout=group_by_layout
                ) if group_by else None
            )

    thanks_to = loop.run_until_complete(run_thanks())
    if display:
        click.echo(thanks_to)
    if save:
        save.write(thanks_to)
