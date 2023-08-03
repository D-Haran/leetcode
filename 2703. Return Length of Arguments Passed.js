// Write a function argumentsLength that returns the count of arguments passed to it.
// https://leetcode.com/problems/return-length-of-arguments-passed/

/**
 * @return {number}
 */
var argumentsLength = function(...args) {
    // Return the length of the `args` array, which represents the count of arguments passed to the function.
    return args.length
};

// Time Complexity: O(1)
// The time complexity is O(1) because we're performing a constant number of operations, regardless of the number of arguments.

// Space Complexity: O(n)
// The space complexity is O(n) because we're storing the arguments in an array. The size of the array scales with the number of arguments.