from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import summarize

app = FastAPI()

# CORS Middleware for Frontend-Backend Communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(summarize.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to MeetAI API"}
