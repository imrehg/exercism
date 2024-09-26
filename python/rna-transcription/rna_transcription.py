def to_rna(dna_strand: str) -> str:
    # This relies on the input being all upper case, and the expected output also being upper caseß
    return dna_strand.replace("G", "c").replace("C", "g").replace("T", "a").replace("A", "u").upper()
