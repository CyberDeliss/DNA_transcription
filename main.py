from genetic_codes import *


def dict_reverse_from_list(_dict):
    """

    :param _dict: which has list like values
    :return: new_dict, where keys from _dict is value for each value from list (from _dict)
    for example {"stop": ["UGA", "UAA", "UAG"]} return {"UGA": "stop", "UAA": "stop", "UAG": "stop"}
    """
    new_dict = {}
    for key in _dict.keys():
        if type(_dict[key]) == list:
            for value in _dict[key]:
                new_dict[value] = key
        else:
            new_dict[_dict[key]] = key
    return new_dict


def dict_reverse_to_list(_dict):
    """
    for example {"UGA": "stop", "UAA": "stop", "UAG": "stop"} return {"stop": ["UGA", "UAA", "UAG"]}
    :param _dict:
    :return: new_dict:
    """
    new_dict = {}
    for key in _dict.keys():
        if new_dict.get(_dict[key]):
            new_dict[_dict[key]].append(key)
        else:
            new_dict[_dict[key]] = [key]
    return new_dict


def convert_dna_to_rna(dna_string):
    """
    convert DNA to RNA
    :param dna_string:
    :return: rna string
    """
    return dna_string.replace("T", "U")


def convert_rna_to_protein(rna_string, genetic_code):
    """

    :param rna_string: RNA like string
    :param genetic_code: dictionary, where keys are
    :return:
    """
    result_string = ""
    n = 3
    parts = [rna_string[i:i + n] for i in range(0, len(rna_string), n)]
    for _amino in parts:
        print(_amino)
        if genetic_code.get(_amino):
            result_string += genetic_code.get(_amino)
    return result_string

def look_for_met(_rna_string):
    pass


def change_amino_to_letters(_dict):
    new_dict = {}
    for key in _dict.keys():
        new_dict[key] = AMINO_LETTERS[_dict[key]]
    return new_dict


genetic_code = dict_reverse_from_list(GENETIC_CODE)
genetic_code = change_amino_to_letters(genetic_code)

my_result = []
for dna in DNA:
    temp_rna = convert_dna_to_rna(dna)
    my_result.append(convert_rna_to_protein(temp_rna, genetic_code))


print(my_result)
print(my_result == RESULT)
print(RESULT)
