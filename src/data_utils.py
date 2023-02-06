import utils
from data import DATA

def repCols(cols):
    cols = utils.copy(cols)
    for _,col in enumerate(cols):
        col[len(col)-1] = col[0] + ":" + col[len(col)-1]
        for j in range(1,len(col)):
            col[j-1]=col[j]
        # col[len(col)-1]=None
        col.pop()
    processed_cols1 = []
    for i in range(len(cols[1])-1):
        processed_cols1.append("Num{}".format(i+1))
    processed_cols1.append('thingX')
    cols.insert(0, processed_cols1)
    return DATA(cols)

def repRows(t,rows):
    rows = utils.copy(rows)
    for j,s in enumerate(rows[-1]):
        rows[0][j]=str(rows[0][j])+":"+str(s)
    rows.pop()
    for n,row in enumerate(rows):
        if(n==0):
            row.append("thingX")
        else:
            u=t["rows"][len(t["rows"])-n]
            row.append(u[len(u)-1])
    
    return DATA(rows)

def repgrid(sFile):
    t = utils.dofile(sFile)
    rows = repRows(t, utils.transpose(t['cols']))
    cols = repCols(t['cols'])
    utils.show(rows.cluster(),"mid",rows.cols.all,1)
    utils.show(cols.cluster(),"mid",rows.cols.all,1)
    repPlace(rows)

def repPlace(data):
    n=20
    g={}
    for i in range(1,n+1):
        g[i]={}
        for j in range(1,n+1):
            g[i][j]=" "

    maxy=0
    print("")
    for r,row in enumerate(data.rows):
        c=chr(97+r).upper()
        print(c,utils.last(row.cells))
        x=int(row.x*n/1)
        y=int(row.y*n/1)
        maxy=max(maxy,y+1)
        g[y+1][x+1]=c
    print("")
    for y in range(1,maxy+1):
        print(" ".join(g[y].values()))