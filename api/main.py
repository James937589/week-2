from fastapi import FastAPI 

app = FastAPI(
    title="FastAPI Example",
    description="This is an example of using FastAPI"
)

@app.get('/')
def default_route():
    """
    This is the default
    """
    return "You have reached default route, Back-end server is listening..."


@app.get("/example")
def get_example():
    """
    This endpoint return a JSON object consisting of a simple message.
    """
    return {"message": "Hello World!", "year":2025}