# Checks weather x & y are in same cluster
def isSameCluster(x,y,clusters):
    for u in clusters:
        if x in u and y in u:
            return True
    return False

# Checks weather only x or y in cluster
def isSingleCluster(x,y,clusters):
    count = 0
    for u in clusters:
        if x in u or y in u:
            count += 1
    if count == 1:
        return True
    return False

# Checks weather x & y are in different cluster
def isDiffCluster(x,y,clusters):
    isX = False
    isY = False
    for u in clusters:
        if x in u and y not in u:
            isX = True
        if y in u and x not in u:
            isY = True
    if isX and isY:
        return True
    return False

# Find the clusters to be merged
def findClusters(x,y,clusters):
    for i,u in enumerate(clusters):
        if x in u:
            c1 = i
        if y in u:
            c2 = i
    return c1, c2

# Find the cluster with x or y
def findCluster(x,y,clusters):
    for i, u in enumerate(clusters):
        if x in u:
            c1 = i
        if y in u:
            c1 = i
    return c1

# Minimum spanning tree using kruskals algo
def minSpanningTree(n,edges):
    spanTree = []
    clusters = []
    for x,y,z in edges:
        if isSameCluster(x,y,clusters):
            continue
        elif isDiffCluster(x,y,clusters):
            c1, c2 = findClusters(x,y,clusters)
            # mergeing two clusters c1 & c2
            if c1 > c2:
                temp = c1
                c1 = c2
                c2 = temp
            temp = clusters.pop(c2)
            for ele in temp:
                clusters[c1].append(ele)
        # Expanding cluster
        elif isSingleCluster(x,y,clusters):
            c1 = findCluster(x,y,clusters)
            if x in clusters[c1]:
                clusters[c1].append(y)
            else:
                clusters[c1].append(x)
        # New cluster
        else:
            clusters.append([x,y])
        spanTree.append([x,y,z])
    return spanTree

if __name__ == '__main__':
    edges = [[int(x) for x in y.split(' ')]for y in input().split(',')]
    N = len(edges)

    # bubble sort
    for i in range(N):
        for j in range(N-1-i):
            if edges[j][2] > edges[j+1][2]:
                temp = edges[j]
                edges[j] = edges[j+1]
                edges[j+1] = temp

    # eliminating self loop
    i =0
    for x, y, z in edges:
        if x == y:
            edges.pop(i)
        i += 1

    N = len(edges)

    # eliminating parallel edges
    for i in range(N-1):
        for j in range(i+1,N):
            if edges[i][0] == edges[j][0] and edges[i][1] ==edges[j][1]:
                if edges[i][2] > edges[j][2]:
                    edges.pop(i)
                else:
                    edges.pop(j)
                N -= 1
    spanTree = minSpanningTree(N,edges)
    print(spanTree)

'''
Input
0 1 4,1 2 8,2 3 7,3 4 9,4 5 10,5 6 2,6 7 1,0 7 8,1 7 11,2 8 2,6 8 6,7 8 7,2 5 4,3 5 14

Output
[[6, 7, 1], [5, 6, 2], [2, 8, 2], [0, 1, 4], [2, 5, 4], [2, 3, 7], [1, 2, 8], [3, 4, 9]]
'''
