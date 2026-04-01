Input:  [3, 4, 7, 8, 10]
Output: 3

arr = [3,4,7,8,10]

count = 0

for num in arr:
    if num % 2 == 0:
        count += 1

print(count)
