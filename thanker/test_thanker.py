import asynctest

from . import Thanker


class TestThanker(asynctest.TestCase):
    use_default_loop = True

    async def setUp(self) -> None:
        self.thanker = Thanker(["aiohttp"])

    async def test_style(self) -> None:
        async with self.thanker as thanks:
            self.assertIsInstance(await thanks.style(), str)
