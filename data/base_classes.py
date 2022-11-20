from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref

Base = declarative_base()


class DnaBase(Base):
    __tablename__ = "dna_base"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(1))
    rna = relationship("RnaBase", backref=backref("rna_base", uselist=False))
    rna_id = Column(Integer, ForeignKey("rna_base.id"))

    def __str__(self):
        return f"{self.name}"


class RnaBase(Base):
    __tablename__ = "rna_base"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(1))

    # dna = relationship("DnaBase")
    # dna_id = Column(Integer, ForeignKey("dna_base.id"))

    def __str__(self):
        return f"{self.name}"


class AminoAcids(Base):
    __tablename__ = "amino_acids"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    short_name = Column(String(1))
    middle_name = Column(String(4))
    full_name = Column(String(30))

    def __str__(self):
        return f"{self.short_name}: {self.middle_name}, ({self.full_name})"


class Codons(Base):
    __tablename__ = "codons"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(3))
    amino_id = Column(Integer, ForeignKey("amino_acids.id"))
    amino = relationship("AminoAcids", backref="amino_codons")

    def __str__(self):
        return f'{self.name}'
