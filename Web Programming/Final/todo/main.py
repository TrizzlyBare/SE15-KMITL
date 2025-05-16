from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

data = {
    1: {"title": "To-do 1", "body": "This is To-do 1"},
    2: {"title": "To-do 2", "body": "This is To-do 2"},
}


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "data": data})


@app.get("/todo/{id}", response_class=HTMLResponse)
async def todo(id: int, request: Request):
    content = data.get(id)
    if content:
        content["id"] = id
    return templates.TemplateResponse(
        "todo.html", {"request": request, "content": content}
    )


@app.get("/create_todo", response_class=HTMLResponse)
async def create_todo(request: Request):
    return templates.TemplateResponse("addtodo.html", {"request": request})


@app.post("/create", response_class=RedirectResponse)
async def create(title: str = Form(...), body: str = Form(...)):
    id = len(data) + 1
    data[id] = {"title": title, "body": body}
    return RedirectResponse(url=f"/todo/{id}")


@app.delete("/delete/{id}", response_class=RedirectResponse)
async def delete(id: int):
    data.pop(id, None)
    return RedirectResponse(url="/home")
