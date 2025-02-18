from src.model.configs.base import Base

from sqlalchemy import Column, String, Integer, ForeignKey

class Inscritos(Base):
    __tablename__ = 'Inscritos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    evento_id = Column(Integer,ForeignKey("Eventos.id")) # join on é literalmente essa linha
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    link = Column(String, nullable=True) #Nn precisa colocar nullable True, mas coloquei para fixação