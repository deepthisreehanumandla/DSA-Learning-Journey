# Largest 3 Same Digits in a String

## Problem
Find the largest substring of length 3 where all digits are the same.

```
Input:  "6777133339"
Output: "777" 
```

If no such substring exists, return `""`.

---

## Code (Python)

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                res = max(res, num[i:i+3])
        
        return res
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
