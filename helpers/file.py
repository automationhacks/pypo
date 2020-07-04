from config.base import DB_PATH


def create_base_db():
    template = """{"logs": []}"""
    with open(DB_PATH, "w+") as f:
        f.write(template)