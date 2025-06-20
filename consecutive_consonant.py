#Check whether more than 4 consecutive consonants are there in a string
chkstr=input("Enter the string")
print(f"Entered string is {chkstr}")
vowelss=list("aeiou ")
print(vowelss)
countc=0
flagg=0
for ch in chkstr:
    if ch not in vowelss:
        countc+=1
        if countc==4:
            flagg=1
            break
    else:
        countc=0
if flagg==1:
    print(f"{chkstr} is Not readable")
else:
    print(f"{chkstr} is Readable")