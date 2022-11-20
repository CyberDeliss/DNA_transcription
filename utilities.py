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


def plot_gc_ratio(genom: str, step: int) -> None:
    """
    This function plots G-C ratio in a DNA molecule has

    The horizontal axis of this graph should be the genome position.
    The vertical axis should be the G-C ratio in the window

    Parameters:
        genom: string
            genomic data as a string
        step: int
            denoting a width of a bin with a default value of 100 characters.

    Returns:
        None

    Result:
        .png | .jpeg file.
        graph

    """
    pass
