"""Protein transcription from RNA sequences"""
from itertools import takewhile

# Known protein translations
PROTEINS = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP', # stop signal for translation
    'UAG': 'STOP', # stop signal for translation
    'UGA': 'STOP', # stop signal for translation
}
def proteins(strand):
    """Protein translation from RNA sequence

    Args:
        strand: string of RNA sequence

    Return:
        the list of proteins transscribed
    """
    return [p for p in takewhile(lambda x: x != 'STOP', [PROTEINS[strand[i:i+3]] for i in range(0, len(strand), 3)])]
