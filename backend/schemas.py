from sqlmodel import SQLModel, Field


class ItemBase(SQLModel):
    title: str = Field(default="Item name", index=True)
    description: str | None = Field(default="No description available.")
    price: float = Field(default=0.0, index=True)
    negotiable: bool = Field(default=False)
    # ID is optional in Python so that the DB itself generates it
    # TODO complete w relevant categories - {date_created};


class Item(ItemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class ItemPublic(ItemBase):
    id: int


class ItemCreate(ItemBase):
    pass


class ItemUpdate:
    title: str | None = None
    description: str | None = None
    price: float | None = None
    negotiable: bool | None = None
