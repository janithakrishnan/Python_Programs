'''A rare disease affects 0.1% of the population. A test has 99% sensitivity and 98% specificity.
What is the probability that a person has the disease given that they tested positive?'''

P_disease=.1/100
P_nodisease=1-P_disease
P_Positive_given_disease=.99
P_Negative_given_noDisease=.98
P_Positive_given_noDisease=1-P_Negative_given_noDisease
P_positive=P_disease*P_Positive_given_disease+P_nodisease*P_Positive_given_noDisease
P_disease_given_positive= P_Positive_given_disease*P_disease/P_positive
print(f"P_disease_given_positive= {P_disease_given_positive}")