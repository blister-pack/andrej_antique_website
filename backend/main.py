from fastapi import Depends, FastAPI, Path, HTTPException, Query
from typing import Annotated
from sqlmodel import Session, select
from backend.db import create_db_and_tables, get_session
from backend.schemas import Item, ItemCreate, ItemPublic, ItemUpdate
from contextlib import asynccontextmanager


SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/get-item-list/", response_model=list[ItemPublic])
def get_all_items(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    item_list = session.exec(select(Item).offset(offset).limit(limit)).all()
    return item_list


@app.get("/get-item/{item_id}", response_model=ItemPublic)
def get_item(
    session: SessionDep,
    item_id: Annotated[int, Path(title="The ID of the item to get")],
):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Selected item does not exist.")
    return item


@app.post("/create-item/", response_model=ItemPublic)
def post_item(
    session: SessionDep,
    item: ItemCreate,
):
    db_item = Item.model_validate(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@app.patch("/update-item/{item_id}", response_model=ItemPublic)
def update_item(
    session: SessionDep,
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    item: ItemUpdate,
):
    db_item = session.get(Item, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    item_data = item.model_dump(exclude_unset=True)
    db_item.sqlmodel_update(item_data)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@app.delete("/delete-item/{item_id}")
def delete_item(
    session: SessionDep,
    item_id: Annotated[int, Path(title="The ID of the item to get")],
):
    db_item = session.get(Item, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(db_item)
    session.commit()
    return {"Message": f"Item {db_item.title} successfully deleted."}
