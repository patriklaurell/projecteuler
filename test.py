import functions
import math
import signal
import time

def signal_handler(signal,frame):
    print(s)

def is_cool(n):
    l = [2,3,5,7,11,13,17]
    for i in range(len(l)):
        if int(n[i+1:i+4]) % l[i] is not 0:
            return False
    return True

def main():
    signal.signal(signal.SIGINT, signal_handler)

    start_time = time.time()

    global s
    s = "0123456789"

    sum = 0
    for i in range(math.factorial(10)):
        if(is_cool(s)):
            sum = sum + int(s)
        s = functions.next_perm(s)
    
    print(sum)
    print("Runtime: {}".format(time.time() - start_time))

if __name__ == "__main__":
    main()
