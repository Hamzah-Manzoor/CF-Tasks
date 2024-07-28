/**
 * Problem Statement:
 * Given a string s, find the length of the longest substring without repeating characters.
 * 
 * Example:
 * Input: "abcabcbb"
 * Output: 3 (Explanation: The answer is "abc", with the length of 3.)
 */

function lengthOfLongestSubstring(s) {
    let maxLength = 0;
    let start = 0;
    const seenChars = new Map();

    for (let i = 0; i < s.length; i++) {
        if (seenChars.has(s[i])) {
            start = Math.max(seenChars.get(s[i]) + 1, start);
        }
        seenChars.set(s[i], i);
        maxLength = Math.max(maxLength, i - start + 1);
    }
    return maxLength;
}

// Test
console.log(lengthOfLongestSubstring("abcabcbb")); // 3
console.log(lengthOfLongestSubstring("bbbbb")); // 1
console.log(lengthOfLongestSubstring("pwwkew")); // 3
