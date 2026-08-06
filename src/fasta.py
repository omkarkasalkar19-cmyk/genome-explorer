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

#------multi fasta parser------------
def read_multiple_fasta(file_name):
    header=""
    sequence=""
    sequences=[]
    with open (file_name,'r') as file:
              for line in file:
                  line = line.strip()
                  if line.startswith(">") :
                       if header:
                          sequences.append((header,sequence))
                       header=line[1:]
                       sequence=""
                       
                  else:
                    sequence += line
    sequences.append((header,sequence))               
    return sequences  
       
