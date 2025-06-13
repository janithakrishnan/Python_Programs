#find the longest word in a sentence
sentence=input("enter the sentence:")
print("INPUT: ", sentence)
words=list(sentence.split())
a=max(words,key=len)
print("Maximum Length:",len(a))
print("Word(s) with maximum length:",[w for w in words if len(w)==len(a)])