from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def list_users():
    return [{"id": 1, "name": "Aparna"}, {"id": 2, "name": "Dev"}]
