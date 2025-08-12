from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

# Get request
#fetch or read all the data
@app.get("/product")
async def all_products():
    return {"message": "Fetching all products"}

# fetch or read all single data
@app.get("/product/{product_id}")
async def single_product(product_id:int):
    return {"message": "Single product fetched", "Product_id": product_id}

# post request
# create of insert data


@app.post("/product")
async def create_product(new_product:dict):
    return {"message": "Product Created", "Product": new_product}
