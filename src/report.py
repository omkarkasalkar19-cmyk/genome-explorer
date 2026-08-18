def write_report(results):
    with open("results/report.txt","w")as file:
     file.write("=" * 50 + "\n")
     file.write("Genome Explorer Report\n")
     file.write("=" * 50 + "\n")
     for result in results:
                    file.write(f"Gene: {result['header']}\n")
                    file.write(f"Sequence: {result['sequence']}\n\n")
                    file.write(f"DNA Length: {result['dna_length']} bp\n")
                    file.write(f"GC content: {result['gc']:.2f}%\n")
                    file.write(f"AT content: {result['at']:.2f}%\n")
                    file.write(f"Protein: {result['protein']}\n")
                    file.write(f"Protein Length:{result['protein_length']}\n")
                    file.write(f"Molecular Weight:{result['weight']:.2f}Da\n")
                    file.write("Amino Acid Count:\n")
                    for aa, count in result["aa_counts"].items():
                       file.write(f"{aa}: {count}\n")
                    file.write(f"ORF: {result['orf']}\n")
                    file.write("Nucleotide Count:\n")
                    file.write(f"A: {result['a']}\n")
                    file.write(f"T: {result['t']}\n")
                    file.write(f"G: {result['g']}\n")
                    file.write(f"C: {result['c']}\n\n")
                    file.write("=" * 50 + "\n")

def write_comparison_report(header1, seq1, header2, seq2,
                            hamming, levenshtein_distance,
                            lcs_result, mutation_result):

    with open("results/comparison_report.txt", "w") as file:

        file.write("=" * 50 + "\n")
        file.write("Sequence Comparison Report\n")
        file.write("=" * 50 + "\n\n")

        file.write("Sequence 1\n")
        file.write("-" * 30 + "\n")
        file.write(f"Header: {header1}\n")
        file.write(f"Length: {len(seq1)} bp\n\n")

        file.write("Sequence 2\n")
        file.write("-" * 30 + "\n")
        file.write(f"Header: {header2}\n")
        file.write(f"Length: {len(seq2)} bp\n\n")

        file.write("Sequence Comparison\n")
        file.write("-" * 30 + "\n")
        file.write(f"Hamming Distance: {hamming}\n")
        file.write(f"Levenshtein Distance: {levenshtein_distance}\n")
        file.write(f"LCS: {lcs_result}\n")
        file.write(f"LCS Length: {len(lcs_result)}\n\n")

        file.write("Mutation Test\n")
        file.write("-" * 30 + "\n")

        if mutation_result:
            position, original, mutated, mutated_type = mutation_result
            file.write(f"Position: {position}\n")
            file.write(f"Original: {original}\n")
            file.write(f"Mutated: {mutated}\n")
            file.write(f"Type: {mutated_type}\n")
        else:
            file.write("No mutation detected\n")

        file.write("\n" + "=" * 50 + "\n")  


def write_alignment_report(result):

    with open("results/alignment_report.txt", "w") as file:

        file.write("===== Needleman-Wunsch Global Alignment =====\n\n")

        file.write(f"Sequence 1: {result['sequence1']}\n")
        file.write(f"Sequence 2: {result['sequence2']}\n\n")

        file.write(f"Alignment 1: {result['aligned_seq1']}\n")
        file.write(f"Alignment 2: {result['aligned_seq2']}\n")

        file.write(f"Alignment Score: {result['score']}\n")                          