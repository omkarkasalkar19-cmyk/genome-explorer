def count_nucleotides(sequence):
 a_count = 0
 t_count = 0
 g_count = 0
 c_count = 0
 for nucleotide in sequence:
      if nucleotide == "A" :
        a_count += 1
      elif nucleotide == "T" :
            t_count += 1
      elif nucleotide == "G" :
            g_count += 1
      elif nucleotide == "C" :
            c_count += 1
 return a_count, t_count, g_count, c_count 