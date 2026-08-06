from src.codon_table import genetic_code
def translate(sequence):
  protein = ""
  for i in range(0, len(sequence), 3):
   codon = sequence[i:i+3]
  #  ingnore incomplete codon atthe end
   if len(codon) !=3:
     break
   amino_acid = genetic_code.get(codon,"X")
   if amino_acid=="*":
      break
   protein += amino_acid
  return protein