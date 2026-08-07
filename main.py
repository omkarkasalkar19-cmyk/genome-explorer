from src.gc import calculate_gc ,calculate_at
from src.nucleotide import count_nucleotides
from src.reverse import reverse_complement
from src.transcription import transcribe
from src.translation import translate
from src.mutation import detect_mutation 
from src.orf_v3 import find_orf
from src.fasta import read_multiple_fasta
from src.report import write_report
from src.protein import protein_length
from src.protein import amino_acid_count
from src.protein import molecular_weight

sequences = read_multiple_fasta("data/insulin.fasta")
sequence1 = "ATGCGAT"
sequence2 = "ATGCAAT"
results = []
for header, sequence in sequences:
    print("=" * 40)
    print("Gene :", header)
    print("=" * 40)

    print("Sequence :", sequence)

    dna_length = len(sequence)
    print(f"DNA Length: {dna_length} bp")

    gc =calculate_gc(sequence)
    print(f"GC Content: {gc:.2f}%")

    at =calculate_at(sequence)
    print(f"AT Content: {at:.2f}%") 

    a,t,g,c=count_nucleotides(sequence)
    print('A :',a)
    print('T :',t)
    print('G :',g)
    print('C :',c) 

    complement, reverse = reverse_complement(sequence)
    print("Complement:", complement)
    print("Reverse Complement:", reverse)
 
    rna=transcribe(sequence)
    print(f"RNA SEQUENCE :{rna}")

    protein=translate(sequence)
    print("protein :", protein)

    weight = molecular_weight(protein)
    print(f"Molecular Weight: {weight:.2f} Da")

    aa_counts = amino_acid_count(protein)
    print("Amino Acid Count:")
    for aa, count in aa_counts.items():
      print(f"{aa}: {count}")

    protein_len = protein_length(protein)
    print("protein length :",protein_len)


    orf=find_orf(sequence)
    print("ORF :",orf)

    result = {
    "header": header,
    "sequence": sequence,
    "dna_length":dna_length,
    "gc": gc,
    "at": at,
    "protein": protein,
    "protein_length":protein_len,
    "weight": weight,
    "aa_counts":aa_counts,
    
    "orf": orf,

    "a": a,
    "t": t,
    "g": g,
    "c": c
}
    results.append(result)
write_report(results)    

position,original,mutated,mutated_type=detect_mutation(sequence1, sequence2)
print("\n----mutation found-----")
print("Position :",position )
print("Original :",original )
print("Mutated  :", mutated)
print("mutated_type : substitution")



   





