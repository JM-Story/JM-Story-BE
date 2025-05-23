# 1. Python 3.10 이미지 사용
FROM python:3.10

# 2. 작업 디렉토리 설정
# WORKDIR /app

# 3. 종속성 파일 복사 후 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 애플리케이션 코드 복사
COPY . .

# 5. GitHub Actions에서 환경 변수를 받아 `.env` 파일로 저장
# ARG DATABASE_URL
# RUN echo "DATABASE_URL=${DATABASE_URL}" > .env

# 6. 컨테이너에서 실행할 포트 설정
EXPOSE 8000

# 7. FastAPI 실행 명령
CMD alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000