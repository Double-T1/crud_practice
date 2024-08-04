from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from orm.setting import db


class Product(db.Model):
    id = mapped_column(Integer, autoincrement=True, primary_key=True)
    title = mapped_column(String, nullable=False)
    description = mapped_column(String)
    price = mapped_column(Integer, nullable=False)
