from logging.config import fileConfig

from sqlalchemy import create_engine, pool
from alembic import context

from db import SQLALCHEMY_DATABASE_URL
from schema import Base

# Alembic 설정 객체
config = context.config
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

# 로깅 설정
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# SQLAlchemy 모델의 metadata 연결
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Offline 모드에서 마이그레이션 실행"""
    context.configure(
        url=SQLALCHEMY_DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Online 모드에서 마이그레이션 실행"""
    engine = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=pool.NullPool)

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            transaction_per_migration=True,  # 여러 마이그레이션을 하나의 트랜잭션으로 실행
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()