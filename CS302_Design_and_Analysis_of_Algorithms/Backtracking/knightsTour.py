max = 6
min = 0
cells = max*max

def prepareJump(i,j,visit,path,count):
    if visit[i][j] == False:
        visit[i][j] = True
        path.append([i,j])
        #print(count)
        count += 1
        jump(i,j,visit,path,count)
        if count<=cells:
            visit[i][j] = False
            path.pop()
            count -= 1
        else:
            raise Exception("Hah Found")

def jump(i,j,visit,path,count):
    if count <= cells:
        if 0 <= i-2 < max  and min <= j-1 <max:
            prepareJump(i-2,j-1,visit,path,count)

        if min <= i-1 < max   and min <= j-2 <max:
            prepareJump(i-1,j-2,visit,path,count)

        if min <= i+1 < max  and min <= j-2 <max:
            prepareJump(i+1,j-2,visit,path,count)

        if min <= i+2 < max  and min <= j-1 <max:
            prepareJump(i+2,j-1,visit,path,count)

        if min <= i+1 < max  and min <= j+2 <max:
            prepareJump(i+1,j+2,visit,path,count)

        if min <= i+2 < max  and min <= j+1 <max:
            prepareJump(i+2,j+1,visit,path,count)

        if min <= i-2 < max  and min <= j+1 <max:
            prepareJump(i-2,j+1,visit,path,count)

        if min <= i-1 < max  and min <= j+2 <max:
            prepareJump(i-1,j+2,visit,path,count)
    else:
        raise Exception("Hah found")


if __name__ == "__main__":
    visit = [[False for x in range(max)] for y in range(max)]
    path = [[0,0]]
    visit[0][0] = True
    count = 1
    try:
        jump(0,0,visit,path,count)
    except:
        print(path)
    if count >= cells:
        print("Path found")
        print(path)
    else:
        print(path)
        print("Not possible")
