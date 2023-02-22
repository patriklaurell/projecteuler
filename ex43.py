import functions
import math
import signal
import time

def main():
    signal.signal(signal.SIGINT, signal_handler)

    version2()
    
    
    return

def version1():
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

def is_cool(n):
    l = [2,3,5,7,11,13,17]
    for i in range(len(l)):
        if int(n[i+1:i+4]) % l[i] is not 0:
            return False
    return True

def version2():
    out = [str(x) for x in range(0,999,17) if len(str(x))==3 and no_rep_digits(str(x))]
    print(out)
    l = [13,11,7,5,3,2]
    for n in l:
        x = [str(x) for x in range(0,999,n) if len(str(x))==3 and no_rep_digits(str(x))]
        print(x)
        tmp = []
        for a in out:
            for b in x:
                if a[:2] == b[1:]:
                    tmp.append(b[0]+a)
        out = tmp
        print(out)
    tmp = []
    for i in out:
        if no_rep_digits(i):
            tmp.append(i)
    print(tmp)
    return

def no_rep_digits(n):
    if len(n)==3:
        if n[0]==n[1] or n[0]==n[2] or n[1]==n[2]:
            return False
        return True
    else:
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if n[i]==n[j]:
                    return False
        return True
def signal_handler(signal,frame):
    print(i)

if __name__ == "__main__":
    main()

