def find_orf(sequence):
    all_orfs= []
    for  frame in range(3):
        found_start = False
        current_orf=""
        for i in range(frame,len(sequence),3):
          codon = sequence[i:i+3]
          if codon == "ATG":
                 found_start = True
          if found_start:
                current_orf += codon
                if codon in ("TAA", "TAG", "TGA"):
                  all_orfs.append(current_orf)
                  current_orf=""
                  found_start=False
    if all_orfs:
        return max(all_orfs,key=len)        
    return ""