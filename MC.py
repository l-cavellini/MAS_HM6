import random
import numpy as np
from genericpath import isfile 

N = 1000000 # number of samples to test
R = 200 # number of runs per test
min_k = 2

def simulate_tests(p, k): # generate N individuals and assign infection status
    
    num_tests = 0
    individuals = [random.random() < p for _ in range(N)]
    
    for i in range(0, N, k):
        
        batch = individuals[i:i+k]
        num_tests += 1
        
        if any(batch):
            num_tests += len(batch)
         
    return num_tests

def monte_carlo(p: float, max_size: int):  
    
    if(isfile('expected_values.txt')):
        f = open('expected_values.txt','a') # open file where to wirte the expected values for each k
    else: f = open('expected_values.txt', 'x')
    
    f.write('probability: ' + str(p))
    min = N  
    batch_sizes = range(min_k, max_size) # range of batch sizes to simulate
    
    
    for k in batch_sizes:
        test = 0
        for _ in range(R):
            test += simulate_tests(p, k) # generate the expected values over 200 generations
        test = test/R
        if min > test:
            min = test
            min_k = k
        f.write('\nk: ' + str(k) + ',tests: ' + str(test))
        if k - min_k > 100: # too many iterations without improving
            break
    
    f.write('\n')   
    f.close()    
    print('for prob', p ,'the best batch size is', min_k,'which returned', min, 'tests')
    print('the expected reduction of the wookloan is', N-min)
    
    
ps = [0.1, 0.01, 0.001, 0.0001]
for p in ps:
    monte_carlo(p, int(1/p)*2)

