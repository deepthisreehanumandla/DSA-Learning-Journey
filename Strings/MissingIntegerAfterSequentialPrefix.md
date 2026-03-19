# Missing Integer After Sequential Prefix (LeetCode 2996)

## Problem
Find the smallest integer ≥ sum of the longest sequential prefix that is not present in the array.

```
Input:  nums = [1,2,3,2,5]
Output: 6
```

---

## Approach
**Technique Used:** Array Traversal + HashSet

- Find longest consecutive prefix
- Compute its sum
- Use set for fast lookup
- Find smallest missing ≥ sum

---

## Code (Python)

```python
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break

        s = set(nums)

        while prefix_sum in s:
            prefix_sum += 1

        return prefix_sum
```

---

## Time Complexity
```
O(n)
```

## Space Complexity
```
O(n)
```
