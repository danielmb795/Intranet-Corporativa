from fastapi import FastAPI

from database.engine  import Base, engine
from models import UserModel, TicketModel
from services.UserSevice import *


Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/init")
def root():
    return {"message": "teste"} 