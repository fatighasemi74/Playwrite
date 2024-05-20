from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles

app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")

# @app.get("/home")
# def read_root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

@app.get("/")
def read_root():
    return {"Hello": "World"}