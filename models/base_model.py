from peewee import Model

from app_init import db


class BaseModel(Model):
    class Meta:
        database = db
