#Write a program to convert a string "python is fun" to "py is on" 
#using only the methods available to the list (append, remove, pop, insert, extend)

string1=list('python is fun')
string1.remove('t')
string1.remove('h')
string1.insert(2,string1[4])
string1.insert(3,string1[6])
string1.insert(4,string1[8])
string1.insert(5,string1[10])
length1=int(len(string1))
for i in range(8,length1):
  string1.pop()
string1=''.join(string1)
print(string1)
