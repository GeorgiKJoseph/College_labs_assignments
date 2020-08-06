adjm = []
col = []
cur = []
N = 0
found = []

def adjCol(i):
    adj = []
    for j, x in enumerate(adjm[i]):
        if x == 1:
            adj.append(cur[j])

    return adj

def mcolor(i):
    adj = adjCol(i)
    for x in col:
        if x not in adj:
            if i < N:
                cur[i] = x
                if i < N-1:
                    mcolor(i+1)
                if i == N-1:
                    found.append(cur.copy())
                cur[i] = None

if __name__ == "__main__":
    adjm = [[0, 1, 1, 1],[1, 0, 1, 0],[1, 1, 0, 1],[1, 0, 1, 0]]
    N = len(adjm)
    cur = [None for i in range(N)]
    col = ["R","B","G"]

    mcolor(0)
    for x in found:
        print(x)

'''
Output
['R', 'B', 'G', 'B']
['R', 'G', 'B', 'G']
['B', 'R', 'G', 'R']
['B', 'G', 'R', 'G']
['G', 'R', 'B', 'R']
['G', 'B', 'R', 'B']
'''
