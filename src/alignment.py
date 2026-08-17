def hamming_distance(sequence1, sequence2):
    count = 0

    if len(sequence1) != len(sequence2):
        raise ValueError("sequence must have equal length")

    for i in range(len(sequence1)):
        if sequence1[i] != sequence2[i]:
            count += 1

    return count