```
Input:  [-2, 3, 4, -1, 5]

Output:
Positive = 3
Negative = 2

arr = [-2,3,4,-1,5]

pos = 0
neg = 0

for num in arr:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1

print("Positive:",pos)
print("Negative:",neg)
```
