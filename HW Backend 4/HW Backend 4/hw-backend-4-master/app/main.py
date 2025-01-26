from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import HTTPException
from .repository import BooksRepository

app = FastAPI()


templates = Jinja2Templates(directory="templates")
repository = BooksRepository()


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/books")
def list_books(request: Request, page: int = 1, per_page: int = 10):
    offset = (page - 1) * per_page
    books = repository.get_books(offset=offset, limit=per_page)
    has_next = len(repository.books) > offset + per_page
    has_prev = offset > 0
    return templates.TemplateResponse("books/index.html", {
        "request": request,
        "books": books,
        "page": page,
        "has_next": has_next,
        "has_prev": has_prev,
    })

@app.get("/books/new")
def new_book_form(request: Request):
    return templates.TemplateResponse("books/new.html", {"request": request})

@app.post("/books")
def create_book(
    title: str = Form(...),
    author: str = Form(...),
    year: int = Form(...),
    total_pages: int = Form(...),
    genre: str = Form(...),
):
    repository.create_book(title, author, year, total_pages, genre)
    return RedirectResponse("/books", status_code=303)


@app.get("/books/{id}")
def get_book_detail(request: Request, id: int):
    book = repository.get_book(book_id=id)
    if not book:
        raise HTTPException(status_code=404, detail="Not Found")
    return templates.TemplateResponse("books/index.html", {
        "request": request,
        "books": [book],
        "page": None,
        "has_next": False,
        "has_prev": False,
        "is_detail": True,
    })
