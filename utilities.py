def convert_dna_to_rna(dna_string: str) -> str:
    """
    replace T in DNA to U in RNA
    :param dna_string: dna as string
    :return: rna as string
    """
    return dna_string.replace("T", "U")


def convert_rna_to_protein(rna_string: str, genetic_code: dict) -> str:
    """
    :param rna_string: RNA as str
    :param genetic_code: dictionary, where keys are codons
    :return: protein as letters
    """
    result_string = ""
    n = 3
    parts = [rna_string[i:i + n] for i in range(0, len(rna_string), n)]
    for _amino in parts:
        print(_amino)
        if genetic_code.get(_amino):
            result_string += genetic_code.get(_amino)
    return result_string


def gc_content(g_selected: int, c_selected: int, len_selected: int) -> int:
    """
    :param g_selected: G is the number of G-bases in the selected region (it may be the whole molecule, or it's part)
    :param c_selected: C is the number of C-bases in the selected region
    :param len_selected:
    :return:
    """
    result = 0
    if len_selected > 0:
        result = (g_selected + c_selected) / len_selected * 100
    return int(result)


def plot_gc_ratio(genome: str, step: int) -> None:
    """
    This function plots G-C ratio in a DNA molecule has

    The horizontal axis of this graph should be the genome position.
    The vertical axis should be the G-C ratio in the window

    Parameters:
        genome: string
            genomic data as a string
        step: int
            denoting a width of a bin with a default value of 100 characters.

    Returns:
        None

    Result:
        .png | .jpeg file.
        graph
    """
    gc_ratio = []

    parts = [genome[i:i + step] for i in range(0, len(genome), step)]
    print(parts)
    for genome_selected in parts:
        count_g = 0
        count_c = 0
        for letter in genome_selected:
            if letter.title() == "G":
                count_g += 1
            if letter.title() == "C":
                count_c += 1
        gc_ratio.append(gc_content(count_g, count_c, len(genome_selected)))
    print(gc_ratio)




