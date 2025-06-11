from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def list_products():
    return [{"id": 101, "name": "Rocket Model"}, {"id": 102, "name": "Space Poster"}]
