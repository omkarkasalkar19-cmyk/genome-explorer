def reverse_complement(sequence):
    complement = ""
    for nucleotide in sequence:
      if nucleotide == "A":
        complement += "T"
      elif nucleotide == "T":
        complement += "A"
      elif nucleotide == "G":
        complement += "C"
      elif nucleotide == "C":
        complement += "G"
    reverse_complement = complement[::-1] 
    return complement,reverse_complement