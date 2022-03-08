import uvicorn
import os

from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from .._thanker import Thanker


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

templates = Jinja2Templates(
    directory=os.path.join(
        CURRENT_DIR,
        "template"
    )
)


async def home(request: Request):
    form = await request.form()

    if form:
        if "packages" not in form:
            return RedirectResponse("/")

        search = form["packages"]

        async with Thanker(form["packages"].split(",")) as thanker:
            packages = [
                package async for package
                in thanker.scan_all()
            ]
    else:
        packages = None
        search = None

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "packages": packages,
         "search": search}
    )


APP = Starlette(routes=[
    Route("/", home, methods=["GET", "POST"]),
    Mount("/assets", StaticFiles(
        directory=os.path.join(
            CURRENT_DIR,
            "assets"
        )
    ), name="assets")
])


def webpanel(**kwargs):
    uvicorn.run(APP, **kwargs)
