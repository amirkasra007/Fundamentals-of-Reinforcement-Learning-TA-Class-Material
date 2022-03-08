from math import exp
import numpy as np

def randsoftmax(z, N):
    exp_weights = []
    for i in range(len(z)):
        exp_weights.append(exp(z[i]))
    
    sum_exp_wights = sum(exp_weights) 
    for j in range(len(exp_weights)):
        exp_weights[j] = exp_weights[j]/sum_exp_wights

    x = np.random.choice(z,N, replace=True, p=exp_weights)
    return x, exp_weights