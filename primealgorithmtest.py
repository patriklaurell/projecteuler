import time
import sys
import signal
from functions import list_of_primes
from math import sqrt

def main():
    signal.signal(signal.SIGINT,signal_handler)
    
    n = int(sys.argv[1])
    start_time = time.time()
    #print(alg1(n))
    print(time.time() - start_time)

    start_time = time.time()
    print(alg2(n))
    print(time.time() - start_time)
    
    return

def is_prime(n):
    if n%2==0:
        return False
    for i in range(3,int(sqrt(n)),2):
        if n%i==0:
            return False
    return True

def alg2(n):
    primes = list_of_primes(int(sqrt(n)))
    for i in primes:
        if n%i==0:
            return False
    return True

def signal_handler(signal, frame):
    print("\n{}".format(float(i)/float(x)))

if __name__ == "__main__":
    main()
