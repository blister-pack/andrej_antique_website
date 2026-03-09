from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from schemas import Item

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


@app.get("/item-list/")
def get_all_items():
    return fake_db_items


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


@app.delete("/delete-item/{item_id}")
def delete_item(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
):
    # if not fake_db_items[item_id]:
    #     raise HTTPException(
    #         status_code=400,
    #         detail="Item does not exist.",
    #     )
    del fake_db_items[item_id]
    return {"Message": "Item deleted."}
#TODO fix mistake when deleting non-existing item
