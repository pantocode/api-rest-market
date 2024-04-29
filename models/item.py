from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: Optional[str]= None
    productName: str
    category: str
    price:float
    quantity:int
    description: str
