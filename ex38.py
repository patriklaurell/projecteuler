
def main():
    print("ans = {}".format(bla()))
    return

def bla( ):
    l = [1,2,3,4,5,6,7,8,9]

    pandigitals = []

    while len(l) > 1:
        x = 1
        while True:
            s = "".join([str(x*i) for i in l])
            if len(s) > 9:
                l = l[:-1]
                break
            if is_pandigital(int(s)):
                print(int(s))
                pandigitals.append(int(s))
                print("l = {}".format(l))
                
            
            x = x + 1
        
    return max(pandigitals)
            
            
def is_pandigital(x):
    return sorted([int(i) for i in str(x)]) == [1,2,3,4,5,6,7,8,9]
    
            
if __name__ == "__main__":
    main()
