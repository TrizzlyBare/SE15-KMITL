from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

data = {
    1: {"title": "Note 1", "body": "This is note 1"},
    2: {"title": "Note 2", "body": "This is note 2"},
}


@app.get("/home", response_class=HTMLResponse)
async def homePage(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "data": data})


@app.get("/notes/{note_id}", response_class=HTMLResponse)
async def notebyid(note_id: int, request: Request):
    note = data.get(note_id)
    return templates.TemplateResponse("notes.html", {"request": request, "note": note})


@app.get("/create_notes", response_class=HTMLResponse)
async def createnotepage(request: Request):
    return templates.TemplateResponse("createnotes.html", {"request": request})


@app.post("/create", response_class=RedirectResponse)
async def createNote(title: str = Form(...), body: str = Form(...)):
    note_id = len(data) + 1
    data[note_id] = {"title": title, "body": body}
    return RedirectResponse(url=f"/notes/{note_id}")
