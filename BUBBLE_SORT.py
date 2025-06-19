#BUBBLE SORT
l=list(input("ENTER THE NUMBERS (separated by space):").split())
print(f"The entered elements are:{l}")
for i in range(0,len(l)):
    for j in range(0,len(l)-i-1):
        if int(l[j])>int(l[j+1]):
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(f"The sorted elements are:{l}")