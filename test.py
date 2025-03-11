from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:wjdalsdk0513@localhost:3306/jsdb"

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    connection = engine.connect()
    print("✅ MySQL 연결 성공!")
    connection.close()
except Exception as e:
    print("❌ MySQL 연결 실패:", e)