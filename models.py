from sqlalchemy import Column, Integer, String, CheckConstraint
from db import Base

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    autor = Column(String(100), nullable=False)
    genero = Column(String(50), nullable=False)
    estado = Column(String(20), nullable=False)

    __table_args__ = (
        CheckConstraint("estado IN ('leído', 'no leído')", name="estado_valido"),
    )

    def __repr__(self):
        return f"<Libro(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', genero='{self.genero}', estado='{self.estado}')>"
