"""
LeetCode Problem 3: Longest Substring Without Repeating Characters

Problem Description:
Given a string s, find the length of the longest substring without repeating characters.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(min(m,n)) where m is the size of the character set

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Approach: Sliding window technique with hash map to track character positions.
"""

def lengthOfLongestSubstring(s: str) -> int:
        n = len(s)
        visited = {}
        maxLen = 0
        start = 0
        end = 0
        while end < n:
            if s[end] not in visited:
                maxLen = max(maxLen, end - start + 1)
            else:
                if visited[s[end]] < start:
                    maxLen = max(maxLen, end - start + 1)
                else:
                    start  = visited[s[end]] + 1
            visited[s[end]] = end
            end += 1
        return maxLen
print(lengthOfLongestSubstring(s = "uqinntq"))