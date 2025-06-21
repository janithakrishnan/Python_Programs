#FINDING MINIMUM OF THE SUMMATION OF AVERAGE OF GROUPS OF 3
#GREEDY APPROACH
l=list(map(int,input().split()))
sum_avg=0
print(l)
l=sorted(l)
j=0
for i in range(0,len(l),3):
    j+=1
    group=l[i:i+3]
    print(f"group{j} is {group}")
    sum_avg=(sum(group))/3+sum_avg

print("MINIMUM AVERAGE:", sum_avg)