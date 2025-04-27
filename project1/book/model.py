from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.mysql as mysql
import uuid
from datetime import datetime

class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: uuid.UUID = Field(
        sa_column=Column(
            mysql.BINARY(16),  # MySQL does not have a native UUID type, so we use BINARY(16)
            primary_key=True,
            unique=True,
            nullable=False
        )
    )

    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    created_at: datetime = Field(sa_column=Column(mysql.DATETIME, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(mysql.DATETIME, default=datetime.now, onupdate=datetime.now))

    def __repr__(self) -> str:
        return f"<Book {self.title}>"