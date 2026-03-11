from sqlmodel import SQLModel, Field


class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str = "womp womp"
    price: float = 0.0
    negotiable: bool = False
    # TODO complete w relevant categories - {date_created};