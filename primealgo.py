import time

start_time = time.time()

N = 200000

l = list(range(2,N))

i = 0
while True:
    if i > len(l)-1:
        break
    num = l[i]
    p = num**2
    if p > N:
        break
    for j in range(p,N,num):
        if j in l:
            l.remove(j)
    i = i + 1

print(l)
print("Runtime: {} seconds".format(time.time() - start_time))

