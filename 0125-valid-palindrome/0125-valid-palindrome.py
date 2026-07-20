class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        clean_s = "".join([char for char in s if char.isalnum()])
        clean_s = clean_s.lower()
        if clean_s == clean_s[::-1]:
            return True
        return False