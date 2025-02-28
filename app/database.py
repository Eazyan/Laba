from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Подключение к базе данных (например, PostgreSQL)
DATABASE_URL = "postgresql://user_test:password@localhost/laba"

# Создаем движок для синхронного подключения
engine = create_engine(DATABASE_URL, echo=True)

# Синхронная сессия
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()

# Мета-данные
metadata = MetaData()

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
