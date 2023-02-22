from math import sqrt

def main():
    d = {i:0 for i in range(1,1001)}
    for a in range(1,1000):
        for b in range(1,1000):
            c = sqrt(a**2 + b**2)
            if a+b+c > 1000:
                break
            c = int(c)
            if c**2 == a**2 + b**2:
                sum = a+b+c
                d[sum] = d[sum] + 1

    max = 0
    for i in range(1,1000):
        if d[i] > max:
            max = d[i]
            index = i

    print("{}: {}".format(index,d[index]))
    return


if __name__ == "__main__":
    main()
