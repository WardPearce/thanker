# Don't be a wanker, be a thanker!
Automatically give thanks to Pypi packages you use in your project!

## Index
- [Install](#install)
- [Examples](#examples)
    - [Command-line](#command-line)
    - [Programmatically](#programmatically)
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
                             file.
  --gratitude_level INTEGER  Basically the depth of requirements we should go
                             to
  --layout TEXT              The layout of the thanks, can be any pypi info
                             parameter
  --display BOOLEAN          If the output should be displayed in console.
  --save FILENAME            File to save thanks to
  --help                     Show this message and exit.
```
![command line gif](https://i.imgur.com/CBsvyB0.gif)

### Programmatically
```py
import asyncio
from thanker import Thanker

async def example() -> None:
    async with Thanker(packages=["thanker"], gratitude_level=None) as thanks:
        print(await thanks.style("- [{name}]({package_url}) by {author}"))

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
```

## Supported Pypi parameters
![pypi parameters](https://i.imgur.com/WQoBl2r.png)

## Thanks to
- [aiohttp](https://pypi.org/project/aiohttp/) by Nikolay Kim
- [attrs](https://pypi.org/project/attrs/) by Hynek Schlawack
- [chardet](https://pypi.org/project/chardet/) by Mark Pilgrim
- [multidict](https://pypi.org/project/multidict/) by Andrew Svetlov
- [async-timeout](https://pypi.org/project/async-timeout/) by Andrew Svetlov
- [yarl](https://pypi.org/project/yarl/) by Andrew Svetlov
- [idna](https://pypi.org/project/idna/) by Kim Davies
- [typing-extensions](https://pypi.org/project/typing-extensions/) by Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee
- [click](https://pypi.org/project/click/) by Armin Ronacher
- [asynctest](https://pypi.org/project/asynctest/) by Martin Richard
- [aiofiles](https://pypi.org/project/aiofiles/) by Tin Tvrtkovic