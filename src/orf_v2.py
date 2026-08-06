def find_orf(sequence):
    longest_orf="" 
    for frame in range(3):
        found_start = False
        current_orf=""
        for i in range(frame,len(sequence),3):
          codon = sequence[i:i+3]
          if codon == "ATG":
                 found_start = True
          if found_start:
                current_orf += codon
                if codon in ("TAA", "TAG", "TGA"):
                 if len(current_orf)>len(longest_orf):
                  longest_orf=current_orf
                  break
    return longest_orf        