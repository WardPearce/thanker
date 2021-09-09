# Don't be a wanker, be a thanker!
Automatically give thanks to Pypi packages you use in your project!

## Install
- `pip3 install thanker`

## Example
```py
import asyncio
from thanker import Thanker


async def example() -> None:
    async with Thanker(packages=["thanker"], gratitude_level=None) as thanks:
        print(await thanks.style("- [{name}]({package_url}) by {author}"))

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
```

## TODO
- Auto docs

## Thanks to
- [aiohttp](https://pypi.org/project/aiohttp/) by Nikolay Kim
- [attrs](https://pypi.org/project/attrs/) by Hynek Schlawack
- [chardet](https://pypi.org/project/chardet/) by Mark Pilgrim
- [multidict](https://pypi.org/project/multidict/) by Andrew Svetlov
- [async-timeout](https://pypi.org/project/async-timeout/) by Andrew Svetlov
- [yarl](https://pypi.org/project/yarl/) by Andrew Svetlov
- [idna](https://pypi.org/project/idna/) by Kim Davies
- [typing-extensions](https://pypi.org/project/typing-extensions/) by Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee
- [asynctest](https://pypi.org/project/asynctest/) by Martin Richard
- [sphinx-material](https://pypi.org/project/sphinx-material/) by Kevin Sheppard
- [Sphinx](https://pypi.org/project/Sphinx/) by Georg Brandl
- [sphinxcontrib-applehelp](https://pypi.org/project/sphinxcontrib-applehelp/) by Georg Brandl
- [sphinxcontrib-devhelp](https://pypi.org/project/sphinxcontrib-devhelp/) by Georg Brandl
- [sphinxcontrib-jsmath](https://pypi.org/project/sphinxcontrib-jsmath/) by Georg Brandl
- [sphinxcontrib-htmlhelp](https://pypi.org/project/sphinxcontrib-htmlhelp/) by Georg Brandl
- [sphinxcontrib-serializinghtml](https://pypi.org/project/sphinxcontrib-serializinghtml/) by Georg Brandl
- [sphinxcontrib-qthelp](https://pypi.org/project/sphinxcontrib-qthelp/) by Georg Brandl
- [Jinja](https://pypi.org/project/Jinja/) by Armin Ronacher
- [Pygments](https://pypi.org/project/Pygments/) by Georg Brandl
- [docutils](https://pypi.org/project/docutils/) by David Goodger
- [snowballstemmer](https://pypi.org/project/snowballstemmer/) by Snowball Developers
- [Babel](https://pypi.org/project/Babel/) by Armin Ronacher
- [pytz](https://pypi.org/project/pytz/) by Stuart Bishop
- [alabaster](https://pypi.org/project/alabaster/) by Jeff Forcier
- [imagesize](https://pypi.org/project/imagesize/) by Yoshiki Shibukawa
- [requests](https://pypi.org/project/requests/) by Kenneth Reitz
- [certifi](https://pypi.org/project/certifi/) by Kenneth Reitz
- [setuptools](https://pypi.org/project/setuptools/) by Python Packaging Authority
- [packaging](https://pypi.org/project/packaging/) by Donald Stufft and individual contributors
- [pyparsing](https://pypi.org/project/pyparsing/) by Paul McGuire
- [BeautifulSoup](https://pypi.org/project/BeautifulSoup/) by Leonard Richardson
- [css-html-js-minify](https://pypi.org/project/css-html-js-minify/) by Juan Carlos
- [lxml](https://pypi.org/project/lxml/) by lxml dev team
- [sphinxcontrib-trio](https://pypi.org/project/sphinxcontrib-trio/) by Nathaniel J. Smith