# Trapping Rain Water (LeetCode 42)
<img width="412" height="161" alt="image" src="https://github.com/user-attachments/assets/c5a39dbf-900c-48e7-9994-0945d55f6da8" />

## Problem
Given an array `height`, compute how much water it can trap.

```
Input:  [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

---

## Approach
**Technique Used:** Two Pointers

- Use two pointers (`i`, `j`)
- Track `maxleft` and `maxright`
- Move the smaller side
- Water = max height seen - current height

---

## Code (Python)

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = 0
        maxright = 0
        i = 0
        j = len(height) - 1
        water = 0

        while i <= j:
            if height[i] <= height[j]:
                maxleft = max(maxleft, height[i])
                water += maxleft - height[i]
                i += 1
            else:
                maxright = max(maxright, height[j])
                water += maxright - height[j]
                j -= 1

        return water
```

---

## Time Complexity
```
O(n)
```

## Space Complexity
```
O(1)
```

![Uploading image.png…]()
