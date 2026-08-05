from src.gc import calculate_gc ,calculate_at
from src.nucleotidegi import count_nucleotides


 
         
 

# -------------------------------------------------------------
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
    
#---------------------------------------------------
def transcribe(sequence):
    rna_sequence=""
    for nucleotide in sequence:
       if nucleotide == 'T':
          rna_sequence +='U'
       else:
          rna_sequence += nucleotide
    return rna_sequence    
    
# --------------------------------------------------
def translate(sequence):
  protein_sequence = ""
  genetic_code ={"ATG": "M" ,"GCT": "A","TTT": "F","GAA": "E"}
  for i in range(0, len(sequence), 3):
   codon = sequence[i:i+3]
   amino_acid = genetic_code.get(codon)
   protein_sequence += amino_acid
  return protein_sequence
#-------------------------------------------------
def detect_mutation(sequence1, sequence2):
  for i in range(len(sequence1)):
    if sequence1[i] != sequence2[i]:
     position = i+1
     original= sequence1[i]
     mutated= sequence2[i]
     mutated_type='substitution'
     return position,original,mutated,mutated_type
# ------------------------------------------------
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
#---------program-----------------------------------
sequence = "ATGGCTTTTGAA"
sequence1 = "ATGCGAT"
sequence2 = "ATGCAAT"
gc =calculate_gc(sequence)
print(f"GC Content: {gc:.2f}%")

at =calculate_at(sequence)
print(f"AT Content: {at:.2f}%") 

a,t,g,c=count_nucleotides(sequence)
print('A :',a)
print('T :',t)
print('G :',g)
print('C :',c) 

complement,reverse=reverse_complement(sequence)
print("Complement:", complement)
print("Reverse Complement:", reverse)

rna=transcribe(sequence)
print(f"RNA SEQUENCE :{rna}")

protein=translate(sequence)
print("protein :", protein)

position,original,mutated,mutated_type=detect_mutation(sequence1, sequence2)
print("\n----mutation found-----")
print("Position :",position )
print("Original :",original )
print("Mutated  :", mutated)
print("mutated_type : substitution")

orf=find_orf(sequence)
print("ORF :",orf)



   





