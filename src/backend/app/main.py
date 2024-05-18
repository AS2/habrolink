from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import messages, search, users

app = FastAPI()

origins = [
    "http://localhost:8000",
    "localhost:8000",
    "http://habrolink_backend:8000",
    "habrolink_backend:8000"
]

app.include_router(messages.router)
app.include_router(search.router)
app.include_router(users.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}