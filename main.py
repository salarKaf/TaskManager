from fastapi import FastAPI
from db.models import Base
from db.database import engine
from Routers import user

Base.metadata.create_all(engine)
app=FastAPI()
app.include_router(user.router)

@app.get("/")
def HomePage():
    return {'message': 'Hello world!'}