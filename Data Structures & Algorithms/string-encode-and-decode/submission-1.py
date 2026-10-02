class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for i in strs:
            res += str(len(i)) + "#" + i
        print(res)
        return res


    def decode(self, s: str) -> List[str]:

        res, p = [], 0

        while p < len(s):
            i = p

            while s[i] != "#":
                i += 1

            l = int(s[p:i])
            res.append(s[i+1: i+1+l])
            p = i + 1 + l

        
        return res



