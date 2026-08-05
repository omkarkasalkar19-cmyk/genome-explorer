def find_orf(sequence):
  found_start = False
  orf = ""
  for i in range(0, len(sequence), 3):
    codon = sequence[i:i+3]
    if codon == "ATG":
        found_start = True
    if found_start:
       orf += codon
       if codon in ("TAA", "TAG", "TGA"):
         break  
  return orf