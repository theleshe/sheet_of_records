from fastapi import FastAPI
from database import engine, Base
from records import router

app = FastAPI()

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app.include_router(router=router)