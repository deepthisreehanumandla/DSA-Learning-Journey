# Substrings in a String

## Problem
Generate all substrings of a given string.

```
Input:  "abc"
Output: ["a","ab","abc","b","bc","c"]
```

---

## Code (Python)

```python
def substrings(s: str):
    result = []

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            result.append(s[i:j])

    return result

print(substrings("abc"))
```

---

## Time Complexity
```
O(n²)
```

## Space Complexity
```
O(n²)
```
