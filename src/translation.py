from src.codon_table import genetic_code
def translate(sequence):
  protein_sequence = ""
  genetic_code ={"ATG": "M" ,"GCT": "A","TTT": "F","GAA": "E"}
  for i in range(0, len(sequence), 3):
   codon = sequence[i:i+3]
  #  ingnore incomplete codon atthe end
   if len(codon)<3:
     break
   amino_acid = genetic_code.get(codon,"X")
   if amino_acid=="*":
      break
   protein_sequence += amino_acid
  return protein_sequence