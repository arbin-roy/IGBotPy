from typing import Optional

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root(req: Request):
    return {"Hello": "Beautiful World", "req": req.query_params['hub.challenge']}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/webhook")
def webhook(req: Request):
    print(req.query_params)
    return int(req.query_params['hub.challenge'])