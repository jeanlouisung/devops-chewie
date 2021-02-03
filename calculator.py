import uvicorn as uvicorn
from fastapi import FastAPI


def add(nb1: int, nb2: int):
    if type(nb1) != int or type(nb2) != int:
        raise TypeError(f"Arguments should be int")
    return nb1 + nb2


app = FastAPI()


@app.get("/add/")
def add_nb(nb1: int, nb2: int):
    return {'result': add(nb1, nb2)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
