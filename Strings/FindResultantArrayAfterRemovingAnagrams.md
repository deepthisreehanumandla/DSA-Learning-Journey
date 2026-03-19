# Find Resultant Array After Removing Anagrams (LeetCode 2273)

## Problem
Remove consecutive strings that are anagrams of each other and return the remaining array.

```
Input:  words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]
```

---

## Approach
**Technique Used:** Sorting + String Comparison

- Sort each word → canonical form
- Compare with previous word
- Skip if same (anagram)

---

## Code (Python)

```python
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []

        for word in words:
            if not result or sorted(word) != sorted(result[-1]):
                result.append(word)

        return result
```

---

## Time Complexity
```
O(n * k log k)
```

## Space Complexity
```
O(n)
```
