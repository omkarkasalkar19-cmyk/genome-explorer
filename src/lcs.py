def lcs(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]        
    for i in range(1, len(a) + 1):
     for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
         dp[i][j] = dp[i - 1][j - 1] + 1
        else:
         dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    i = len(a)
    j = len(b)
    lcs_sequence = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs_sequence.append(a[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
               i -= 1
            else:
              j -= 1
    lcs_sequence.reverse()  

          
    return "".join(lcs_sequence)       