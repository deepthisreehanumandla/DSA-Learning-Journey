# Valid Palindrome (Two Pointers)

## Problem
Check if a string is a palindrome considering only alphanumeric characters and ignoring cases.

```
Input:  "A man, a plan, a canal: Panama"
Output: True
```

---

## Code (Python)

```python
def is_palindrome_pointers(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
            
    return True

print(is_palindrome_pointers("A man, a plan, a canal: Panama"))
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
