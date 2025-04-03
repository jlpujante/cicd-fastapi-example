from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/")
async def root():
    ts = time.time()
    return dict(
        msg="Hello World",
        ts=ts
    )