from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, url: str):
        self.engine = create_engine(url, future=True)
        self.Session = sessionmaker(self.engine, future=True)

    def session(self):
        return self.Session()
