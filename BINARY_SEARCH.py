#BINARY SEARCH

def bin_srch(element,list1,min1,max1):
    if min1<=max1:
        mid=(min1+max1)//2
        if element==list1[mid]:
            print(f"{element} is present at {mid}")
        elif element<list1[mid]:
            bin_srch(element,list1,min1,mid-1)
        else:
            bin_srch(element,list1,mid+1,max1)
    else:
        print(f"{element} is not present" )

numlist=[6,7,8,9,2,0]
numlist=sorted(numlist)
print(numlist)
element=int(input("Enter the number to search"))
bin_srch(element,numlist,0,len(numlist)-1)