N = 4
check =[]
posi = []

def setCheck(i,j,val):
    if val == 1:
        posi.append([i,j])
    else:
        posi.pop()
    check[i][j] = val

    if i == N-1:
        raise('Hah found')

    # STRAIGHT down
    ii, jj = i+1, j
    while 0 <= ii < N:
        check[ii][jj] = val
        ii, jj = ii+1, jj

    # LEFT diagonal
    ii, jj = i+1, j-1
    while 0 <= ii < N and 0 <= jj < N:
        check[ii][jj] = val
        ii, jj = ii+1, jj-1

    # RIGHT diagonal
    ii, jj = i+1, j+1
    while 0 <= ii < N and 0 <= jj < N:
        check[ii][jj] = val
        ii, jj = ii+1, jj+1

def nQueen(i):
    for j in range(N):
        if check[i][j] == 0:
            setCheck(i,j,1)
            nQueen(i+1)
            setCheck(i,j,0)


if __name__ == "__main__":
    check = [[0 for i in range(N)] for j in range(N)]
    try:
        for j in range(N):
            setCheck(0,j,1)
            nQueen(1)
            setCheck(0,j,0)
        print("Not found")
    except:
        print("Found")
        print(posi)
