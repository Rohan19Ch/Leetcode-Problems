def longestCommonSubsequence(s):
        text1 = s[:]
        text2 = s[::-1]
        n = len(text1)
        m = len(text2)
        DP = [[0 for j in range(m+1)]for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    DP[i][j] = DP[i-1][j-1] + 1
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        return DP[i][j]
print(longestCommonSubsequence("cbbd"))