from fastapi import FastAPI
from post import router as post_router

app = FastAPI(root_path="/api")

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Post 라우터 등록
app.include_router(post_router, prefix="/posts", tags=["posts"])

