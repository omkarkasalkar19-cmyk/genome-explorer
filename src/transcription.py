def transcribe(sequence):
    rna_sequence=""
    for nucleotide in sequence:
       if nucleotide == 'T':
          rna_sequence +='U'
       else:
          rna_sequence += nucleotide
    return rna_sequence