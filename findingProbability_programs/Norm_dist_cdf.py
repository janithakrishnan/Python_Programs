from scipy.stats import norm

# Given normal distribution parameters
mu = 65        # Mean
sigma = 9     # Standard deviation

# Q1. P(X < 54)
p1 = norm.cdf(54, mu, sigma) #cdf- Cummulative Distribution Function
print("Q1: P(X < 54) =", round(p1, 4)) 

# Q2. P(X > 80)
p2 = 1 - norm.cdf(80, mu, sigma)
print("Q2: P(X > 80) =", round(p2, 4))  

# Q3. P(70 < X < 86)
p3 = norm.cdf(86, mu, sigma) - norm.cdf(70, mu, sigma)
print("Q3: P(60 < X < 85) =", round(p3, 4))