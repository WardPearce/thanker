import asynctest

from . import Thanker


class TestThanker(asynctest.TestCase):
    use_default_loop = True

    async def setUp(self) -> None:
        self.thanker = Thanker(["thanker"])

    async def test_style(self) -> None:
        async with self.thanker as thanks:
            self.assertIsInstance(await thanks.style(), str)

    async def test_package_info(self) -> None:
        async with self.thanker as thinks:
            self.assertIsInstance(
                await thinks.package_info("aiohttp"),
                dict
            )

    async def test_scan(self) -> None:
        async with self.thanker as thinks:
            async for info in thinks.scan("aiohttp"):
                self.assertIsInstance(info, dict)
