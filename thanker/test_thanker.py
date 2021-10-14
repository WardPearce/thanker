import asynctest
from os import path

from . import Thanker, GroupBy


class TestThanker(asynctest.TestCase):
    use_default_loop = True

    async def setUp(self) -> None:
        self.thanker = Thanker(["thanker"])

    async def test_style(self) -> None:
        async with self.thanker as thanks:
            self.assertIsInstance(await thanks.style(), str)

    async def test_package_info(self) -> None:
        async with self.thanker as thanks:
            self.assertIsInstance(
                await thanks.package_info("aiohttp"),
                dict
            )

    async def test_scan(self) -> None:
        async with self.thanker as thanks:
            async for info in thanks.scan("aiohttp"):
                self.assertIsInstance(info, dict)

    async def test_load_from_requirements(self) -> None:
        async with self.thanker as thanks:
            await thanks.load_from_requirements(
                path.join(
                    path.dirname(path.realpath(__file__)),
                    "../requirements.txt"
                )
            )

    async def test_group_by(self) -> None:
        async with self.thanker as thanks:
            await thanks.style(
                layout="- [{name}]({package_url})",
                group_by=GroupBy(
                    group="author",
                    layout="### Created by {author}\n{__layout__}"
                )
            )
