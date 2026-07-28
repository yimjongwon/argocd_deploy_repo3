from fastapi import FastAPI

app = FastAPI()

@app.get("/fortune")
def get_fortune():
    return {
        "service": "fortune", 
        "message": "동쪽으로 가명 귀인을 만나요~"
    }