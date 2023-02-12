import numpy as np
from scipy.optimize import curve_fit

# Define the function to be fit
def func(x, B):
    dy2dx2 = np.gradient(np.gradient(y, x), x)
    return B - (dy2dx2 * 5.288)

# Load the data from a file or define it manually
data = np.loadtxt('bulk.dat')
x = data[:, 0]
y = data[:, 1]

# Perform the curve fit
popt, pcov = curve_fit(func, x, y)

# Extract the fitted parameters
B_fit = popt[0]

# Print the result
print("The Bulk modulus B = {:.4f}".format(B_fit))
print("Good Luck !! Have a nice Day")


