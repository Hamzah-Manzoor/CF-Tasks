/**
 * Problem Statement:
 * Given an integer array nums, find the contiguous subarray (containing at least one number) 
 * which has the largest sum and return its sum.
 * 
 * Example:
 * Input: [-2,1,-3,4,-1,2,1,-5,4]
 * Output: 6 (Explanation: [4,-1,2,1] has the largest sum = 6.)
 */

function maxSubArray(nums) {
    let maxSum = nums[0];
    let currentSum = nums[0];

    for (let i = 1; i < nums.length; i++) {
        currentSum = Math.max(nums[i], currentSum + nums[i]);
        maxSum = Math.max(maxSum, currentSum);
    }

    return maxSum;
}

// Test
console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])); // 6
console.log(maxSubArray([1])); // 1
console.log(maxSubArray([5,4,-1,7,8])); // 23
