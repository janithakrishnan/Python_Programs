'''There are three bags:
- Bag A: 2 white, 3 black
- Bag B: 1 white, 4 black
- Bag C: 5 white, no black
A bag is chosen at random and a ball is drawn. It is white. 
What is the probability that it came from
Bag C?'''

A_white=2
A_black=3
B_white=1
B_black=4
C_white=5
C_black=0
n_A=A_white+A_black
n_B=B_white+B_black
n_C=C_white+C_black
total=n_A+n_B+n_C
P_white=(A_white+B_white+C_white)/total
P_white_given_C=C_white/n_C
P_C=1/3
P_C_given_white=P_white_given_C * P_C/P_white
print(f"P_C_given_white= {P_C_given_white}")