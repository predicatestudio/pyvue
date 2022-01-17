from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path


app = FastAPI()
app.mount("/static", StaticFiles(directory=Path(__file__).parent), name="static")


@app.get("/")
def home(request: Request):
    return RedirectResponse("static/example.html")


def main():
    import uvicorn

    uvicorn.run("serve:app", reload=True)


if __name__ == "__main__":
    main()
