from fastapi import FastAPI,status,Query
from typing import Annotated
from enum import Enum
app=FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

# Get request
#fetch or read all the data
# @app.get("/product")
# async def all_products():
#     return {"message": "Fetching all products"}

# # fetch or read all single data
# @app.get("/product/{product_id}")
# async def single_product(product_id:int):
#     return {"message": "Single product fetched", "Product_id": product_id}

# # post request
# # create of insert data
# @app.post("/product")
# async def create_product(new_product:dict):
#     return {"message": "Product Created", "Product": new_product}

# # put method
# # update complete data
# @app.put("/product/{product_id}")
# async def update_product(new_updated_product: dict,product_id:int):
#     return {"message": "Complete product updated","Product id":product_id, "new_updated_product": new_updated_product}


# # patch method
# # update partial data
# @app.patch("/product/{product_id}")
# async def partial_update_product(new_updated_product: dict, product_id: int):
#     return {"message": "Partial product updated", "Product id":product_id, "new_updated_product": new_updated_product}

# # delete method
# # delete data 
# @app.delete("/product/{product_id}")
# async def delete_product(product_id: int):
#     return {"message": "Product deleted", "Product id": product_id}


# Enum example
# class ProductCategory(str, Enum):
#     books = "books"
#     electronics = "electronics"
#     clothing = "clothing"

# # path parameter with predefined values using enum
# @app.get("/product/{category}")
# async def get_product_by_category(category: ProductCategory):
#     return {"message": "Products fetched by category", "Category": category.value}

# # path converter
# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"You requested file at ": file_path}


# Single Query parameter
# @app.get("/product") # product?category="book"
# async def product(category:str):
#     return {"status":"OK", "category": category}

# Multiple Query parameter
# @app.get("/product")  # product?category="book"
# async def product(category: str, price: float = 5): # default query parameter
#     return {"status": "OK", "category": category,"price": price}

# Optional Query parameter
# @app.get("/product")  # product?category="book"
# async def product(category: str, price: float | None=None):  # default query parameter
#     return {"status": "OK", "category": category, "price": price}

# # post request
# # create of insert data with status code
# @app.post("/product", status_code=status.HTTP_201_CREATED)
# async def create_product(new_product:dict):
#     return {"message": "Product Created", "Product": new_product}

#limit character in query parameter
#validation without anotated 
# @app.get("/product")
# async def product(search:str | None = Query(default=None, min_length=3, max_length=5)):
#     return {"status": "OK"}

# validation with anotated
 # new way to validate query parameter 
@app.get("/product")
async def product(search:Annotated[str | None, Query(min_length=3, max_length=5)] = None):
    return {"status": "OK"}
