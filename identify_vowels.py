#ASSIGNMENT 5: QUESTION 1
#Identify vowels in the input string
vowels=['a','e','i','o','u']
string1= input("Enter the string:")
found=[]
loc=0
for char_i in string1:
    if char_i in vowels:
        if char_i not in found:
            found.append(char_i)
print(found)
