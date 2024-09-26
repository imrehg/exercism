DNA_TO_RNA = str.maketrans("GCTA", "CGAU")


def to_rna(dna_strand: str) -> str:
    # This relies on the input being all upper case, and the expected output also being upper caseß
    # return dna_strand.replace("G", "c").replace("C", "g").replace("T", "a").replace("A", "u").upper()

    # From the Dig Deeper, this is much simpler, though still relies on casing
    return dna_strand.translate(DNA_TO_RNA)
