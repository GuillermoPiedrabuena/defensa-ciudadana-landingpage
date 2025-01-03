from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

# Define las rutas estáticas y los templates
STATIC_DIR = Path(__file__).parent / "statics"
TEMPLATE_DIR = Path(__file__).parent / "templates"

app.mount("/statics", StaticFiles(directory=STATIC_DIR), name="statics")
templates = Jinja2Templates(directory=STATIC_DIR)

@app.get("/alimentos", response_class=HTMLResponse)
async def get_alimentos(request: Request):
    return templates.TemplateResponse("alimentos.html", {
        "request": request, 
        "logo_url": "/statics/logo.png",
        "lawyers_url": "/statics/df_lawyers.jpg",
    
    })
