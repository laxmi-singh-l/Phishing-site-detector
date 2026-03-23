from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def read_root():
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
