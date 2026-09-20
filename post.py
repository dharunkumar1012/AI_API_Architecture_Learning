from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float = Field(gt=0)
    quantity: int = Field(ge=1, default=1)

@app.post("/products")
def create_product(product: Product):
    return{
        "name" : product.name,
        "price": product.price,
        "quantity": product.quantity
    }