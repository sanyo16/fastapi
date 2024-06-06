from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    text: str
    is_done: bool = False


items = []


@app.get("/")
def root():
    return {"FFF":"you"}


@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items


@app.get("/items", response_model=list[Item])
def list_items(limit: int = 3):
    return items[0:limit]


@app.get("/items/{id}", response_model=Item)
def get_item(id: int) -> Item:
    if id < len(items):
        return items[id]
    raise HTTPException(status_code=404, detail="item not found")