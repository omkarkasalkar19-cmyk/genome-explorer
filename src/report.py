def write_report(results):
    with open("results/report.txt","w")as file:
     file.write("=" * 50 + "\n")
     file.write("Genome Explorer Report\n")
     file.write("=" * 50 + "\n")
     for result in results:
        file.write(f"Gene: {result['header']}\n")
        file.write(f"Sequence: {result['sequence']}\n\n")
        file.write(f"Length: {result['length']} bp\n")
        file.write(f"GC content: {result['gc']:.2f}%\n")
        file.write(f"AT content: {result['at']:.2f}%\n")
        file.write(f"Protein: {result['protein']}\n")
        file.write(f"ORF: {result['orf']}\n")
        file.write("Nucleotide Count:\n")
        file.write(f"A: {result['a']}\n")
        file.write(f"T: {result['t']}\n")
        file.write(f"G: {result['g']}\n")
        file.write(f"C: {result['c']}\n\n")
        file.write("=" * 50 + "\n")