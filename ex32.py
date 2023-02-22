
def main():
    bla()
    return

def bla():
    pandigitals = []
    for i in range(1,999999):
        for j in range(1,999999):
            checklist = [1,2,3,4,5,6,7,8,9]
            l = [int(x) for x in str(i)] + [int(x) for x in str(j)] + [int(x) for x in str(i*j)]
            if len(l) > 9:
                break
            l.sort()
            if l == checklist and i*j not in pandigitals:
                print("{} * {} = {}".format(i,j,i*j))
                pandigitals.append(i*j)
    print(sum(pandigitals))
            
            
if __name__ == "__main__":
    main()
