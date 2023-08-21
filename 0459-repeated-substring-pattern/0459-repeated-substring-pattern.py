class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s==(s[:i+1]*(len(s)//len(s[:i+1]))):
                return True
        return False