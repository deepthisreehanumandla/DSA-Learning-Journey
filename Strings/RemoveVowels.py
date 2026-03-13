s = "Hello hi welcome"
vowels = "aeiouAEIOU"
result = ""
for i in s:
    if i not in vowels:
        result+=i
    
print(result)        
