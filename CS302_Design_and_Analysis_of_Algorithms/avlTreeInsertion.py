class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

class LinkList:
    def __init__(self):
        self.next = None

head = LinkList()
map = []
mini = []

# Binary tree insertion
def insertion(prev,cur,data,child):
    if cur == None and child != None:
        new = Node(data)
        if child == 'r':
            prev.rchild = new
        else:
            prev.lchild = new
    elif cur ==None and child == None:
        new = Node(data)
        head.next = new
    elif data < cur.data:
        map.append('l')
        insertion(cur,cur.lchild,data,'l')
    elif data > cur.data:
        map.append('r')
        insertion(cur,cur.rchild,data,'r')

# Inorder DFS traversal
def traversal(node):
    if node != None:
        print(node.data, end=" ")
        traversal(node.lchild)
        traversal(node.rchild)

# Recursive function to return height from node
def findHeight(node):
    if node != None:
        l = findHeight(node.lchild)
        r = findHeight(node.rchild)
        if l > r:
            return l + 1
        else:
            return r + 1
    return 1

# Check weather L branch and R branch are balanced or not
def balance(node):
    lmax = 0
    rmax = 0
    lmax = findHeight(node.lchild)
    rmax = findHeight(node.rchild)
    return (lmax - rmax)

# Check and convert a btree to avl tree after every insertion
def avlfication(node):
    map_vertices = []
    map_vertices.append(node)
    temp = node
    for x in map:
        if x == 'l':
            map_vertices.append(temp.lchild)
            temp = temp.lchild
        else:
            map_vertices.append(temp.rchild)
            temp = temp.rchild

    temp_map = map.copy()
    reject = []
    while len(map_vertices) != 0:
        temp = map_vertices.pop()
        try:
            prev = map_vertices[len(map_vertices)-1]
            LorR = temp_map.pop()
            reject.append(LorR)
        except:
            prev = head
            LorR = None
        bal = balance(temp)
        if abs(bal) >= 2:
            #
            # Right rotation
            if reject[len(reject)-1] == 'l' and reject[len(reject)-2] == 'l':
                if LorR == 'l':
                    tp = temp.lchild
                    prev.lchild = temp.lchild
                    temp.lchild = temp.lchild.rchild
                    tp.rchild = temp
                elif LorR == 'r':
                    tp = temp.lchild
                    prev.rchild = temp.lchild
                    temp.lchild = temp.lchild.rchild
                    tp.rchild = temp
                else:
                    tp = temp.lchild
                    prev.next = temp.lchild
                    temp.lchild = temp.lchild.rchild
                    tp.rchild = temp
            #
            # Left Rotation
            elif reject[len(reject)-1] == 'r' and reject[len(reject)-2] == 'r':
                if LorR == 'l':
                    tp = temp.rchild
                    prev.lchild = temp.rchild
                    temp.rchild = temp.rchild.lchild
                    tp.lchild = temp
                elif LorR == 'r':
                    tp = temp.rchild
                    prev.rchild = temp.rchild
                    temp.rchild = temp.rchild.lchild
                    tp.lchild = temp
                else:
                    tp = temp.rchild
                    prev.next = temp.rchild
                    temp.rchild = temp.rchild.lchild
                    tp.lchild = temp
            #
            # Left-Right rotation
            elif reject[len(reject)-1] == 'l' and reject[len(reject)-2] == 'r':
                # First rotation
                l = temp.lchild
                r = l.rchild
                temp.lchild = r
                l.rchild = r.lchild
                r.lchild = l
                if LorR == 'l':
                    # Second rotation
                    tp = temp.lchild
                    prev.lchild = temp.lchild
                    temp.lchild = temp.lchild.rchild
                    tp.rchild = temp
                elif LorR == 'r':
                    # Second rotation
                    tp = temp.lchild
                    prev.rchild = temp.lchild
                    temp.lchild = temp.lchild.rchild
                    tp.rchild = temp
                else:
                    tp = temp.lchild
                    prev.next = temp.lchild
                    temp.lchild = temp.lchild.rchild
                    tp.rchild = temp
            #
            # Right-Left rotation
            else:
                #First Rotation
                r = temp.rchild
                l = r.lchild
                temp.rchild = l
                r.lchild = l.rchild
                l.rchild = r
                # Second Rotation
                if LorR == 'l':
                    tp = temp.rchild
                    prev.lchild = temp.rchild
                    temp.rchild = temp.rchild.lchild
                    tp.lchild = temp
                elif LorR == 'r':
                    tp = temp.rchild
                    prev.rchild = temp.rchild
                    temp.rchild = temp.rchild.lchild
                    tp.lchild = temp
                else:
                    tp = temp.rchild
                    prev.next = temp.rchild
                    temp.rchild = temp.rchild.lchild
                    tp.lchild = temp


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        data = int(input())
        map = []
        insertion(head.next,head.next,data,None)
        avlfication(head.next)

    traversal(head.next)
