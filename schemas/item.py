def productEntity(product)->dict:
    return {
        "id": str(product["_id"]),
        "productName": product["productName"],
        "category" :product["category"],
        "price": product["price"],
        "quantity": product["quantity"],
        "description": product["description"]
    }

def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]