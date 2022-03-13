import numpy as np
import matplotlib.pyplot as plt
from math import exp
from math import sqrt
from math import log

print('Task 6: Confidence Intervals using Hoeffdings Inequality')

##Initialization

alpha=0.05    #Parameter for confidence level
p = 0.4       #probability of heads
n_max = 1000  #maximum sample size
n_runs = 100  #number of samples per sample size


##Simulation Study
#variable for "coverage"
cov=np.zeros((1,n_max))
cov1=np.zeros((1,n_max))
#variable for "length of interval"
lenn=np.zeros((1,n_max))

for i in range(1, n_max+1):

    #n_run random samples, each sample consists of n Bernoulli(p) realizations
    x0 = np.random.choice([0,1],n_runs*i, replace=True, p = [1-p,p]) 

    x = np.reshape(x0, (i, n_runs))
    eps= sqrt(log(2/alpha)/(2*i));  #determine confidence intervals for all runs


    a=np.mean(x, axis = 0)-eps   #lower bound
    b=np.mean(x, axis = 0)+eps   #upper bound

    #determine coverage (relative frequency of confidence interval containing p)
    cov[0,i-1] = np.size(np.nonzero(np.where(a <= p, a, 0)))/n_runs
    cov1[0,i-1] = np.size(np.nonzero(np.where(b >= p, b, 0)))/n_runs
    
    #determine length of confidence interval
    lenn[0,i-1]=2*eps;   

##Plots
bb=[j for j in range(1,n_max,10)]
b_numpy = np.asarray(bb)
plt.scatter(b_numpy, cov[0][1:n_max:10])
plt.xlabel('sample size n')
plt.ylabel('coverage')
plt.title("The relative frequency of confidence interval containing probability p")
plt.grid()
plt.show()


xlabel = [k for k in range(1,1001)]
plt.plot(xlabel,lenn[0])
plt.xlabel('sample size n')
plt.ylabel('length of confidence interval')
plt.grid()
plt.title("The variation of confidence interval length according to sample size")
plt.ylim(0, 1.5)
plt.show()
print('End of task')


