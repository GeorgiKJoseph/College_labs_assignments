import random

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

def topologicalSort(node,visited,stack):
    bran = node.branch
    visited.append(node)
    while bran != None:
        if bran.adj not in visited:
            topologicalSort(bran.adj,visited,stack)
        bran = bran.next
    stack.append(node)


if __name__ == '__main__':
    mat = [[int(x) for x in y.split(' ')] for y in input().split(',')]
    if len(mat) != len(mat[0]):
        print("Invalid Input!")
        exit()

    N = len(mat)
    graphList = matToGraph(mat,N)
    visited = []
    stack = []
    untouched = [x for x in graphList if x not in visited]
    while len(untouched) != 0:
        node = untouched[random.randint(0,len(untouched)-1)]
        topologicalSort(node,visited,stack)
        untouched = [x for x in graphList if x not in visited]

    # Display stack
    while len(stack) != 0:
        ele = stack.pop()
        print(ele.data,end=' -> ')

'''
Input
0 0 1 0 0 0 0 0,0 0 1 1 0 0 0 0,0 0 0 0 1 0 0 0,0 0 0 0 0 1 0 0,0 0 0 0 0 1 1 0,0 0 0 0 0 0 0 1,0 0 0 0 0 0 0 0,0 0 0 0 0 0 0 0

Output
1 -> 3 -> 0 -> 2 -> 4 -> 6 -> 5 -> 7
'''
