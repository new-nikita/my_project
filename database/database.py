from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, sessionmaker

from datetime import datetime

Base = declarative_base()


class User(Base):
    """
    Создание таблицы запроса истории команд пользователя
    """
    __tablename__ = 'users_requests'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # id пользователя
    user_name: Mapped[str] = mapped_column(String, nullable=False)  # Имя пользователя
    date: Mapped[str] = mapped_column(String)  # Команды пользователя
    date_of_registration: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())  # Дата регистрации пользователя


DATABASE_URL = 'sqlite:///users_requests.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def initialize_db():
    Base.metadata.create_all(engine)
