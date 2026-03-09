from pydantic import BaseModel

class Item(BaseModel):
    title: str
    description: str = "womp womp"
    price: float = 0.0
    negotiable: bool = False
    # TODO complete w relevant categories - {date_created};