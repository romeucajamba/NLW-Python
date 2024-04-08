###### Conexão com Banco de Dados ###

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) -> None:
        self.connection_string = "{}:///{}".format(
            "sqlite",
            "storage.db"
        ) 
        self.__engine = None
        self.__session = None
    def connector_db(self) -> None:
        self.__engine = create_engine(self.connection_string)

    def get_egine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker()
        self.__session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()
        self.__engine.dispose()