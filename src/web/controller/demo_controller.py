from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.responses import Response

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


@app.get("/image")
async def image():
    return FileResponse("misc/test-data/dice.png")


# Notice: For some reason Pycharm lights responses and response_class in the following annotation red, as if it was
# an error. But this code works LOL
@app.get("/imageBytes",
         responses={
             200: {
                 "content": {"image/png": {}},
             }
         },
         response_class=Response
         )
async def image_bytes():
    in_file = open("misc/test-data/dice.png", "rb")
    data = in_file.read()
    in_file.close()
    return Response(content=data, media_type="image/png")
