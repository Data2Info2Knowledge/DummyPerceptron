import random

def plusminusone():
#  x = -1.+random.random()*2.
  x = random.uniform(-1.,1.)
  return x

def affineline(xa, ya, xb, yb):
  slope = 0
  try:
    slope = (yb - ya)/(xb - xa)
  except ZeroDivisionError:
    print("Can't divide by zero !")
  intcpt = ya - xa * slope
  return slope, intcpt