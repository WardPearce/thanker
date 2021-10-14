import asyncio
from thanker import Thanker, GroupBy


async def example() -> None:
    async with Thanker(packages=["thanker"], gratitude_level=None) as thanks:
        # No grouping
        print(await thanks.style("- [{name}]({package_url}) by {author}"))

        # Grouping requirements by author
        print(await thanks.style(
            layout="- [{name}]({package_url})",
            group_by=GroupBy(
                group="author",
                layout="### Created by {author}\n{__layout__}"
            )
        ))

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
