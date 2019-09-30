import numpy as np
import pandas as pd
from scipy import optimize

def fobj(x):
  value = 0
  for i in range(len(x)):
      value += x[i]**2
  return value / len(x)

bounds=[(-100, 100)] * 32
ret = optimize.differential_evolution(fobj,bounds, init="latinhypercube", maxiter=200, popsize=50,recombination=0.5)

print("global minimum: x = ",ret.x, "f(x0) = ",ret.fun)