from fastapi import Depends, FastAPI, Path, HTTPException, Query
from typing import Annotated
from sqlmodel import Session, select
from backend.db import create_db_and_tables, get_session
from backend.schemas import Item
from contextlib import asynccontextmanager


SessionDep = Annotated[Session, Depends(get_session)]
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


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


@app.get("/get-item-list/", response_model=list[Item])
def get_all_items(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    item_list = session.exec(select(Item).offset(offset).limit(limit)).all()
    return item_list


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
    fake_db_items[item_id] = item.model_dump()
    return fake_db_items[item_id]


@app.put("/update-item/{item_id}")
def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    item: Item,
):
    update_item_helper = item
    fake_db_items[item_id] = update_item_helper.model_dump()
    return update_item_helper


@app.delete("/delete-item/{item_id}")
def delete_item(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
):
    if item_id not in fake_db_items.keys():
        raise HTTPException(
            status_code=404,
            detail="Item does not exist.",
        )
    del fake_db_items[item_id]
    return {"Message": "Item deleted."}
