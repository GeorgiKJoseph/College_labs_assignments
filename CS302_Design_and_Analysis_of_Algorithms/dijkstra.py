class Node:
    def __init__(self,data):
        self.data = data
        self.branch = None

class Branch:
    def __init__(self,link):
        self.adj = link
        self.next = None

# Make branches
def makeBranch(node,adj):
    bran = Branch(adj)
    end = None
    temp = node.branch
    while temp != None:
        end = temp
        temp = temp.next
    if end == None:
        node.branch = bran
    else:
        end.next = bran

# Build graph from adjacency matrix
def matToGraph(mat,n):
    list = []
    # creating Nodes
    for i in range(N):
        node = Node(i)
        list.append(node)
    # Constructing graph
    for i in range(n):
        for j in range(n):
            if mat[i][j] > 0:
                makeBranch(list[i],list[j])
    return list

# Finding next node based on distance
def nextNode(visited,distance):
    nxt = None
    val = float('inf')
    for i, d in enumerate(distance):
        if val > d and not visited[i]:
            val = d
            nxt = i
    return nxt

# Finding shortest using Dijkstra Algo
def dShortPath(n,start,graphList,distance,visited,mat):
    cur = start
    itCount = n
    while itCount != 0:
        link = graphList[cur].branch
        du = distance[cur]
        while link != None:
            if not visited[link.adj.data]:
                bran = link.adj
                adj = graphList.index(bran)
                weight = mat[cur][adj]
                temp_dis = du + weight
                if temp_dis < distance[adj]:
                    distance[adj] = temp_dis
            link = link.next
        visited[cur] = True
        itCount -= 1
        cur = nextNode(visited,distance)

# Input graph in adjacency matrix form
if __name__ == '__main__':
    mat = [[int(x) for x in y.split(' ')] for y in input().split(',')]
    if len(mat) != len(mat[0]):
        print("Invalid input")
        exit()
    N = len(mat)
    graphList = matToGraph(mat,N)
    start = int(input("Start node: "))
    distance = [float('inf') for m in mat]
    distance[start] = 0
    visited = [False for m in mat]

    dShortPath(N,start,graphList,distance,visited,mat)
    for i in range(N):
        print(start,' -> ',i," = ",distance[i])

'''
Sample input
0 4 0 0 0 0 0 8 0,4 0 8 0 0 0 0 11 0,0 8 0 7 0 4 0 0 2,0 0 7 0 9 14 0 0 0,0 0 0 9 0 10 0 0 0,0 0 4 14 10 0 2 0 0,0 0 0 0 0 2 0 1 6,8 11 0 0 0 0 1 0 7,0 0 2 0 0 0 6 7 0

Output
Start node: 0
0  ->  0  =  0
0  ->  1  =  4
0  ->  2  =  12
0  ->  3  =  19
0  ->  4  =  21
0  ->  5  =  11
0  ->  6  =  9
0  ->  7  =  8
0  ->  8  =  14
'''
