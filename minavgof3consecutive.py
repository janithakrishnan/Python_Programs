##ARRANGE THE LIST TO MINIMISE THE AVERAGE OF 3 CONSECUTIVE NUMBERS

nu=[3,9,7,6,2,1,8]
print("The entered list is:",nu)
num=sorted(nu)
numlength=len(num)
i=0
maxlist=[]
for _ in range(4):
    max1=num[len(num)-1]
    maxlist.append(max1)
    num.pop()
for i in [0,numlength-1,1,numlength-2]:
    num.insert(i,maxlist[0])
    maxlist.pop(0)
print("The sequence is:",num)