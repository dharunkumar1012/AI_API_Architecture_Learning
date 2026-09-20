from fastapi import FastAPI, Query

app = FastAPI()

# Basic GET route  
@app.get("/")
def home():
    return {"Message": "Hello AI API"}

@app.get("/hello")
def hello():
    return {"message": "Hello DK"}

@app.get("/contact")
def contact():
    return {
        "contact" : "+91 984563123",
        "address" :  "chennai, india"
    }

# GET -> Path Parameters
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# GET -> Query Parameters
# @app.get("/users")
# def get_users(limit: int=10):
#     return {
#         "limit": limit
#     }

# Multiple Query parameter

@app.get("/users")
def get_users(limit: int = 10, active: bool = True):
    return{
        "limit": limit,
        "active": active
    }

@app.get("/products")
def get_products(category: str, limit: int):
    return{
        "category": category,
        "limit" : limit 
    }

@app.get("/search")
def get_search(query: str, limit: int=5):
    return{
        "query": query,
        "limit": limit
    }

# GET Query Parameters Constraints
@app.get("/tv")
def get_tv(category: str, limit: int = Query(5, ge=1, le=100)):
    return{
        "category" : "tv",
        "limit" : limit

    }