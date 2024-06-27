
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine=create_engine("sqlite:///TaskManager.db" , connect_args={"check_same_thread": False})
Base = declarative_base()

sessionLocal=sessionmaker(bind=engine , autoflush=False , autocommit=False)

def get_db():
    session=sessionLocal()
    try:
        yield session
    finally:
        session.close()