from fastapi import FastAPI
from typing import List
from .db.operations import get_articles
from .db.schemas import Article

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/articles", response_model=List[Article])
def read_articles():
    """
    Retrieve all articles from the database.
    """
    articles = get_articles()
    return articles
