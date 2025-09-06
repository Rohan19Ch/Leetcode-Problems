"""
LeetCode Problem 1143: Longest Common Subsequence

Problem Description:
Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence is a sequence that can be derived from another sequence by deleting some or 
no elements without changing the order of the remaining elements.

Time Complexity: O(m * n) where m and n are the lengths of the two strings
Space Complexity: O(m * n) for the DP table

Example:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Input: text1 = "abc", text2 = "abc"
Output: 3

Input: text1 = "abc", text2 = "def"
Output: 0

Approach: Dynamic Programming - build a 2D table where DP[i][j] represents LCS of first i and j characters.
"""

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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