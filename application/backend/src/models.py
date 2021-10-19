from src.database import Connection

class Model:

    def __init__(self) -> None:
        pass

    def fetch_one(self, sql: str, as_dict=False, *args):
        pass

    def fetch_all(self, sql: str, as_dict=False, *args):
        pass

    def execute_query(self, sql: str, *args) -> None:
        pass