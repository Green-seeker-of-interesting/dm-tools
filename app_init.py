from peewee import SqliteDatabase

import setting

db = SqliteDatabase(setting.DB_NAMES)


def create_tables():
    from models.games_model import Game, GameItem, GameSystem

    with db:
        db.create_tables(
            [
                GameSystem,
                Game,
                GameItem,
            ]
        )
