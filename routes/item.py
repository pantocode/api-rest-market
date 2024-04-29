from fastapi import APIRouter, Response
from config.db import conn
from schemas.item import productEntity,productsEntity
from models.item import Product
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

product = APIRouter()

@product.get('/products',response_model=list[Product],tags=['products'])
def find_all_products():
    return productsEntity(conn.local.product.find())


@product.post('/products',response_model=Product,tags=['products'])
def create_product(product: Product):
    new_product = dict(product)
    del new_product["id"]
    id = conn.local.product.insert_one(new_product).inserted_id
    product = conn.local.product.find_one({"_id":id})
    return productEntity(product)


@product.get('/products/{id}',response_model=Product,tags=['products'])
def find_product(id:str):
    return productEntity(conn.local.product.find_one({"_id":ObjectId(id)}))

@product.put('/products/{id}',response_model=Product,tags=['products'])
def update_product(id:str, product:Product):
    conn.local.product.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(product)})
    return productEntity(conn.local.product.find_one({"_id":ObjectId(id)}))

@product.delete('/products/{id}',status_code=HTTP_204_NO_CONTENT,tags=['products'])
def delete_product(id:str):
    productEntity(conn.local.product.find_one_and_delete({"_id":ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)


    


