from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class UserRequest(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    name: str
    email: str

@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserRequest):
    return user