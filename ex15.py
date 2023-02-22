
def main(n):
    x = 2**(2*n)
    for i in range(1,n+1):
        x = x - (2**i)*2
    print(x)
    return x

if __name__ == "__main__":
    main(20)
    assert main(2) == 6
