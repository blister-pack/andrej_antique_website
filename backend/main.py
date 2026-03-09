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
    price: float = 0.0
    negotiable: bool = False
    # TODO complete w relevant categories - {date_created};


@app.get("/item-list")
def get_all_items(item_list: Annotated[dict, Path(title="A list of all inserted items")]):
    return fake_db_items

@app.get("/get-item/{item_id}")
def get_item(item_id: Annotated[int, Path(title="The ID of the item to get")]):
    return fake_db_items[item_id]


@app.post("/create-item/{item_id}")
def post_item(item_id: int, item: Item):
    if item_id in fake_db_items:
        pass
    

@app.put("/update-item/{item_id}")
def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    item: Item,
):
    update_item_helper = item
    fake_db_items[item_id] = update_item_helper
    return update_item_helper

