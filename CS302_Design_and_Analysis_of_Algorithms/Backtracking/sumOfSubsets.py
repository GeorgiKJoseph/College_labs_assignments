check = []
set = []
found = []
N = 0
length = 0

def pushCheck(check):
    if check not in found:
        found.append(check.copy())

def subsetSum(i,s,rs):
    if s == N:
        pushCheck(check)
    if s <= N and s+rs >= N:
        if i < length:
            # s[i] IN
            check[i] = 1
            subsetSum(i+1,s+set[i],rs-set[i])

            # s[i] OUT
            check[i] = 0
            subsetSum(i+1,s,rs-set[i])

def displaySubset():
    for x in found:
        for i, y in enumerate(x):
            if y == 1:
                print(set[i], end=" ")
        print()

if __name__ == "__main__":
    set = [int(x) for x in input().split(" ")]
    check = [0 for x in range(len(set))]
    N = int(input())
    length =len(set)
    subsetSum(0,0,sum(set))
    displaySubset()

'''
Input
5 10 12 13 15 18 
30

Output
5 10 15
5 12 13
12 18
'''
