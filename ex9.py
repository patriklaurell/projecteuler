import time

time1 = time.time()

from math import sqrt
foobar = False
for a in range(1,500):
    for b in range(1,500):
        c = sqrt(a**2 + b**2)
        if a+b+c == 1000:
            foobar = True
            break
    if foobar:
        break
print("a = {} b = {} c = {}".format(a,b,c))
print(a*b*c)
print("Time: {} seconds".format(time.time()-time1))

time2 = time.time()

print([a*b*(a*a+b*b)**0.5 for a in range(1,1000) for b in range(1,1000) if (a+b+(a*a+b*b)**0.5) == 1000][0])

print("Time: {} seconds".format(time.time()-time2))
