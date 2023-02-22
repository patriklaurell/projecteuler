import sys

c = [1,2, 5, 10, 20, 50, 100, 200]

def main():
    print("combinations = " + str(numOfCombinations(int(sys.argv[1]),int(sys.argv[2]))))


def numOfCombinations(highestCoin, N):
    coins = c[:highestCoin+1];
    if N == 0:
        return 0;
    if highestCoin == 0:
        return 1;
    x = N % c[highestCoin];
    combs = 0;
    for i in range(0,N//coins[highestCoin]+1):
        combs = combs + numOfCombinations(highestCoin-1, N-i*coins[highestCoin])
    if N % coins[highestCoin] == 0:
        combs = combs + 1
    return combs


if __name__ == "__main__":
    main()
