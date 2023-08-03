"""
You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10-5 of the actual answer will be accepted.

https://leetcode.com/problems/convert-the-temperature/description/
"""

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # Convert Celsius to Kelvin and Fahrenheit and store the results in `res`.
        res = [celsius+273.15, (celsius*1.80)+32]
        # Return `res`.
        return res

    # Time Complexity: O(1)
    # The time complexity is O(1) because we're performing a constant number of operations. 

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with the size of the input.
