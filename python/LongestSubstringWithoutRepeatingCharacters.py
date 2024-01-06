class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        queue = deque()

        for char in s:
            while char in queue:
                queue.popleft()
            queue.append(char)
            maxLen = max(maxLen, len(queue))

        return maxLen