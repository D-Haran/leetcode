"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
https://www.lintcode.com/problem/659/ 
(Leetcode premium, but free on Lintcode)
"""

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, str: str) -> List[str]:
        res = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

    # Time Complexity: O(n)

    # Space Complexity: O(n)