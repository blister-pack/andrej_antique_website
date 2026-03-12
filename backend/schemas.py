from sqlmodel import SQLModel, Field


class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(default="Item name", index=True)
    description: str | None = Field(default=None)
    price: float = Field(default=0.0, index=True)
    negotiable: bool = Field(default=False)
    # ID is optional in Python so that the DB itself generates it
    # TODO complete w relevant categories - {date_created};
