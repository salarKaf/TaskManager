from fastapi import FastAPI
from db.models import Base
from db.database import engine
from Routers import user
from Routers import project
from Routers import task
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware



Base.metadata.create_all(engine)
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(project.router)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(task.router)
@app.get("/")
def HomePage():
    return {'message': 'Hello world!'}