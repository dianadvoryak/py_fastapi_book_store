from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from category.router import router_category

# from category.router import router_category

app = FastAPI(
    title="Book Store"
)

app.include_router(router_category)

@app.get("/")
def hello():
    json_compatible_item_data = jsonable_encoder("Hello World!")
    return JSONResponse(content=json_compatible_item_data)
    # return "Hello World!"