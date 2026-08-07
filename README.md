# 🧬 Genome Explorer v1.0

Genome Explorer is a Python-based bioinformatics toolkit developed to perform fundamental DNA and protein sequence analysis from FASTA files. It provides commonly used bioinformatics analyses through a modular Python project.

---

## 📌 Features

### 🧬 DNA Analysis

- Read FASTA and Multi-FASTA files
- Calculate DNA sequence length
- Calculate GC Content
- Calculate AT Content
- Count nucleotides (A, T, G, C)
- Generate Reverse Complement
- Transcribe DNA into RNA

### 🧪 Protein Analysis

- Translate DNA into Protein
- Calculate Protein Length
- Calculate Protein Molecular Weight
- Count Amino Acid Composition

### 🧬 Gene Analysis

- Open Reading Frame (ORF) Detection
- Mutation Detection

### 📄 Report Generation

Automatically generates a detailed report containing:

- Gene Information
- DNA Sequence
- DNA Length
- GC Content
- AT Content
- Protein Sequence
- Protein Length
- Molecular Weight
- Amino Acid Count
- ORF
- Nucleotide Count


---

# 📂 Project Structure

```text
Genome-Explorer/
│
├── data/
│   └── insulin.fasta
│
├── results/
│   └── report.txt
│
├── src/
│   ├── fasta.py
│   ├── gc.py
│   ├── nucleotide.py
│   ├── reverse.py
│   ├── transcription.py
│   ├── translation.py
│   ├── codon_table.py
│   ├── amino_acid_weights.py
│   ├── mutation.py
│   ├── orf_v3.py
│   ├── protein.py
│   └── report.py
│
├── main.py
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/omkarkasalkar19-cmyk/genome-explorer.git
```

Move into the project directory

```bash
cd genome-explorer
```

Run the program

```bash
python main.py
```

---

# 📊 Example Output

The program generates a report similar to:

```text
Gene: Homo sapiens insulin

DNA Length: 495 bp
GC Content: 60.00%
AT Content: 40.00%

Protein Length: 45 aa
Molecular Weight: 5616.17 Da

ORF Found

Nucleotide Count
A:121
T:77
G:140
C:157
```

---

# 🛠 Technologies Used

- Python
- FASTA File Parsing
- Dictionaries
- File Handling
- Modular Programming
- Basic Bioinformatics Algorithms

---

# 📖 Concepts Implemented

- FASTA Parsing
- DNA Sequence Analysis
- GC & AT Content
- Reverse Complement
- Transcription
- Translation
- Codon Table
- ORF Detection
- Mutation Detection
- Protein Analysis
- Report Generation

---

# 🔮 Future Improvements

- Compare mutations between two FASTA sequences
- Detect insertions and deletions (indels)
- SNP analysis
- Mutation summary report
- Pairwise Sequence Alignment
- Needleman-Wunsch Algorithm
- Smith-Waterman Algorithm
- BLAST Integration
- Motif Finding
- Restriction Enzyme Analysis
- GenBank File Support
- Sequence Visualization

---

# 👨‍💻 Author

**Omkar Kasalkar**

M.Sc. Bioinformatics Student

---

# ⭐ Acknowledgements

This project was built as a learning project to understand fundamental bioinformatics algorithms and improve Python programming skills.
