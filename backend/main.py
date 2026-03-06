from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

fake_db_items = {
    1: {
        "title": "Grand Clock",
        "description": "A big ol' Clock",
        "price": 250,
        "negotiable": False,
    },
}


class Item(BaseModel):
    title: str
    description: str | None = None
    price: float
    negotiable: bool
    # TODO complete w relevant categories


@app.get("/get-item/{item_id}")
def get_item(item_id: Annotated[int, Path(title="The ID of the item to get")]):
    return fake_db_items[item_id]


@app.put("/update-item/{item_id}")
def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    item: Item,
):
    item[item_id] = item
    return item[item_id]
