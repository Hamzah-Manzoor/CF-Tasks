/**
 * Problem Statement:
 * Given an array nums of n integers where n > 1, return an array output such that output[i] 
 * is equal to the product of all the elements of nums except nums[i].
 * 
 * Example:
 * Input: [1,2,3,4]
 * Output: [24,12,8,6]
 */

function productExceptSelf(nums) {
    const length = nums.length;
    const result = new Array(length).fill(1);
    let prefix = 1;
    let suffix = 1;

    for (let i = 0; i < length; i++) {
        result[i] *= prefix;
        prefix *= nums[i];
    }

    for (let i = length - 1; i >= 0; i--) {
        result[i] *= suffix;
        suffix *= nums[i];
    }

    return result;
}

// Test
console.log(productExceptSelf([1,2,3,4])); // [24,12,8,6]
console.log(productExceptSelf([0,0])); // [0,0]
console.log(productExceptSelf([1,2,3,0])); // [0,0,0,6]
