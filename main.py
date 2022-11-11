
def dict_revers(_dict):
    new_dict = {}
    for key in _dict.keys():
        for value in _dict[key]:
            new_dict[value] = key
    return new_dict


def convert_dna_to_rna(dna_string):
    return dna_string.replace("T", "U")


def convert_rna_to_protein():
    pass


def look_for_met(_rna_string):
    pass


LETTERS = "UCAG"
codons = [f"{x}{y}{z}" for x in LETTERS for y in LETTERS for z in LETTERS]
print(codons)

genetic_code = {
    "stop": ["UGA", "UAA", "UAG"],
    "met": ["AUG"],
    "ala": ["GCU", "GCC", "GCA", "GCG"],
    "arg": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "asn": ["AAU", "AAC"],
    "asp": ["GAU", "GAC"],
    "cys": ["UGU", "UGC"],
    "glu": ["GAA", "GAG"],
    "gln": ["CAA", "CAG"],
    "gly": ["GGU", "GGC", "GGA", "GGG"],
    "his": ["CAU", "CAC"],
    "leu": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
    "lys": ["AAA", "AAG"],
    "lle": ["AUU", "AUC", "AUA"],
    "pro": ["CCU", "CCC", "CCA", "CCG"],
    "phe": ["UUU", "UUC"],
    "ser": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
    "tyr": ["UAU", "UAC"],
    "thr": ["ACU", "ACC", "ACA", "ACG"],
    "trp": ["UGG"],
    "val": ["GUU", "GUC", "GUA", "GUG"],
}

genetic_code = dict_revers(genetic_code)
print(genetic_code)
print("\n")

print(sorted(list(genetic_code.keys())) == sorted(codons))
amino = ["stop", "met", "ala",
         "arg", "asn", "asp", "cys",
         "glu", "gln", "gly",
         "his", "leu", "lys", "lle",
         "pro", "phe", "ser", "tyr",
         "thr", "trp", "val"]
print(amino)




RNA = ["AUUUGGCUACUAACAAUCUA",
       "GUUGUAAUGGCCUACAUUA",
       "CAGGUGGUGUUGUUCAGUU",
       "GCUAACUAAC",
       "GCUAACUAACAUCUUUGGCACUGUU",
       "UAUGAAAAACUCAAA",
       "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU"]

DNA = ["ATTTGGCTACTAACAATCTA",
       "GTTGTAATGGCCTACATTA",
       "CAGGTGGTGTTGTTCAGTT",
       "GCTAACTAAC",
       "GCTAACTAACATCTTTGGCACTGTT",
       "TATGAAAAACTCAAA",
       "CCCGTCCTTGATTGGCTTGAAGAGAAGTTT"]

result = ["IWLLTI",
          "VVMAYI",
          "QVVLFS",
          "AN.",
          "HLWHC",
          "PVLDWLEEKF"]

for dna in DNA:
    print(convert_dna_to_rna(dna))