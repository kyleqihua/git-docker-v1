from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from pydantic_ai import Agent

app = FastAPI()

# 静态文件配置
app.mount("/static", StaticFiles(directory="static"), name="static")

# 模板配置
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "message": "Hello from FastAPI with HTMX!"}
    )
