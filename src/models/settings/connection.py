###### Conexão com Banco de Dados ###

from sqlalchemy import create_engine

class DBConnectionHandler:
    def __init__(self) -> None:
        self.connection_string = "{}:///{}".format(
            "sqlite",
            "storage.db"
        ) 
        self.__engine = None
    def connector_db(self) -> None:
        self.__engine = create_engine(self.connection_string)

    def get_egine(self):
        return self.__engine