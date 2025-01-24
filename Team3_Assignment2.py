# Assignment 3 (Curve Fitting) Question 4
# Team 3
'''
************** Team Members ****************
1. Amr Ayman Farouk
2. Abdelrahman sherif Ibrahim Nabil
3. Omar Ahmed Reda Abdelkader Ismail 
'''

import numpy as np
from sympy import symbols, Eq, solve

# Data from given table
h = np.array([0, 866, 2753, 4763, 6942, 10593])
P = np.array([30, 23, 27, 26, 23, 20])

# Method 1 : Using Scipy Library

from scipy.stats import linregress

# Step 1: Linearize the equation
'''
P = ae^(bh)
Ln(P) = Ln(a) + Ln(e^(b * h))
Ln(P) = Ln(a) + b * h
  Y   =  ao  + a1 * X
  Y = Ln(P), ao = Ln(a), a1 = b, X = h
'''

Y = np.log(P)  # Y = Ln(P)
X = h          # X = h (no transformation needed)

# Step 2: Perform linear regression on the transformed data
slope, intercept, r_value, p_value, std_err = linregress(X, Y)

# Step 3: Get a and b
a1 = slope
a0 = intercept
a = np.exp(a0)  # a0 = Ln(a) -> a = e^(a0)
b = a1          # a1 = b
r = r_value
St = std_err

# Step 4: Calculate the regression error Sr
P_predictions = a * np.exp(b * h)
Sr = np.sum((P - P_predictions) ** 2)

# Output the results
print(f"Calculated values using linear fitting using scipy library:")
print(f"a = {a}")
print(f"b = {b}")
print(f"Sr = {Sr}")

# Method 2: Using manual calculations as in course

n = X.shape[0]
ΣX = np.sum(X)
ΣX_squared = np.sum(X**2)
ΣXY = np.sum(X*Y)
ΣY = np.sum(Y)

a0, a1 = symbols('a0, a1')
eqn_1 = Eq(n * a0 + ΣX * a1, ΣY)
eqn_2 = Eq(ΣX * a0 + ΣX_squared * a1, ΣXY)

solution = solve((eqn_1, eqn_2), (a0, a1))
a0_symbolic = solution[a0]
a1_symbolic = solution[a1]
a0 = float(a0_symbolic.evalf())
a1 = float(a1_symbolic.evalf())
a = np.exp(a0)
b = a1

P_predictions = a * np.exp(b * h)
Sr = np.sum((P - P_predictions) ** 2)

print(f"\nCalculated values using linear fitting using manual solution:")
print(f"a = {a}")
print(f"b = {b}")
print(f"Sr = {Sr}")



