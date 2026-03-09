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
number_of_items = 1


class Item(BaseModel):
    title: str
    description: str = "womp womp"
    price: float = 0.0
    negotiable: bool = False
    # TODO complete w relevant categories - {date_created};


@app.get("/item-list/")
def get_all_items(
    item_list: Annotated[dict, Path(title="A list of all inserted items")],
):
    return fake_db_items


# TODO fix the damn broken list


@app.get("/get-item/{item_id}")
def get_item(item_id: Annotated[int, Path(title="The ID of the item to get")]):
    return fake_db_items[item_id]


@app.post("/create-item/")
def post_item(item: Item):
    """
    The function posts a new item to the fake DB. The item_id is self-generated
    and based on the number of items already created. This ensures every ID is
    and never overwritten or reused.
    """
    item_id = number_of_items + 1
    fake_db_items[item_id] = item
    return fake_db_items[item_id]


@app.put("/update-item/{item_id}")
def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    item: Item,
):
    update_item_helper = item
    fake_db_items[item_id] = update_item_helper
    return update_item_helper
