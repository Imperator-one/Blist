from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

# Читаем HTML файл один раз при запуске
with open("index.html", "r", encoding="utf-8") as file:
    HTML_TEMPLATE = file.read()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Отображает ваш HTML файл"""
    return HTML_TEMPLATE

@app.get("/{name}", response_class=HTMLResponse)
async def greet(name: str):
    """Отображает ваш HTML файл с подстановкой имени"""
    # Просто заменяем плейсхолдеры на значения
    html = HTML_TEMPLATE.replace("{{name}}", name)
    html = html.replace("{{title}}", f"Привет, {name}!")
    return html

@app.get("/page/{page_id}", response_class=HTMLResponse)
async def dynamic_page(page_id: int, name: str = "Гость"):
    """Отображает ваш HTML с любыми параметрами"""
    html = HTML_TEMPLATE
    # Заменяем все плейсхолдеры, какие есть в вашем HTML
    html = html.replace("{{page_id}}", str(page_id))
    html = html.replace("{{name}}", name)
    html = html.replace("{{year}}", "2026")
    # Добавьте столько замен, сколько нужно для вашего HTML
    return html