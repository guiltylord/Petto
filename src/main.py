from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.exceptions import ValidationException
from src.html import html

app = FastAPI(
    title="Petto"
)

fake_users = {
    1 : "Bob"
}
@app.get("/")
def get_hello():
    return (HTMLResponse(html))

@app.get("/users/{user_id}")
def get_user(user_id):
    return fake_users.get("1")

@app.post("/users/{user_id}")
def change_name(user_id: int, new_name):
    fake_users[user_id] =  new_name
    return fake_users.get(user_id)

