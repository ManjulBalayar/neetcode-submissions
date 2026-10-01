class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""

        for s in strs:
            final_str += str(len(s)) + "#" + s
        
        return final_str


    def decode(self, s: str) -> List[str]:
        final_list = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]

            final_list.append(word)

            i = j + 1 + length

        return final_list