from fastapi import FastAPI

app = FastAPI()

@app.get("/orders")
def list_orders():
    return [{"order_id": 9001, "user_id": 1, "product_id": 101}]
