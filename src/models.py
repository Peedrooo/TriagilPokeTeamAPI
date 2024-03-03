from sqlalchemy import VARCHAR, Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

from database import Base


# Tabela de associação entre Trainer e Pokemon
trainer_pokemon_association = Table(
    "trainer_pokemon_association",
    Base.metadata,
    Column("trainer_id", Integer, ForeignKey("TRAINER.id")),
    Column("pokemon_id", Integer, ForeignKey("POKEMON.id"))
)

class Trainer(Base):
    __tablename__ = "TRAINER"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(VARCHAR(255), unique=True, index=True)
    pokemons = relationship("Pokemon", secondary=trainer_pokemon_association, back_populates="trainers")

class Pokemon(Base):
    __tablename__ = "POKEMON"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(255), unique=True, index=True)
    weight = Column(Integer)
    height = Column(Integer)
    trainers = relationship("Trainer", secondary=trainer_pokemon_association, back_populates="pokemons")
