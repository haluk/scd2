import pathlib

current_file = pathlib.Path(__file__)
db_file = current_file.parents[1] / "database.db"

db_url = f"sqlite+pysqlite:///{db_file}"
