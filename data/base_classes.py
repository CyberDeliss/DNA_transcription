from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.future import select
from sqlalchemy.orm import relationship, backref
from data.db import Base, Session


class DnaBase(Base):
    __tablename__ = "dna_base"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(1))
    rna = relationship("RnaBase", backref=backref("dna", uselist=False))
    rna_id = Column(Integer, ForeignKey("rna_base.id"))

    def __str__(self):
        return f"{self.name}"


class RnaBase(Base):
    __tablename__ = "rna_base"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(1))

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


def convert_dna_letter_to_rna_letter(db: Session, dna_letter: str) -> RnaBase:
    """
    :param db: The session, which was opened
    :param dna_letter: one letter from DNA string

    :return: rna as RnaBase
    """
    rna_base = db.execute(select(RnaBase).join_from(DnaBase, RnaBase).filter(DnaBase.name == dna_letter)).scalar()
    return rna_base


def convert_codon_to_amino(db: Session, codon: str) -> AminoAcids:
    """
    :param db: The session, which was opened
    :param codon: one codon as str

    :return: amino as AminoAcids object
    """
    if len(codon) == 3:
        amino = db.execute(select(AminoAcids).join_from(Codons, AminoAcids).filter(Codons.name == codon)).scalar()
        return amino


def convert_dna_to_rna(db: Session, dna_string: str) -> str:
    if not dna_string:
        return "Your DNA string is empty"

    result_str = ""
    dna_string = dna_string.upper()

    if check_dna_string(dna_string):
        for dna in dna_string:
            result_str += convert_dna_letter_to_rna_letter(db, dna).name
        return result_str
    return "Your DNA string is wrong"


def get_codons(rna_string: str) -> list:
    n = 3
    return [rna_string[i:i + n].upper() for i in range(0, len(rna_string), n)]


def convert_rna_to_protein(db: Session, rna_string: str) -> str:
    """
    :param db: The session, which was opened
    :param rna_string: RNA as str
    :return: protein string
    """
    if not rna_string:
        return "Your RNA string is empty"

    result_string = ""
    rna_string = rna_string.upper()

    if check_rna_string(rna_string):
        codons = get_codons(rna_string)
        for codon in codons:
            if len(codon) == 3:
                result_string += convert_codon_to_amino(db, codon).short_name
        return result_string
    return f"Your RNA string is wrong"


def check_dna_string(dna_string: str) -> bool:
    condition = True
    for letter in set(dna_string):
        if not (letter in set("ACTG")):
            condition = False
            break
    return condition


def check_rna_string(rna_string: str) -> bool:
    condition = True
    for letter in set(rna_string):
        if not (letter in set("ACUG")):
            condition = False
            break
    return condition
