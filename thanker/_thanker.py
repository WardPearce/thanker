import asyncio

from typing import AsyncGenerator, List, Optional
from aiohttp import ClientSession

from ._scanner import Scanner


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
            Basically the depth of requirements we should go to,
            by default None
        """

        self._packages = packages
        self._gratitude_level = gratitude_level

    async def __aenter__(self) -> "Thanker":
        self._requests = ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
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

    async def scan_all(self) -> AsyncGenerator[dict, None]:
        """Scans all packages given.

        Yields
        -------
        dict
        """

        async def convert_to_list(requirement: str) -> List[dict]:
            infos = []
            async for info_ in self.scan(requirement):
                infos.append(info_)
            return infos

        results = await asyncio.gather(*[
            convert_to_list(package) for package in self._packages
        ])

        for result in results:
            for info_ in result:
                yield info_

    async def scan(self, name: str) -> AsyncGenerator[dict, None]:
        """Scan for all requirements of a package .

        Parameters
        ----------
        name : str

        Yields
        -------
        dict
        """

        async for info in Scanner(self).scan(name, self._gratitude_level):
            yield info

    async def style(self, layout: str = "- [{name}]({package_url}) by {author}") -> str:  # noqa: E501
        """Return a string containing all the packages in this package.

        Parameters
        ----------
        layout : str, optional
            The layout of the thanks, can be any pypi info parameter,
            e.g. https://pypi.org/pypi/thanker/json/,
            by default "- [{name}]({package_url}) by {author}"

        Returns
        -------
        str
        """

        text = ""
        async for info in self.scan_all():
            text += layout.format_map(info) + "\n"

        return text
