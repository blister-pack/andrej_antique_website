from fastapi import FastApi
from typing import Optional
from pydantic import BaseModel

app = FastApi()

class Item(BaseModel):
    title: str
    description: str
    price: float
    #TODO complete w relevant categories


