from fastapi import APIRouter, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from category.models import Category, metadata

from category.models import get_async_session

# from models import Category

router_category = APIRouter(
    prefix="/category",
    tags=["Category"]
)

@router_category.get("/")
async def categories(session: AsyncSession = Depends(get_async_session),):
    categories = select(Category)
    select_all_results = await session.execute(categories)
    # categories = select(Category)
    # return select_all_results
    json_compatible_item_data = jsonable_encoder('{"test" => "test"}')
    return JSONResponse(content=json_compatible_item_data)


