import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


# Fitting function
def func(x, a, b, c):
    return a*x**2 + b*x + c


# Experimental x and y data points
xData = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
yData = np.array([26, 15, 9, 4, 1, 0.2, 1, 4, 8, 16, 24])

# Plot experimental data points
plt.plot(xData, yData, 'bo', label='experimental-data')

# Initial guess for the parameters
# initialGuess = [1.0, 1.0, 1.0]

# Perform the curve-fit
popt, pcov = curve_fit(func, xData, yData)
print(popt)

# Plot the fitted function
plt.plot(xData, func(xData, *popt), 'r', label='fit params: a=%5.4f, b=%5.4f, c=%5.4f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()