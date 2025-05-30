# AMSTRONG NUMBER
numstr=input("Enter the number:")
order=len(numstr)
sum_num=0
for n in numstr:
    num=int(n)
    sum_num+=num**order
if int(numstr)==sum_num:
    print(f"{numstr} is an Amstrong Number")
else:
    print(f"{numstr} is not an Amstrong Number")