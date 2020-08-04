class Node:
    def __init__(self,data):
        self.data = data
        self.branch = None

class Branch:
    def __init__(self,adj):
        self.adj = adj
        self.next = None
#
# Data structure for spanning tree
class SpanningTree:
    def __init__(self):
        self.next = None

class SNode:
    def __init__(self,data):
        self.data = data
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

# Build spanning tree
def spanningTree(prev,node,visited):
    visited.append(node)
    snode = SNode(node.data)
    prev.next = snode
    #
    bran = node.branch
    while bran != None:
        if bran.adj not in visited:
            snode = spanningTree(snode,bran.adj,visited)
        bran = bran.next
    return snode



sTreeHeader = SpanningTree()

if __name__ == '__main__':
    mat = [[int(x) for x in y.split(' ')] for y in input().split(',')]
    if len(mat) != len(mat[0]):
        print("Invalid input")
        exit()
    N = len(mat)
    graphList = matToGraph(mat,N)
    visited = []
    spanningTree(sTreeHeader,graphList[0],visited)

    temp = sTreeHeader.next
    while temp != None:
        print(temp.data,end=' -> ')
        temp = temp.next

'''
Input
0 1 1 0 1,0 0 0 1 1,0 1 0 1 0,0 0 0 0 0,0 0 0 1 0

Output
0 -> 1 -> 3 -> 4 -> 2 
'''
