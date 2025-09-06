"""
LeetCode Problem 516: Longest Palindromic Subsequence

Problem Description:
Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or 
no elements without changing the order of the remaining elements.

Time Complexity: O(n²) where n is the length of the string
Space Complexity: O(n²) for the DP table

Example:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Approach: Convert to LCS problem by finding LCS between string and its reverse.
"""

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