from fastapi import FastAPI

app = FastAPI()
saved_text = "No data"


@app.get("/")
async def simple_json_response():
    return {"Hello": "World"}


@app.post("/save")
async def save(text: str):
    global saved_text
    saved_text = text
    return "Saved"


@app.get("/save")
async def retrieve():
    global saved_text
    return saved_text
