from app_init import create_tables, db
from gui.base_window import star_giu


def run():
    create_tables()
    star_giu()


def destroid():
    db.close()


if __name__ == "__main__":
    run()
    destroid()
