from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/test")
def test():
    number = 10 / 0
    return {"result": number}

# Exception Handling
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={'msg' : 'Something went wrong'}
    )

# Custom exception
class ProductOutOfStock(Exception):
    pass

@app.get("/products")
def get_product():
    raise ProductOutOfStock()

@app.exception_handler(ProductOutOfStock)
async def product_out_of_stock(
    request: Request,
    exc: ProductOutOfStock
):
    return JSONResponse(status_code=500,content={'msg':'Product out of stock nanbaa.'}
    )