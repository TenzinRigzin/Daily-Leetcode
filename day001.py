"""
# Max Consecutive Ones

## Problem Statement
Given a binary array `nums`, return the maximum number of consecutive 1's in the array.

### Examples

**Example 1:**
*   **Input:** `nums = [1,1,0,1,1,1]`
*   **Output:** `3`
*   **Explanation:** The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

**Example 2:**
*   **Input:** `nums = [1,0,1,1,0,1]`
*   **Output:** `2`

### Constraints
*   `1 <= nums.length <= 10^5`
*   `nums[i]` is either `0` or `1`.

---

"""
## Solution
class Solution(object):
    def findMaxConsecutiveOnes(self,nums):
        maxCount = 0
        currentCount = 0

        for num in nums:
            if num == 1:
                currentCount += 1
            else:
                if currentCount > maxCount:
                    maxCount = currentCount
                currentCount = 0
        return max(maxCount, currentCount)


    nums = [1,1,0,1,1,1]
    self=1
    findMaxConsecutiveOnes(self,nums)

