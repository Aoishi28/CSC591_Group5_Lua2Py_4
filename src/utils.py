import math
import re
import copy as copy_module
import json

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


def rnd(n,nPlaces = None):
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
        v,k = fun(k,v)
        if k != None:
            u[k] = v
        else:
            u.append(v)  
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
    return t[len(t)-1]

def copy(t):
    return copy_module.deepcopy(t)

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



def coerce(s):
    if(s=='true'):
        return True
    elif(s=='false'):
        return False
    elif s.isdigit():
        return int(s)
    elif '.' in s and s.replace('.','').isdigit():
        return float(s)
    else:
        return s



def oo(t):
    # get all the attributes of the object
    object_attributes = t.__dict__
    # get class name of the object
    object_attributes['a'] = t.__class__.__name__
    # get an unique id for the object
    object_attributes['id'] = id(t)
    print(dict(sorted(object_attributes.items())))


def dofile(file):
    with open(file, 'r', encoding = 'utf-8') as f:
        content  = f.read()
        content = re.findall(r'(return\s+[^.]+)', content)[0]
        map = {'return ' : '', '{' : '[', '}' : ']','=':':', '[\n':'{\n', '\n]':'\n}', '_':'"_"', '\'':'"'}
        for k,v in map.items():
            content = content.replace(k, v)
        content = re.sub("(\w+):",r'"\1":',content)
        parsed_json = json.loads(content)
        return parsed_json

def show(node, what = None, cols = None, nPlaces = None, lvl = None):
    if node:
        lvl = lvl if lvl else 0
        print("|.. "*lvl, end = "")
        # if 'left' not in node.keys():
        if not node.get('left'):
            print(node['data'].rows[-1].cells[-1])
        else:
            print("{:.1f}".format(rnd(100*node['c'])))
        show(node.get('left'), what, cols, nPlaces, lvl+1)
        show(node.get('right'), what, cols, nPlaces, lvl+1)

def transpose(t):
    u=[]
    for i in range(len(t[1])):
        u.append([])
        for j in range(len(t)):
            u[i].append(t[j][i])

    return u
