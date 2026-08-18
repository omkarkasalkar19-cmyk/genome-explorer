def hamming_distance(sequence1, sequence2):
    count = 0

    if len(sequence1) != len(sequence2):
        raise ValueError("sequence must have equal length")

    for i in range(len(sequence1)):
        if sequence1[i] != sequence2[i]:
            count += 1

    return count

def needleman_wunsch(alignment_seq1, alignment_seq2):
    match=1
    mismatch=-1
    gap = -2
    rows=len(alignment_seq1)+1
    cols=len(alignment_seq2)+1
    matrix=[[0]*cols for _ in range(rows)]
    # First coloumn
    for i in range(rows):
      matrix[i][0] = i * gap
    # first row  
    for j in range(cols):
      matrix[0][j] = j * gap
    # remaining cell  
    for i in range(1, rows):
        for j in range(1, cols):  
         if alignment_seq1 [i-1] == alignment_seq2[j-1]:
          diagonal = matrix[i-1][j-1] + match
         else:
          diagonal = matrix[i-1][j-1] + mismatch

         up = matrix[i-1][j] + gap
         left = matrix[i][j-1] + gap
         matrix[i][j] = max(diagonal, up, left)
    aligned_seq1 = ""
    aligned_seq2 = ""

    i = len(alignment_seq1)
    j = len(alignment_seq2)

         
    while i > 0 or j > 0:
        if alignment_seq1[i-1] == alignment_seq2[j-1]:
              score = match
        else:
              score = mismatch
        diagonal = matrix[i-1][j-1] + score      
        if matrix[i][j] == diagonal:
           aligned_seq1 += alignment_seq1[i-1]
           aligned_seq2 += alignment_seq2[j-1]
           i -= 1
           j -= 1

        elif matrix[i][j] == matrix[i-1][j] + gap:
           aligned_seq1 += alignment_seq1[i-1]
           aligned_seq2 += "-"
           i -= 1   
        else:
          aligned_seq1 += "-"
          aligned_seq2 += alignment_seq2[j-1]
          j -= 1

    aligned_seq1 = aligned_seq1[::-1]
    aligned_seq2 = aligned_seq2[::-1]

    score = matrix[len(alignment_seq1)][len(alignment_seq2)]
          
    return matrix , aligned_seq1, aligned_seq2,score