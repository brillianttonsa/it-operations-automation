from fastapi import FastAPI

# Instantiate the application instance
app = FastAPI()

# Define a root GET endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI with Uvicorn!"}

