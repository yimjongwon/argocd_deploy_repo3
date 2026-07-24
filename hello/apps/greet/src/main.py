from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def get_fortune():
    return {
        "service": "greet", 
        "message": "hello"
    }