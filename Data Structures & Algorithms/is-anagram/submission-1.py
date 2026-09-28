class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        # Method 1 (by values itself): 
        # better when you only need the values
        for i in s:
            countS[i] = 1 + countS.get(i, 0)
        
        for i in t:
            countT[i] = 1 + countT.get(i, 0)

        sCount, tCount = {}, {}

        # Method 2 (by index):
        # useful when you need the index or want to access multiple sequences
        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)


        return sCount == tCount
        

        