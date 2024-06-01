from statistics import mean
from experiment import run_exp

iter_to_conv=[]
prob_misclas=[]
numpoints = 101
for m in range(1001):
  iter_count, frac_misclass = run_exp(numpoints)
  iter_to_conv.append(iter_count)
  prob_misclas.append(frac_misclass)
  print (str(m), end='\r') # display run number, overwriting as we go...

avg_iter = mean(iter_to_conv)
avg_prob = mean(prob_misclas)
print(f'\n Avg # iter. = {avg_iter:.1f} \t Avg P(disagree) = {avg_prob:.3f}')