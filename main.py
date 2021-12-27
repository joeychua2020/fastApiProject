from fastapi import FastAPI
from path import Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


inventory = {
    1: {"name": "milk",
        "price": 3.99,
        "brand": "regular"
        }
}

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory [item_id]

@app.get("/get-by-name")
def get_item(name: Optional[str]):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "not found"}


@app.post("/create-item/{item_id")
def create_item(item_id: int, item: UpdateItem):
    if item_id in inventory:
        return {"Error": "Item ID already exist"}
    inventory[item_id] = {"name": item.name, "brand": item.brand,"price": item.price}
    return inventory[item_id]

@app.put("/update-item/{item-id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        return {"Error": "ID doesn't exist"}
    inventory[item_id].update(item)
    return inventory[item_id]