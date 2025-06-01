'''A box contains 4 red and 6 black balls. A second box contains 5 red and 5 black balls.
A box is selected at random, and then a ball is drawn.
If the ball drawn is red, what is the probability it came from the first box?'''

b1_red=4
b1_black=6
n_b1=b1_red+b1_black
b2_red=5
b2_black=5
n_b2=b2_red+b2_black
P_b1=1/2
n_red=b1_red+b2_red
n_black=b1_black+b2_black
total=n_red+n_black
P_red=n_red/total
P_both_b1andRed=b1_red/total
P_b1_given_red=P_both_b1andRed/P_red
print(f"P_b1_given_red = {P_b1_given_red}")