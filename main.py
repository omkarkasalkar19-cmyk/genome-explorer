from src.gc import calculate_gc ,calculate_at
from src.nucleotide import count_nucleotides
from src.reverse import reverse_complement
from src.transcription import transcribe
from src.translation import translate
         
 



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



   





