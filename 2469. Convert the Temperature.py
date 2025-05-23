"""
You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10-5 of the actual answer will be accepted.

https://leetcode.com/problems/convert-the-temperature/description/
"""

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        res = [celsius+273.15, (celsius*1.80)+32]
        return res

    # Time Complexity: O(1)
    # Space Complexity: O(1)
