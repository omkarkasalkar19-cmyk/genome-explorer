def translate(sequence):
  protein_sequence = ""
  genetic_code ={"ATG": "M" ,"GCT": "A","TTT": "F","GAA": "E"}
  for i in range(0, len(sequence), 3):
   codon = sequence[i:i+3]
   amino_acid = genetic_code.get(codon)
   protein_sequence += amino_acid
  return protein_sequence