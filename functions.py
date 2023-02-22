
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

def next_perm(num):
    num = str(num)
    exists_next_perm = False
    for i in range(len(num)-2,-1,-1):
        if num[i] < num[i+1]:
            exists_next_perm = True
            break
    if i == 0 and exists_next_perm is not True:
        return int(num)
    for j in range(len(num)-1,-1,-1):
        if num[j] > num[i]:
            break
    tmp = [x for x in num]
    tmp[i], tmp[j] = tmp[j], tmp[i]
    num = "".join(tmp)
    num = num[:i+1]+num[i+1:][::-1]
    return str(num)

def list_of_primes(N):
    N = N - 2

    marked = [0] * N
    while True:
        for (i,x) in enumerate(marked):
            if x == 0:
                num = i + 2
                marked[i] = 2
                break
        p = num**2
        if p > N:
            break  
        while p < N+2:
            marked[p-2] = 1
            p = p + num
                
    return [i+2 for i in range(len(marked)) if marked[i] is not 1]
