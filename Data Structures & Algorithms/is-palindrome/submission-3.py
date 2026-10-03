class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # two pointers method
        left = 0
        right = len(s) - 1
        count = 0

        cleaned_s = "".join(char.lower() for char in s if char.isalnum())
        clean_count = int(len(cleaned_s)/2)

        while left < right:
            
            if not s[left].isalnum():
                left += 1
                continue
                
            if not s[right].isalnum():
                right -= 1
                continue
                
            print(f"Comparing: {s[left].lower()} and {s[right].lower()}")
            
            if s[left].lower() == s[right].lower():
                count += 1
            
            left += 1
            right -= 1

        print(count)
        print(clean_count)
        
        return count == clean_count