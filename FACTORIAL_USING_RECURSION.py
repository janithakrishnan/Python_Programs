#FACTORIAL USING RECURSION
factorial=1
def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
    return factorial
num=int(input("Enter the number: "))
print(f"The factorial of {num} is {fact(num)}")