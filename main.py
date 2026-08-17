from src.gc import calculate_gc ,calculate_at
from src.nucleotide import count_nucleotides
from src.reverse import reverse_complement
from src.transcription import transcribe
from src.translation import translate
from src.mutation import detect_mutation 
from src.orf_v3 import find_orf
from src.fasta import read_multiple_fasta
from src.report import write_report,write_comparison_report
from src.protein import protein_length
from src.protein import amino_acid_count
from src.protein import molecular_weight
from src.alignment import hamming_distance
from src.levenshtein import levenshtein
from src.lcs import lcs

sequences = read_multiple_fasta("data/insulin.fasta")
sequences2 = read_multiple_fasta("data/insulin_2.fasta")

header1, seq1 = sequences[0]
header2, seq2 = sequences2[0]

print("FASTA 1:", header1)
print("Length 1:", len(seq1))

print("FASTA 2:", header2)
print("Length 2:", len(seq2))


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

sequence1 = "ATGCGAT"
sequence2 = "ATGCAAT"
position,original,mutated,mutated_type=detect_mutation(sequence1, sequence2)
print("\n----mutation found-----")
print("Position :",position )
print("Original :",original )
print("Mutated  :", mutated)
print("mutated_type :",mutated_type)

print("\n----------FASTA comparison--------------")
if len(seq1) == len(seq2):
    hamming_result = hamming_distance(seq1, seq2)
else:
    hamming_result = "Not applicable-sequences have different lengths"

print("Hamming distance:", hamming_result)

lev_distance = levenshtein(seq1, seq2)
print("Levenshtein distance:", lev_distance) 
lcs_result = lcs(seq1, seq2)

print("LCS:", lcs_result)
print("LCS length:", len(lcs_result))

write_comparison_report(
    header1,
    seq1,
    header2,
    seq2,
    hamming_result,
    lev_distance,
    lcs_result,
    (position, original, mutated, mutated_type)
)
   





