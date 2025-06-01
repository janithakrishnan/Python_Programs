'''In a company: 70% of employees know Python, 60% know SQL, and 50% know both.
 What is the probability that an employee knows SQL given they know Python?'''

P_python=70/100
P_SQL=60/100
P_both=50/100
P_SQL_given_Python=P_both/P_python
print(f"P_SQL_given_Python= {P_SQL_given_Python}")