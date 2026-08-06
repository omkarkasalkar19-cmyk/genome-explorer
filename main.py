from src.gc import calculate_gc ,calculate_at
from src.nucleotide import count_nucleotides
from src.reverse import reverse_complement
from src.transcription import transcribe
from src.translation import translate
from src.mutation import detect_mutation 
from src.orf import find_orf
from src.fasta import read_fasta


 
sequence = read_fasta("data/sample.fasta")
print(sequence)
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



   





