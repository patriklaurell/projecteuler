from math import sqrt
import time

start_time = time.time()

N = 200000000
N = N - 2

marked = [0] * N

while True:
    for (i,x) in enumerate(marked):
        if x == 0:
            num = i + 2
            marked[i] = 2
            break
    p = num**2
    #print("i = {} num = {} marked[i] = {} p = {}".format(i,num,marked[i],p))
    #print(marked)
    if p > N:
        break
   
    while p < N+2:
        marked[p-2] = 1
        p = p + num

primes = [i+2 for i in range(len(marked)) if marked[i] is not 1]

print(sum(primes))

print("Runtime: {} seconds".format(time.time()-start_time))


    

