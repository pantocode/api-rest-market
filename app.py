from fastapi import FastAPI
from routes.item import product
from docs import tags_metadata

app= FastAPI(
    title="SuperMarket API",
    description="API que permite ver controlar el inventario de un supermercado.",
    version="0.0.1",
    openapi_tags=tags_metadata
    )

app.include_router(product)
