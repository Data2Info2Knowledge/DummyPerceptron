import numpy as np

# Calculate target function f as position above/below line
def f_targ(x, y, slope, intcpt):
  line_eqn=slope * x + intcpt
  return np.sign(line_eqn-y)