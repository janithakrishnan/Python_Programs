#Letter Count
alphabet=list('abcdefghijklmnopqrstuvwxyz')
x=input("ENTER THE STRING:")
print(alphabet)
letter_freq={}
for ltr in x:
    if ltr in alpha:
        letter_freq.setdefault(ltr,0)
        letter_freq[ltr]+=1
for k,v in sorted(letter_freq.items()):
    print(f"letter {k} is present {v} times")
