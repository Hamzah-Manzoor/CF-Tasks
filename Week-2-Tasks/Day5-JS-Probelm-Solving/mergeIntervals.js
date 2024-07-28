/**
 * Problem Statement:
 * Given a collection of intervals, merge all overlapping intervals.
 * 
 * Example:
 * Input: [[1,3],[2,6],[8,10],[15,18]]
 * Output: [[1,6],[8,10],[15,18]]
 */

function mergeIntervals(intervals) {
    if (intervals.length === 0) return [];

    intervals.sort((a, b) => a[0] - b[0]);
    
    const merged = [intervals[0]];

    for (let i = 1; i < intervals.length; i++) {
        const lastMergedInterval = merged[merged.length - 1];
        const currentInterval = intervals[i];

        if (lastMergedInterval[1] >= currentInterval[0]) {
            lastMergedInterval[1] = Math.max(lastMergedInterval[1], currentInterval[1]);
        } else {
            merged.push(currentInterval);
        }
    }
    return merged;
}

// Test
console.log(mergeIntervals([[1,3],[2,6],[8,10],[15,18]])); // [[1,6],[8,10],[15,18]]
console.log(mergeIntervals([[1,4],[4,5]])); // [[1,5]]
console.log(mergeIntervals([[1,4],[0,2],[3,5]])); // [[0,5]]
