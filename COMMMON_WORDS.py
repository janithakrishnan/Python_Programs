#FIND COMMMON WORDS IN TWO STRINGS
str1=input("enter first string").split()
str2=input("enter second string").split()
common=""
for i in str1:
    for j in str2:
        if i==j:
            common=common+i
print("COMMON WORDS",common)