def protein_length(protein):
    len(protein)
    return len(protein)    

def amino_acid_count(protein):
    counts = {}

    for aa in protein:
        if aa in counts:
            counts[aa] += 1
        else:
            counts[aa] = 1

    return counts 

from src.amino_acid_weights import AMINO_ACID_WEIGHTS
def molecular_weight(protein):
    total_weight=0
    for aa in protein:
        total_weight += AMINO_ACID_WEIGHTS[aa]
    return total_weight