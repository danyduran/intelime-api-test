from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def index():
    return "Hola mundo"