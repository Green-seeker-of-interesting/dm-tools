from peewee import CharField, ForeignKeyField, TextField, DateField

from models.base_model import BaseModel


class GameSystem(BaseModel):
    name = CharField()


class Game(BaseModel):
    name = CharField()
    system = ForeignKeyField(GameSystem)


class GameItem(BaseModel):
    game = ForeignKeyField(Game)
    date = DateField()
    description = TextField()
