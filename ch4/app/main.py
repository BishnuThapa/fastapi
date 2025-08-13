from fastapi import FastAPI,status,Query,Body
from pydantic import BaseModel, Field

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
# @app.get("/product")
# async def product(search:Annotated[str | None, Query(min_length=3, max_length=5)] = None):
#     return {"status": "OK"}


#create and insert data and validata using pydantic model
#define a pydantic model
class Product(BaseModel):
    id:int
    name: str
    price: float
    stock:int | None = None  # Optional field
    
# @app.post("/product", status_code=status.HTTP_201_CREATED)
# async def create_product(new_product: Product): #new product type of Product that is defined above
#     return new_product


# @app.post("/product", status_code=status.HTTP_201_CREATED)
# # access attributes of Product model inside function
# async def create_product(new_product: Product):
#     print(new_product.id)
#     print(new_product.name)
#     print(new_product.price)
#     print(new_product.stock)
#     return new_product


# @app.post("/product", status_code=status.HTTP_201_CREATED)
# add new calculated field to Product model
# async def create_product(new_product: Product):
#     product_dict=new_product.model_dump()  # Convert Pydantic model to dictionary
#     price_with_tax=new_product.price + (new_product.price*18/100)  # Calculate price with tax
#     product_dict.update({"price_with_tax": price_with_tax})  # Add new field to dictionary
#     return product_dict

#combining request body with path parameter
# @app.put("/product/{product_id}", status_code=status.HTTP_200_OK)
# async def update_product(product_id: int, new_updated_product: Product):
#     return {"product_id": product_id, "updated_product": new_updated_product}

#adding query parameter with request body
# @app.put("/product/{product_id}", status_code=status.HTTP_200_OK)
# async def update_product(
#     product_id: int, 
#     new_updated_product: Product, 
#     discount: float | None = Query(default=None, ge=0, le=100)  # Query parameter with validation
# ):
#     return {
#         "product_id": product_id, 
#         "updated_product": new_updated_product, 
#         "discount": discount
#     }

# MUltiple body parameters
# class Product(BaseModel):
#     name:str
#     price:float
#     stock:int | None=None

# class Seller(BaseModel):
#     name:str
#     full_name:str

# @app.post("/product", status_code=status.HTTP_201_CREATED)
# async def create_product(product:Product,seller:Seller):
#     return {
#         "product": product,
#         "seller": seller
#     }

#make body optional
# @app.post("/product", status_code=status.HTTP_201_CREATED)
# async def create_product(product: Product, seller: Seller | None = None):
#     return {
#         "product": product,
#         "seller": seller
#     }


#singular value in body
# @app.post("/product", status_code=status.HTTP_201_CREATED)
# async def create_product(product: Product, seller: Seller,sec_key:Annotated[str,Body()]):
#     return {
#         "product": product,
#         "seller": seller,
#         "sec_key": sec_key
#     }

# with embed-> difference shown in reponses of swagger
# @app.post("/product", status_code=status.HTTP_201_CREATED)
# async def create_product(product: Annotated[Product,Body(embed=True)]):
#     return {
#         "product": product,
        
#         # output: {
#         #     "product": { # this as a key is added because of embed=True
#         #         "name": "string",
#         #         "price": 0,
#         #         "stock": 0
#         #     }
#         # }
#     }



#Pydantic Fields, validation
class Product(BaseModel):
    name:str=Field(
        min_length=3, 
        max_length=10, 
        title="Product Name", 
        description="Name of the product"
        )
    price:float=Field(
        gt=0, 
        le=10000, 
        title="Product Price", 
        description="Price of the product"
        )
    stock:int | None=Field(
        default=None,
        ge=0, 
        le=1000,
        title="Product Stock",
        description="Stock of the product"
        )
@app.post("/product", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    return {
        "product": product,
    }
