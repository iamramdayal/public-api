from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from routers import links

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://links.ramdhayal.com/",
    "https://links-ramdhayal-com.web.app/",
    "https://links-ramdhayal-com.firebaseapp.com/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(links.router)

@app.get("/")
def root():
    return {"Visit": "https://www.ramdhayal.com"}