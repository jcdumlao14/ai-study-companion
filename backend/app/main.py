from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, ai, leaderboard, user

app = FastAPI(title="AI Study Companion API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(ai.router, prefix="/ai", tags=["ai"])
app.include_router(leaderboard.router, prefix="/leaderboard", tags=["leaderboard"])
app.include_router(user.router, prefix="/user", tags=["user"])

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Study Companion API"}