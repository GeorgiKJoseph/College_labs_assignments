def constructPiTable(string):
    piTable = []
    # table starts from index 0
    # first entry always 0
    piTable.append(0)
    length = len(string)
    #
    # Constructing table
    i = 1
    while i < length:
        for j in range(0,length):
            if string[j] == string[i]:
                piTable.append(piTable[len(piTable)-1]+1)
            else:
                piTable.append(0)
                i += 1
                break
            i += 1

    return piTable

def kmpPatternMatch(string,substring,piTable):
    patternMatchIndices = []
    i = 0
    j = 0
    while i < len(string):
        if string[i] == substring[j]:
            print(j)
            j += 1
            if j >= len(substring):
                index = i- j+ 1
                patternMatchIndices.append(index)
                j = piTable[j-1]
        else:
            print("else: ", j)
            j = piTable[j-1]+1

        i += 1


    return patternMatchIndices

if __name__=='__main__':
    string = [x for x in input().split(" ")]
    substring = [x for x in input().split(" ")]

    piTable = constructPiTable(substring)
    patternMatchIndices = kmpPatternMatch(string,substring,piTable)
    print(piTable)
    print(patternMatchIndices)


'''
Input
A A A A A A A A A A A A A A A A A B
A A A A B

Output
[13]
'''
