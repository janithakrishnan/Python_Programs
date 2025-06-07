#PASCAL'S TRIANGLE

n=int(input("Enter the number of lines to be printed:"))
def factorial(n):
    if (n==0):
        return 1
    else:
        return n*factorial(n-1)
for i in range(n):
    print("  "*(n-i+1),end='')
    for j in range(i+1):
        print("  ",factorial(i)//(factorial(j)*factorial(i-j)),end='')
    print()