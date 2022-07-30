

#Root finding by Newton-Raphson method

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import sys

def f(x):
    return np.tan(x)+4*x
def g(x):
    return 1/(np.cos(x)**2)+4

#Plotting the given function
x=np.linspace(-5,5,100)
plt.plot(x,f(x))
plt.plot(x,g(x))
plt.grid(True)
plt.show()

iterative_counter=0
a=float(input("Enter the initial point: "))
tol=float(input("Enter the tolerance: "))

while(abs(f(a))>tol and iterative_counter<50):
    a=a-float(f(a))/g(a)
    if abs(g(a))<1.0e-4:
        print("The error Dreivative is very small: ",a)
        sys.exit()
    iterative_counter+=1
if iterative_counter>0:
    print("The no.of iterations: ",iterative_counter)
    print("solution is: ",a)
else:
    print("solution is not found")
# scipy solution
print("Root by Newton-Raphson method scipy module")
print(opt.newton(f,a))
