from fastapi import FastAPI
from db.models import Base
from db.database import engine
from Routers import user
from Routers import project
from auth import authentication

Base.metadata.create_all(engine)
app=FastAPI()
app.include_router(project.router)
app.include_router(user.router)
app.include_router(authentication.router)

@app.get("/")
def HomePage():
    return {'message': 'Hello world!'}