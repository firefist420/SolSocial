from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routes import auth_router, posts_router, tokens_router, users_router, feeds_router

app = FastAPI(title="SolSocial API", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(posts_router)
app.include_router(tokens_router)
app.include_router(feeds_router)

@app.get("/")
async def root():
    return {"message": "SolSocial API"}