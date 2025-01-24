import numpy as np
import matplotlib.pyplot as plt

def simple_harmonic_oscillator(t, y, v):
    """
    Calculates the derivatives for the simple harmonic oscillator:
    dy/dt = v  ---> f (uses k coefficient)
    dv/dt = -y ---> g (uses m coefficient)
    """
    f = v
    g = -y
    return f, g


# Euler's Method Implementation
def euler_method(t0, y0, v0, h, t_values):
    y_values = []
    v_values = []
    y, v = y0, v0
    '''
    - Calculates y_i+1 & v_i+1 for each ti
    - Uses the euler formula y_i+1 = y_i + f(x_i, y_i) * h
    - Since this problem is a second-order ODE then formulas are as follows
        # y_i+1 = y_i + f(t_i, y_i, v_i) * h where f = v
        # v_i+1 = v_i + g(t_i, y_i, v_i) * h where g = -y
    '''
    for t in t_values:
        y_values.append(y)
        v_values.append(v)

        f, g = simple_harmonic_oscillator(t, y, v)
        y = y + h * f
        v = v + h * g

    return np.array(y_values), np.array(v_values)

# 4th-Order Runge-Kutta Method Implementation
def runge_kutta_method(t0, y0, v0, h, t_values):
    y_values = []
    v_values = []

    y, v = y0, v0
    '''
    - Calculates y & v for each t
    - Uses the Runge-Kutta formula : y = y_0 + (h/6) * (k1 + 2*k2 + 2*k3 + k4) where k1, k2, k3, and k4 are as follows:
        # k1 = f(x_0, y_0)                  # k2 = f(x_0 + h/2, y_0 + ((k1 * h) / 2))
        # k2 = f(x_0 + h/2, y_0 + ((k2 * h) / 2))
        # k4 = f(x_0 + h, y_0 + k3 * h)
        
    - Since this problem is a second-order ODE then formulas are as follows
        # k1 = f(t_0, y_0, v_0)
        # m1 = g(t_0, y_0, v_0)
        # k2 = f(t_0 + h/2, y_0 + ((k1 * h) / 2), v_0 + ((m1 * h) / 2))
        # m2 = g(t_0 + h/2, y_0 + ((k1 * h) / 2), v_0 + ((m1 * h) / 2))
        # k3 = f(t_0 + h/2, y_0 + ((k2 * h) / 2), v_0 + ((m2 * h) / 2))
8        # m3 = g(t_0 + h/2, y_0 + ((k2 * h) / 2), v_0 + ((m2 * h) / 2))
        # k4 = f(t_0 + h, y_0 + k3 * h, v_0 + m3 * h)
        # k4 = g(t_0 + h, y_0 + k3 * h, v_0 + m3 * h)
        
        #y = y_0 + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        #v = v_0 + (h/6) * (m1 + 2*m2 + 2*m3 + m4)
    '''
    for t in t_values:
        y_values.append(y)
        v_values.append(v)

        k1, m1 = simple_harmonic_oscillator(t, y, v)
        k2, m2 = simple_harmonic_oscillator(t + (h / 2), y + ((k1 * h) / 2), v + ((m1 * h) / 2))
        k3, m3 = simple_harmonic_oscillator(t + (h / 2), y + ((k2 * h) / 2), v + ((m2 * h) / 2))
        k4, m4 = simple_harmonic_oscillator(t + h, y + h * k3, v + h * m3)

        y += h/6 * (k1 + 2 * k2 + 2 * k3 + k4)
        v += h/6 * (m1 + 2 * m2 + 2 * m3 + m4)

    return np.array(y_values), np.array(v_values)

# Exact Solution
def exact_solution(t, y0):
    return y0 * np.cos(t)

def calculate_avg_exact_error(y_numerical, y_exact):
    exact_error = np.abs((y_exact - y_numerical) / y_exact)
    avg_exact_error = np.mean(exact_error)
    return avg_exact_error

def plot_comparison(t_values, y_euler, y_rk, y_exact):
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, y_euler, label= "Euler's Method", linestyle= "-", marker= "o", markersize=4)
    plt.plot(t_values, y_rk, label= "Runge-Kutta Method", linestyle= "-", marker= "s", markersize=4)
    plt.plot(t_values, y_exact, label= "Exact Solution", linestyle= "-", color= "black")

    plt.xlabel("Time (t)")
    plt.ylabel("Displacement (y)")
    plt.title("Numerical Solution of the Simple Harmonic Oscillator")
    plt.legend()
    plt.grid()
    plt.show()

# Parameters
y0 = 1.0  # Initial displacement
v0 = 0.0  # Initial velocity
t0 = 0.0  # Start time
t_end = 10.0  # End time
h_values = [0.01, 0.05, 0.09]  # Step size
# h_values = [0.1, 0.5,0.9] to check convergence

for h in h_values:
    t_values = np.arange(t0, t_end, h)  # Generates evenly spaced values within a given interval (Works exactly like table mode in calculator)
    # Soloution using Euler's Method
    y_euler, v_euler = euler_method(t0, y0, v0, h, t_values)

    # Soloution using Runge-Kutta Method
    y_rk, v_rk = runge_kutta_method(t0, y0, v0, h, t_values)

    # Exact solution
    y_exact = exact_solution(t_values, y0)

    plot_comparison(t_values, y_euler, y_rk, y_exact)
    avg_exact_error_euler = calculate_avg_exact_error(y_euler, y_exact)
    avg_exact_error_rk = calculate_avg_exact_error(y_rk, y_exact)

    print(f"Step size h = {h}")
    print(f"Average exact error (Euler's Method): {avg_exact_error_euler:.4f}%")
    print(f"Accuracy (Euler's Method): {100 - avg_exact_error_euler:.4f}%")
    print(f"Average exact error (Runge-Kutta Method): {avg_exact_error_rk:.4f}%")
    print(f"Accuracy (Runge-Kutta Method): {100 - avg_exact_error_rk:.4f}%\n")




