import asyncio
from thanker import Thanker


async def example() -> None:
    async with Thanker(packages=["thanker"]) as thanks:
        print(await thanks.style("- [{name}]({package_url}) by {author}"))

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
