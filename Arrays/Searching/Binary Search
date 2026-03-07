Binary Search is a searching algorithm used on a sorted array.

Instead of checking every element like Linear Search, it repeatedly divides the array into halves.
Binary Search works only when the array is sorted.

Steps:
-Find the middle element
-Compare it with the target
-If target is smaller → search left half
-If target is larger → search right half

Repeat until element is found or range becomes empty

arr = [1,3,5,7,9,11]
target = 7

left = 0
right = len(arr) - 1

while left <= right:
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        print(mid)
        break
        
    elif arr[mid] < target:
        left = mid + 1
        
    else:
        right = mid - 1
