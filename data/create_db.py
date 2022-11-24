from data.genetic_codes import GENETIC_CODE_MIDDLE, AMINO_FULL_NAME
from data.base_classes import DnaBase, RnaBase, AminoAcids, Codons
from data.db import Base, engine, Session

dna_bases = []
temp_id = 0
for letter in "ACGT":
    temp_id += 1
    dna_bases.append(DnaBase(id=temp_id, name=letter))

temp_id = 0
rna_bases = []
for letter in "ACGU":
    temp_id += 1
    rna_bases.append(RnaBase(id=temp_id, name=letter))

temp_id = 0
aminos = []
for key in list(AMINO_FULL_NAME.keys()):
    temp_id += 1
    aminos.append(
        AminoAcids(
            id=temp_id,
            short_name=key.capitalize(),
            middle_name=AMINO_FULL_NAME.get(key)[0].capitalize(),
            full_name=AMINO_FULL_NAME.get(key)[1].title()
        )
    )

for dna in dna_bases:
    for rna in rna_bases:
        if str(dna.name) == str(rna.name):
            dna.rna = rna
            dna.rna_id = rna.id
            break
        elif str(dna.name) == "T":
            if str(rna.name) == "U":
                dna.rna = rna
                dna.rna_id = rna.id
                break

LETTERS = "UCAG"

temp_id = 0
codons = []
for x in LETTERS:
    for y in LETTERS:
        for z in LETTERS:
            temp_id += 1
            codons.append(Codons(id=temp_id, name=f"{x}{y}{z}"))

for codon in codons:
    for amino in aminos:
        if GENETIC_CODE_MIDDLE[str(codon.name)].capitalize() == str(amino.middle_name):
            amino.amino_codons.append(codon)
            amino.codon_id = codon.id


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
