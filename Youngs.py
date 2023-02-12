import numpy as np
from scipy.optimize import curve_fit

# Define the function to be fit
def func(x, C):
    dy2dx2 = np.gradient(np.gradient(y, x), x)
    return C - dy2dx2 / 5.29440258863427


# Load the data from a file or define it manually
data = np.loadtxt('young.dat')
x = data[:, 0]
y = data[:, 1]

# Perform the curve fit
popt, pcov = curve_fit(func, x, y)

# Extract the fitted parameters
C_fit = popt[0]

# Print the result
print("The Young's modulus C = {:.4f}".format(C_fit))
print("Good Luck !! Have a nice Day")
