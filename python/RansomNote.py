class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = set(ransomNote)
        for char in s:
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True