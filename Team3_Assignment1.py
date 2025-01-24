# Assignment 1 (Errors) Question 4
# Team 3 
'''
************** Team Members ****************
1. Amr Ayman Farouk
2. Abdelrahman sherif Ibrahim Nabil
3. Omar Ahmed Reda Abdelkader Ismail
'''


# Data from given table
x = [1.2, 1.4, 1.6, 1.8, 2]
fx = [2.572, 5.798, -34.233, -4.286, -2.185]

# Defining the finite difference formula for second derivative
def compute_second_derivative(fx_i, fx_i_prev, fx_i_next, h):
    return (fx_i_next - 2*fx_i + fx_i_prev) / (h**2)

# (a) h = 0.2
h1 = 0.2
fx_i = fx[2]       # f(1.6)
fx_i_prev = fx[1]  # f(1.4)
fx_i_next = fx[3]  # f(1.8)

# Calculating the second derivatives for h = 0.2
answer_A = compute_second_derivative(fx_i, fx_i_prev, fx_i_next, h1)

# (b) h = 0.4
h2 = 0.4
fx_i = fx[2]       # f(1.6)
fx_i_prev = fx[0]  # f(1.2)
fx_i_next = fx[4]  # f(2.0)

# Calculating the second derivatives for h = 0.4
answer_B = compute_second_derivative(fx_i, fx_i_prev, fx_i_next, h2)

print(f"(a) {answer_A:.4f}")
print(f"(b) {answer_B:.4f}\n")
print("The lower the step size, the more accurate the approximation is.")


