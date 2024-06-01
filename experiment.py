import random
import math
import pandas as pd
import numpy as np

from utils import plusminusone, affineline
from ML_funcs import f_targ

def run_exp(numpoints):
# Create vector of numpoints random points in [-1,1]x[-1,1]
  x_array = pd.Series(plusminusone() for i in range(numpoints))
  y_array = pd.Series(plusminusone() for j in range(numpoints))
  mydata = {"x1":x_array, "x2":y_array}
  df= pd.DataFrame(mydata)
# Select 2 random points in [-1,1]x[-1,1] and 
# determine equation of line through them
  slope, intcpt = affineline(plusminusone(), plusminusone(), plusminusone(), plusminusone())
# print (f'Slope = {slope:.3f}; intercept = {intcpt:.3f}')

# Initialise weights
  weights = np.array([0., 0., 0.])
# Add column = target function f as position above/below line
  df["y"]=f_targ(df["x1"], df["x2"],slope, intcpt)
# print(df)

  iter_count=0
  for m in range(25):
# Add/update column = hypothesis h
    df["h"] = np.sign(weights[0]+weights[1]*df.x1+weights[2]*df.x2)
# Select a misclassified point
    nb_misclass=len(df[df.h != df.y])
    if nb_misclass < 1: # no misclassified points
      break
    iter_count=iter_count+1
    frac_misclass=nb_misclass/(numpoints-1)
  
    theslice = df[df.h != df.y].sample(n=1)
    vec = theslice.values.tolist()[0]
# Update weights using PLA: w <- w + y_n * x_n
    weights[0] = weights[0] + vec[2]
    weights[1] = weights[1] + vec[2] * vec[0]
    weights[2] = weights[2] + vec[2] * vec[1]

  df["h"] = np.sign(weights[0]+weights[1]*df.x1+weights[2]*df.x2)
#    print(df)
  return(iter_count, frac_misclass)