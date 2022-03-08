# Don't be a wanker, be a thanker!
Automatically give thanks to Pypi packages you use in your project!

## Index
- [Install](#install)
- [Examples](#examples)
    - [Command-line](#command-line)
    - [Programmatically](#programmatically)
    - [Webpanel](#webpanel)
- [Supported Pypi parameters](#supported-pypi-parameters)
- [Thanks to](#thanks-to)

## Install
`pip3 install thanker`

## Examples
### Command-line
```
Usage: thanks [OPTIONS]

Options:
  --packages TEXT            List of packages to thank, seperated by a comma
  --requirements PATH        Used to load a requirements from a requirements
                             file
  --gratitude_level INTEGER  Basically the depth of requirements we should go
                             to
  --layout TEXT              The layout of the thanks, can be any pypi info
                             parameter
  --display BOOLEAN          If the output should be displayed in console
  --save FILENAME            File to save thanks to
  --group_by TEXT            Pypi parameter to group requirements by
  --group_by_layout TEXT     Layout for group by
  --help                     Show this message and exit.
```
![command line gif](https://i.imgur.com/CBsvyB0.gif)

### Programmatically
```py
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
```

### Webpanel
```py
from thanker import webpanel

if __name__ == "__main__":
    webpanel()
```
![Image of thanker webpanel, with uvicorn & starlette as the provided packages.](https://i.imgur.com/wEmA3hZ.png)


## Supported Pypi parameters
![pypi parameters](https://i.imgur.com/WQoBl2r.png)

## Thanks to
### Created by Nikolay Kim
- [aiohttp](https://pypi.org/project/aiohttp/)
### Created by Hynek Schlawack
- [attrs](https://pypi.org/project/attrs/)
### Created by Mark Pilgrim
- [chardet](https://pypi.org/project/chardet/)
### Created by Andrew Svetlov
- [multidict](https://pypi.org/project/multidict/)
- [async-timeout](https://pypi.org/project/async-timeout/)
- [yarl](https://pypi.org/project/yarl/)
### Created by Kim Davies
- [idna](https://pypi.org/project/idna/)
### Created by Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee
- [typing-extensions](https://pypi.org/project/typing-extensions/)
### Created by Armin Ronacher
- [click](https://pypi.org/project/click/)
### Created by Martin Richard
- [asynctest](https://pypi.org/project/asynctest/)
### Created by Tin Tvrtkovic
- [aiofiles](https://pypi.org/project/aiofiles/)