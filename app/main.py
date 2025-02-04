from fastapi import FastAPI, Request
from database import engine, Base
from records import router
from jinja_config import templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app.include_router(router=router)

@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request" : request, "name" : "theleshe"})