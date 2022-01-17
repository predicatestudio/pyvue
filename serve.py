from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
import pyvue
from pathlib import Path


app = FastAPI()
# template = Jinja2Templates(".")


def get_panels():
    """Dynamically searches for panels with an example.html"""
    panels = []
    for dir in [obj for obj in Path(__file__).parent.iterdir() if obj.is_dir()]:
        if dir.joinpath("example.html").exists():
            panels.append(str(dir.stem))
    return panels


# Mount panel dirs as static files
for panel in get_panels():
    app.mount("/" + panel, StaticFiles(directory=panel), name=panel)

# Index with links to examples
@app.get("/")
def home():
    return HTMLResponse(pyvue.core.main("/home/benjamin/predicatestudio/pyvue/SwitchPanel/components/Switch.vue"))
    return pyvue.core.main("/home/benjamin/predicatestudio/pyvue/SwitchPanel/components/Switch.vue")
    # var = pyvue
    # return pyvue

def main():
    import uvicorn
    uvicorn.run("serve:app", reload=True)


if __name__ == "__main__":
    main()
