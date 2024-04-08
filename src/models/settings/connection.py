###### Conexão com Banco de Dados ###

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class __DBConnectionHandler:
    def __init__(self) -> None:
        self.connection_string = "{}:///{}".format(
            "sqlite",
            "storage.db"
        ) 
        self.__engine = None
        self.session = None
    def connector_db(self) -> None:
        self.__engine = create_engine(self.connection_string)

    def get_egine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

db_connection_handler = __DBConnectionHandler()