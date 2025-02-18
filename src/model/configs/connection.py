# aqui terá toda a classe para organizar a conexão com o banco
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "sqlite:///schema.db"
        self.__engine = self.__create_database_engine()
        self.session = None #começa a sessão zerada
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
# aqui você poderia usar o DBConnectionHandler para conectar ao banco

# abrindo uma sessão no banco de dados 
    def __enter__(self):
        session_make = sessionmaker(bind = self.__engine)
        self.session = session_make()

        return self #retornando todo o contexto da classe
        #para que detro do with, eu possa utilizar de todo o contexto da minha class

    def __exit__(self, exc_type, exc_value, exc_tb): #exc são exeptions
        self.session.close() #fechando a sessão ao sair do with