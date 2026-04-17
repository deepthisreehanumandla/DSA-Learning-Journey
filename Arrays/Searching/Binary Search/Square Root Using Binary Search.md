Input: 16
Output: 4

Idea of the Algorithm

Instead of checking every number, we binary search between 1 and n.
We check:
mid * mid
If mid² ≤ n → mid can be the answer, but maybe a bigger number also works → move right
If mid² > n → mid is too large → move left
We store the latest valid mid in ans.

def sqrt_binary(n):
    
    left = 1
    right = n
    ans = 0
    
    while left <= right:
        
        mid = (left + right) // 2
        
        if mid * mid <= n:
            ans = mid
            left = mid + 1
        
        else:
            right = mid - 1
    
    return ans
