def read_fasta(file_name):
    sequence=""
    with open (file_name,'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                continue
            else:
                sequence += line
    return sequence            
