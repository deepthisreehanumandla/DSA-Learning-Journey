Input:
arr = [1,2,2,2,3,4]
target = 2

Output:
3

def last_occurrence(arr, target):
    
    left = 0
    right = len(arr) - 1
    ans = -1
    
    while left <= right:
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            ans = mid
            left = mid + 1
        
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return ans
