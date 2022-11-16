from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy.orm import sessionmaker

# engine = create_engine("sqlite:///my_base.db")
# session = sessionmaker(bind = engine)

Base = declarative_base()


class Dna_base(Base):
    __tablename__ = "dna_base"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(1))
    rna = relationship("Rna_base", backref=backref("rna_base", uselist=False))
    rna_id = Column(Integer, ForeignKey("rna_base.id"))

    def __str__(self):
        return f"{self.name}"


class Rna_base(Base):
    __tablename__ = "rna_base"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(1))

    # dna = relationship("Dna_base")
    # dna_id = Column(Integer, ForeignKey("dna_base.id"))

    def __str__(self):
        return f"{self.name}"


class Amino_acids(Base):
    __tablename__ = "amino_acids"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    short_name = Column(String(1))
    middle_name = Column(String(4))
    full_name = Column(String(30))

    # codon = relationship("Codons")
    # codon_id = Column(Integer, ForeignKey("codons.id"))
    # amino_codons = []

    def __str__(self):
        return f"{self.short_name}: {self.middle_name}, ({self.full_name})"


class Codons(Base):
    __tablename__ = "codons"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(3))
    amino_id = Column(Integer, ForeignKey("amino_acids.id"))
    amino = relationship("Amino_acids", backref="amino_codons")

    def __str__(self):
        return f'{self.name}'

