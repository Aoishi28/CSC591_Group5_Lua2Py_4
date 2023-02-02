import math
import re
from data import DATA

def transpose(t):
    u=[]
    for i in range(1,len(t[1])+1):
        u[1]=[]
        for j in range(1,len(t)+1):
            u[i][j]=t[j][i]

    return u

def repCols(cols):
    cols=copy(cols)
    for _,col in enumerate(cols):
        col[len(col)] = str(col[1])+":"+str(col[len(col)])
        for j in range(2,len(col)+1):
            col[j-1]=col[j]
        col[len(col)]=None
    cols.insert(1, kap(cols[1], lambda k, v: "Num" + str(k)))
    cols[1][len(cols[1])]="thingX"
    return DATA(cols)

def repRows(t,rows,u):
    rows=copy(rows)
    for j,s in enumerate(rows[len(rows)]):
        rows[1][j]=str(rows[1][j])+":"+str(s)
    rows[len(rows)] = None
    for n,row in enumerate(rows):
        if(n==1):
            row.append("thingX")
        else:
            u=t.rows[len(t.rows)-n+2]
            row.append(u[len(u)])
    
    return DATA(rows)

def repPlace(data):
    n=20
    g=[]
    for i in range(1,n+2):
        g[i]=[]
        for j in range(1,n+2):
            g[i][j]=" "

    maxy=0
    print("")
    for r,row in enumerate(data.rows):
        c=chr(64+r)
        print(c,last(row.cells))
        x=int(row.x*n/1)
        y=int(row.y*n/1)
        maxy=max(maxy,y+1)
        g[y+1][x+1]=c
    print("")
    for y in range(1,maxy+1):
        print(g[y])

def repgrid(sFile):
    t=exec(open(sFile).read())
    rows=repRows(t,transpose(t.cols))
    cols=repCols(t.cols)
    show(rows.cluster())
    show(cols.cluster())
    repPlace(rows)


def show(node,what,cols,nPlaces,lvl=0):
    '''
    prints the tree generated from `DATA:tree`
    '''
    if(node):
        if(lvl):
            lvl=lvl
        else:
            lvl=0

    if node:
        print("| " * lvl + str(len(node["data"].rows)) + "  ")
        if('left' not in node.keys() or lvl==0):
            print (node["data"].stats("mid",node["data"].cols.y,nPlaces)) 
        else:
            print("")
        show(node.get("left"), what,cols, nPlaces, lvl+1)
        show(node.get("right"), what,cols,nPlaces, lvl+1)

seed = 937162211    
# Utility function for numerics
def rint(lo = None, hi = None):
    return math.floor(0.5+rand(lo,hi))

def rand(lo = None, hi = None):
    global seed
    if(lo is None):
        lo=0
    if(hi is None):
        hi=1
    seed=(16807*seed)%2147483647
    return lo+(hi-lo)*seed/2147483647


def rnd(n,nPlaces):
    if(nPlaces is None):
        nPlaces=3
    mult=math.pow(10,nPlaces)
    return math.floor(n*mult+0.5)/mult

def cosine(a,b,c):
    '''
    find x,y from a line connecting `a` to `b`
    '''
    c2 = 1 if c == 0 else 2*c
    x1= (a**2+c**2 -b**2)/(c2)
    x2=max(0,min(1,x1))
    y=abs((a**2-x2**2))**0.5
    return x2,y

# Utility functions for lists

# map a function fun(v) over list (skip nil results)
def map( t, fun):
    u = []
    for k,v in enumerate(t):
        o = fun(v)
        v,k = o[0], o[1]
        if k != 0:
            u[k] = v
        else:
            u[1+len(u)] = v  
    return u

# map function fun(k,v) over list (skip nil results)
def kap( t, fun):
    u = []
    for k,v in enumerate(t):
        o = fun(k,v)
        v,k = o[0], o[1]
        if k != 0:
            u[k] = v
        else:
            u[1+len(u)] = v  
    return u

# sort the list with given comparator
def sort( t, fun):
    return sorted(t, key = fun)

# return a function that sorts ascending on 'x'
def lt(x):
    return lambda a,b: a[x]<b[x]

# return sorted list of keys of given list
def keys( t):
    return sort(kap(t,lambda k,_:k))

# returns one items at random
def any(t):
    return t[rint(len(t)-1)]

# return some items from 't'
def many(t,n):
    u=[]
    for i in range(1,n+1):
        u.append(any(t))
    return u

def last(t):
    return t[len(t)]

def copy(t):
    if type(t)!=list:
        return t
    u=kap(t, lambda k,v : copy(v),copy(k))
    return ..... # to be edited

# Utility functions for Strings

def o(t, isKeys = None):
    if type(t)!=list:
        return str(t)
    def fun(k,v):
        if str(k).find('^_') == -1:
            return ':{} {}'.format(o(k), o(v))

    if (len(t)>0 and not isKeys):
        return '{' + ' '.join(str(item) for item in map(t,o)) + '}'
    else:
        return '{' + ' '.join(str(item) for item in kap(t,fun)) + '}'



def coerce( s):
    def fun(s1):
        if(s1=='true'):
            return True
        elif(s1=='false'):
            return False
        return s1
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return fun(re.search('^\s*(.+?)\s*$',s).group((1)))
    except Exception as e:
        print("Error 101 : corece_file_crashed")



def oo(t):
    # print(o(t))
    return t