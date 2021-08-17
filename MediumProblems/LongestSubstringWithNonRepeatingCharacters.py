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