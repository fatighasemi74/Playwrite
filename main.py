from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/assets", StaticFiles(directory="templates/assets"), name="assets")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    
@app.get("/index")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/shop")
def read_root(request: Request):
    return templates.TemplateResponse("shop.html", {"request": request})

@app.get("/about")
def read_root(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/services")
def read_root(request: Request):
    return templates.TemplateResponse("services.html", {"request": request})

@app.get("/blog")
def read_root(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request})

@app.get("/contact")
def read_root(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/cart")
def read_root(request: Request):
    print(request.method)
    return templates.TemplateResponse("cart.html", {"request": request})

@app.get("/shop")
def read_root(request: Request):
    return templates.TemplateResponse("shop.html", {"request": request})

@app.get("/checkout")
def read_root(request: Request):
    print(request.method)
    return templates.TemplateResponse("checkout.html", {"request": request})

@app.get("/thankyou")
def read_root(request: Request):
    print(request.method)
    return templates.TemplateResponse("thankyou.html", {"request": request})

