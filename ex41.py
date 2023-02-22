import signal
import sys
import time
from math import sqrt

def main():
    start_time = time.time()
    #Connect signal handler
    signal.signal(signal.SIGINT, signal_handler)

    prime_list = generate_primes()

    global number
    number = 7654321
    while True:
        if is_prime(prime_list,number):
            print("{} is prime".format(number))
            break
        prev_number = number
        number = prev_perm(number)
        if number==int("".join(sorted(str(number)))) and prev_number==number:
            number = int(str(number)[:-1][::-1])
            print("Changed number to {}. Previous number = {}".format(number, prev_number))
            
    print("ans = {}".format(number))
    print("Runtime = {} seconds".format(time.time() - start_time))
        
def prev_perm(num):
    num = str(num)
    exist_prev_perm = False
    for i in range(len(num)-2,-1,-1):
        if num[i] > num[i+1]:
            exist_prev_perm = True
            break
    if i == 0 and exist_prev_perm is not True:
        return int(num)
    for j in range(len(num)-1,-1,-1):
        if num[j] < num[i]:
            break
    tmp = [x for x in num]
    tmp[i], tmp[j] = tmp[j], tmp[i]
    num = "".join(tmp)
    num = num[:i+1]+num[i+1:][::-1]
    return int(num)
    
def is_prime(prime_list,num):
    for i in prime_list:
        if i > sqrt(num):
            break
        if num%i==0:
            return False
    return True

def generate_primes():
    prime_list = [2]
    for i in range(3,31426):
        i_is_prime = True
        for j in prime_list:
            if i%j == 0:
                i_is_prime = False
                break
        if i_is_prime:
            prime_list.append(i)
    return prime_list

def signal_handler(signal,frame):
    print(number)

if __name__ == "__main__":
    main()
