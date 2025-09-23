from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def index():
    return {"message": "Hello, World!"}

@app.get("/blogs/{id}")
async def show(id: int):
    return {"message": f"Blog with id {id}"}

@app.get("/blogs/{id}/comments")
async def comments(id: int):
    return {"Blog_id": id, "comments": ["Great post!", "Very informative."] }