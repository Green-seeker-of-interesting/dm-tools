from app_init import create_tables, db


def run():
    create_tables()


def destroid():
    db.close()


if __name__ == "__main__":
    run()
    destroid()
