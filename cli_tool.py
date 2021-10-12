import click
import asyncio

from typing import Optional
from thanker import Thanker

loop = asyncio.get_event_loop()


@click.command()
@click.option("--packages", type=str,
              help="List of packages to thank, seperated by a comma")
@click.option("--gratitude_level", type=int, default=None,
              help="Basically the depth of requirements we should go to")
@click.option("--layout", type=str,
              default="- [{name}]({package_url}) by {author}",
              help=" The layout of the thanks, can be any pypi info parameter")
@click.option("--display", default=True, type=bool,
              help="If the output should be displayed in console.")
@click.option("--save", type=click.File(mode="w+"), default=None,
              help="File to save thanks to")
def cli(packages: str, gratitude_level: Optional[int], layout: str,
        display: bool, save) -> None:
    thanker = Thanker(
        packages=packages.split(","),
        gratitude_level=gratitude_level
    )

    async def run_thanks() -> str:
        async with thanker as thanks:
            return await thanks.style(layout=layout)

    thanks_to = loop.run_until_complete(run_thanks())
    if display:
        click.echo(thanks_to)
    if save:
        save.write(thanks_to)
