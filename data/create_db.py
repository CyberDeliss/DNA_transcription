from data.genetic_codes import GENETIC_CODE_MIDDLE, AMINO_FULL_NAME
from data.base_classes import DnaBase, RnaBase, AminoAcids, Codons
from data.db import Base, engine, Session


def create_dna_list() -> list:
    dna_objects = []
    temp_id = 0
    for letter in "ACGT":
        temp_id += 1
        dna_objects.append(DnaBase(id=temp_id, name=letter))
    return dna_objects


def create_rna_list() -> list:
    temp_id = 0
    rna_objects = []
    for letter in "ACGU":
        temp_id += 1
        rna_objects.append(RnaBase(id=temp_id, name=letter))
    return rna_objects


def create_aminos_list() -> list:
    temp_id = 0
    aminos_objects = []
    for key in list(AMINO_FULL_NAME.keys()):
        temp_id += 1
        aminos_objects.append(
            AminoAcids(
                id=temp_id,
                short_name=key.capitalize(),
                middle_name=AMINO_FULL_NAME.get(key)[0].capitalize(),
                full_name=AMINO_FULL_NAME.get(key)[1].title()
            )
        )
    return aminos_objects


def create_codons() -> list:
    letters = "UCAG"
    temp_id = 0
    codons_objects = []
    for x in letters:
        for y in letters:
            for z in letters:
                temp_id += 1
                codons_objects.append(Codons(id=temp_id, name=f"{x}{y}{z}"))
    return codons_objects


def connect_dna_and_rna() -> tuple:
    dna_objects = create_dna_list()
    rna_objects = create_rna_list()

    for dna in dna_objects:
        for rna in rna_objects:
            if str(dna.name) == str(rna.name):
                dna.rna = rna
                dna.rna_id = rna.id
                break
            elif str(dna.name) == "T":
                if str(rna.name) == "U":
                    dna.rna = rna
                    dna.rna_id = rna.id
                    break
    return dna_objects, rna_objects


def connect_codons_and_aminos() -> tuple:
    codons_objects = create_codons()
    aminos_objects = create_aminos_list()

    for one_codon in codons_objects:
        for one_amino in aminos_objects:
            if GENETIC_CODE_MIDDLE[str(one_codon.name)].capitalize() == str(one_amino.middle_name):
                one_amino.amino_codons.append(one_codon)
                one_amino.codon_id = one_codon.id
    return codons_objects, aminos_objects


def create_db() -> tuple:
    dna_bases, rna_bases = connect_dna_and_rna()
    codons, aminos = connect_codons_and_aminos()
    return dna_bases, rna_bases, codons, aminos


def filling_base():
    dna_bases, rna_bases, codons, aminos = create_db()
    Base.metadata.create_all(engine)
    with Session() as session:
        for dna_base in dna_bases:
            session.add(dna_base)

        for rna_base in rna_bases:
            session.add(rna_base)

        for amino in aminos:
            session.add(amino)

        for codon in codons:
            session.add(codon)
        session.commit()
