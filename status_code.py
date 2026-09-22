from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserRequest(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    name: str
    email: str

class ProductRequest(BaseModel):
    name: str
    quantity: int

# Status code - 201
@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserRequest):
    return user

# Status code - 400
@app.post("/products")
def create_product(product: ProductRequest):
    if product.quantity > 10:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail="Quantity can't be greater than 10"
        )
    return product