'''An exam has 5 multiple-choice questions with 4 choices each (only one correct). If a student
guesses all answers randomly, what is the probability they get exactly 3 questions correct?'''

def fact(num):
    num=int(num)
    factorial=1
    for i in range(1,num+1):
        factorial=i*fact(num-1)
    return factorial

n_questions=5
n_choices=4
P_correct=1/4
n_times=3
P_E=(fact(n_questions)/(fact(n_questions-n_times)*fact(n_times)))*pow(P_correct,n_times)*pow((1-P_correct),(n_questions-n_times))
print(P_E)