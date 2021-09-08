import re

from typing import AsyncGenerator, List, Optional
from aiohttp import ClientSession


__version__ = "0.0.1"
__url__ = "https://thanker.readthedocs.io/en/latest/"
__description__ = "Don't be a wanker, be a thanker!"
__author__ = "WardPearce"
__author_email__ = "wardpearce@protonmail.com"
__license__ = " Apache-2.0"


class Thanker:
    __pypi_api = "https://pypi.python.org/pypi/{name}/json"

    def __init__(self, packages: List[str],
                 gratitude_level: Optional[int] = None) -> None:
        """Used to thank developers of python packages.

        Parameters
        ----------
        packages : List[str]
            List of root packages.
        gratitude_level : Optional[int], optional
            Basically the depth of requirements we should go to, by default 3
        """

        self._packages = packages
        self._gratitude_level = gratitude_level

    async def __aenter__(self):
        self._requests = ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._requests.close()

    async def package_info(self, name: str) -> Optional[dict]:
        """Get information about a package.

        Parameters
        ----------
        name : str

        Returns
        -------
        Optional[dict]
        """

        url = self.__pypi_api.format(name=name)
        async with self._requests.get(url) as resp:
            if resp.status == 200:
                return (await resp.json())["info"]

    async def scan(self, name: str, current_gratitude: Optional[int] = None
                   ) -> AsyncGenerator[dict, None]:
        """Scan for all requirements of a package .

        Parameters
        ----------
        name : str
        current_gratitude : Optional[int], optional
            by default None

        Yields
        -------
        dict
        """

        new_gratitude = (
            current_gratitude - 1 if current_gratitude is not None
            else None
        )

        if new_gratitude != -1:
            name = re.sub("[^a-zA-Z\\-]+", "", name)

            info = await self.package_info(name)
            if info:
                yield info

                if info["requires_dist"]:
                    for requirement in info["requires_dist"]:
                        async for info_ in self.scan(requirement,
                                                     new_gratitude):
                            yield info_

    async def style(self, layout: str = "- [{name}]({package_url}) by {author}") -> str:  # noqa: E501
        """Return a string containing all the packages in this package as markdown.

        Parameters
        ----------
        layout : str, optional
            The layout of the thanks, can be any pypi parameter,
            e.g. https://pypi.org/pypi/thanker/json/,
            by default "[{name}]({package_url}) by {author}"

        Returns
        -------
        str
        """

        text = ""
        for package in self._packages:
            async for info in self.scan(package, self._gratitude_level):
                text += layout.format_map(info) + "\n"

        return text
