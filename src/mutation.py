def detect_mutation(sequence1, sequence2):
  for i in range(len(sequence1)):
    if sequence1[i] != sequence2[i]:
     position = i+1
     original= sequence1[i]
     mutated= sequence2[i]
     mutated_type='substitution'
     return position,original,mutated,mutated_type