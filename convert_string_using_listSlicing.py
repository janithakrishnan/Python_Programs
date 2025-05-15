#Write a program to convert a string "python is fun" to "py is on" 
#using list slicing

string_list1=list('python is fun')
print(string_list1)
string_list2=string_list1[0:2]+string_list1[6:10]+string_list1[4:6]
print(string_list2)
print( ''.join(string_list2)) #Printing new list as string
