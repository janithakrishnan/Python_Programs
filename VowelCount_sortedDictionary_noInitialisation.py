#Vowel Count
vowels=['a','e','i','o','u']
ustr=input("Enter the string:")
found={}
for letter in ustr:
    if letter in vowels:
        if letter not in found:
            found[letter]=0
        found[letter]+=1
print(f"The user input is: {ustr}")
for k,v in sorted(found.items()):
    print(f"Vowel {k} is found {v} times")