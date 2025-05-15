#Use a dictionary to count the no:of vowels in a string

vowels={'a':0,
        'e':0,
        'i':0,
        'o':0,
        'u':0}
user_string=input("Enter the string:")
print("The entered string is:",user_string)
for char in user_string: #for each char in the user string
    if char in vowels:  #if char matches with any of the key in vowels dictionary
        vowels[char]=vowels[char]+1     #value of the corresponding char is incremented
print(vowels)
