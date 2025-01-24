# Assignment 4 (Integration) Question 21
# Team 3
'''
************** Team Members ****************
1. Amr Ayman Farouk
2. Abdelrahman sherif Ibrahim Nabil
3. Omar Ahmed Reda Abdelkader Ismail
'''

import numpy as np

'''
let u = 1/t
if t = inf -> u = 0
if t = 1/3 -> u = 3
t = 1/u -> dt = (-1/u^2) du
now a = 3, b = 0
now integration is from a to b
where I = - ((e^-1/u) / u) du
due to neg sign now limits are a = 0, b = 3
now integration is from a to b
where I = ((e^-1/u) / u) du
'''

a = 0
b = 3

'''
transform to Gauss-Legendre form
let u = (b + a) / 2 + ((b - a) / 2) * z
du = (((b - a) / 2) * z ) dz
after transformation now limits are a = -1, b = 1
'''

n = 3
intercept = (b + a) / 2   # 1.5
slope = (b - a) / 2       # 1.5

C = np.array([0.5555556, 0.8888889, 0.5555556])
X = np.array([-0.774596669, 0, 0.774596669])

# now applying function after transformation to Gauss form
def Fx (X) -> np.array:
    return np.exp(-1 / (intercept + slope * X)) / (intercept + slope * X)

CFx = C * Fx(X)
I = slope * np.sum(CFx)
print("I =", I)

    



















































