"""
Main function of API

@author Anthony Epps
"""
from fastapi import FastAPI
import model
from config import engine
import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def index():
    return "API Running"

app.include_router(router.router,prefix="/student",tags=["student"])