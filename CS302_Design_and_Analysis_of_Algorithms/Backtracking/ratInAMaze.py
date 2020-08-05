N = 4
path = []
maze = []

def move(i,j):
    if i==(N-1) and j==(N-1):
        raise("Hah found it")
    else:
        if i+1 < N and maze[i+1][j] == 1:
            path.append([i+1,j])
            move(i+1,j)
            path.pop()
        if j+1 < N and maze[i][j+1] == 1:
            path.append([i,j+1])
            move(i,j+1)
            path.pop()


if __name__=="__main__":
    maze = [[int(x) for x in y.split(" ")] for y in input().split(",")]
    maze.append([0,0])
    try:
        move(0,0)
        print("Not found")
    except:
        print("Found")
        print(path)

'''
Input
1 0 0 0,1 1 0 1,0 1 0 0,1 1 1 1
Output
[[1, 0], [1, 1], [2, 1], [3, 1], [3, 2], [3, 3]]
'''
