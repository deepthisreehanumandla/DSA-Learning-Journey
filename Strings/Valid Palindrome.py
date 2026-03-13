def is_palindrome_pointers(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from the left
        if not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from the right
        elif not s[right].isalnum():
            right -= 1
        # Compare characters once both pointers are on alphanumeric ones
        else:
            if s[left].lower() != s[right].lower():
                return False # Mismatch found
            left += 1
            right -= 1
            
    return True # All matching pairs found

# Example usage:
print(is_palindrome_pointers("A man, a plan, a canal: Panama")) # True
