import re
from typing import TYPE_CHECKING, AsyncGenerator, Optional

if TYPE_CHECKING:
    from . import Thanker


class Scanner:
    def __init__(self, upper: "Thanker") -> None:
        self._upper = upper
        self.__ignore = []

    async def scan(self, name: str, current_gratitude: Optional[int] = None,
                   ) -> AsyncGenerator[dict, None]:
        new_gratitude = (
            current_gratitude - 1 if current_gratitude is not None
            else None
        )

        name = (re.sub("[^a-zA-Z\\-]+", "", name)).lower()
        if new_gratitude != -1 and name not in self.__ignore:
            self.__ignore.append(name)

            info = await self._upper.package_info(name)
            if info:
                yield info

                if info["requires_dist"]:
                    for requirement in info["requires_dist"]:
                        async for info_ in self.scan(requirement,
                                                     new_gratitude):
                            yield info_
