from fastapi import FastApi
from typing import Optional
from pydantic import BaseModel

app = FastApi()

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
def get_item(item_id: int):
    pass
