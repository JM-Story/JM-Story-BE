from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from post import router as post_router

app = FastAPI(root_path="/api")

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://jm-story.site"],  # Vite 프론트엔드 URL
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST, PUT, DELETE 등)
    allow_headers=["*"],  # 모든 헤더 허용
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Post 라우터 등록
app.include_router(post_router, prefix="/posts", tags=["posts"])

