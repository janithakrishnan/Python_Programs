''' In a class: 40% of students play cricket, 30% play football, and 15% play both. 
What is the probability that a student plays cricket given that they play football?'''

P_cricket=40/100
P_football=30/100
P_both=15/100
P_cricket_given_football= P_both/P_football
print(f"P_cricket_given_football ={P_cricket_given_football}")