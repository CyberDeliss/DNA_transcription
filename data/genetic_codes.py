LETTERS = "UCAG"
codons = [f"{x}{y}{z}" for x in LETTERS for y in LETTERS for z in LETTERS]

GENETIC_CODE = {
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
    "ile": ["AUU", "AUC", "AUA"],
    "pro": ["CCU", "CCC", "CCA", "CCG"],
    "phe": ["UUU", "UUC"],
    "ser": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
    "tyr": ["UAU", "UAC"],
    "thr": ["ACU", "ACC", "ACA", "ACG"],
    "trp": ["UGG"],
    "val": ["GUU", "GUC", "GUA", "GUG"],
}

amino = ["stop", "met", "ala",
         "arg", "asn", "asp", "cys",
         "glu", "gln", "gly",
         "his", "leu", "lys", "lle",
         "pro", "phe", "ser", "tyr",
         "thr", "trp", "val"]


AMINO_LETTERS = {
    "ala": "A",
    "cys": "C",
    "asp": "D",
    "glu": "E",
    "phe": "F",
    "gly": "G",
    "his": "H",
    "ile": "I",
    "lys": "K",
    "leu": "L",
    "met": "M",
    "asn": "N",
    "pro": "P",
    "gln": "Q",
    "arg": "R",
    "ser": "S",
    "thr": "T",
    "val": "V",
    "trp": "W",
    "tyr": "Y",
    "stop": "."}

unused_letters = "BJOUXZ"

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

RESULT = ["IWLLTI",
          "VVMAYI",
          "QVVLFS",
          "AN.",
          "AN.HLWHC",
          "YEKLK",
          "PVLDWLEEKF"]
