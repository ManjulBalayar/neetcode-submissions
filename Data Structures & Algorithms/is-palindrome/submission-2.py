class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for char in s:
            if char.isalnum():
                result += char.lower()
        print(result)

        rev = "".join(reversed(result))

        print(rev)
        if result == rev:
            return True
        
        return False