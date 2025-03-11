from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# MySQL 연결 설정
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:wjdalsdk0513@localhost:3306/jsdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DB 세션 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
