# Group Anagrams (LeetCode 49)

## Problem 
Group strings that are anagrams of each other.

```
Input:  ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]] 
```

---

## Approach
**Technique Used:** HashMap (Frequency/Sorted Key)

- Use sorted string as key
- Group words with same key

---

## Code (Python)

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            hashmap[key].append(word)

        return list(hashmap.values())
```

---

## Time Complexity
```
O(n * k log k)
```

## Space Complexity
```
O(n * k)
```
