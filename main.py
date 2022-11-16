from data.genetic_codes import *
from data.base_classes import *
from utilities import *


genetic_code = dict_reverse_from_list(GENETIC_CODE)
print(genetic_code)
genetic_code = change_amino_to_letters(genetic_code, AMINO_LETTERS)
print(genetic_code)

my_result = []
for dna in DNA:
    temp_rna = convert_dna_to_rna(dna)
    my_result.append(convert_rna_to_protein(temp_rna, genetic_code))

#
# print(my_result)
# print(my_result == RESULT)
# print(RESULT)



