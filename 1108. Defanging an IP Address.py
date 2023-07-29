"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

https://leetcode.com/problems/defanging-an-ip-address/
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for i in address:
            if i == ".":
                res += "[.]"
            else:
                res += i

        return res