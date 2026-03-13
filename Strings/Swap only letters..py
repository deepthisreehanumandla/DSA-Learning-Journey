string = "123deepu2345"
s = list(string)

left = 0
right = len(s) - 1

while left<right:
    if not s[left].isalpha():
        left+=1
    elif not s[right].isalpha():
        right-=1
    else:
        s[left],s[right] = s[right],s[left]
        left+=1
        right-=1
print("".join(s))    
