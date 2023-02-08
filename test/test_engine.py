import sys
sys.path.append("./src")
# sys.setrecursionlimit(10000)
import data_utils
from num import NUM
from sym import SYM
from data import DATA
import utils
import main
from egs import Egs


# stdoutOrigin = sys.stdout 
# sys.stdout = open("./etc/out/test_engine.out", "w", encoding="utf-8")

help = '''
cluster.lua : an example csv reader script
USAGE: cluster.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump    on crash, dump stack   = false
  -f  --file    name of file           = ./etc/data/repgrid1.csv
  -F  --Far     distance to "faraway"  = 0.95
  -g  --go      start-up action        = data
  -h  --help    show help              = false
  -m  --min     stop clusters at N^min = 0.5
  -p  --p       distance coefficient   = 2
  -s  --seed    random number seed     = 937162211
  -S  --Sample  sampling data size     = 512
ACTIONS:
'''

the = main.cli(main.settings(help))

tester = Egs(help)


def test1(): #the
    # utils.oo(the)
    print(the)

def test2(): #copy
    t1={'a':1,'b':{'c':2,'d':[3]}}
    t2=utils.copy(t1)
    t2['b']['d'][0] = 10000
    print("b4 {} \nafter {}".format(t1, t2))

def test3(): #sym
    sym =SYM(None, None)
    l = ['a','a','a','a','b','b','c']
    for i in l:
        sym.add(i)
    return "a" == sym.mid() and 1.379 == utils.rnd(sym.div(), None)

def test4(): #num
    num = NUM(None, None)
    l = [1,1,1,1,2,2,3]
    for n in l:
        num.add(n)
    return 11/7 == num.mid() and 0.787 == utils.rnd(num.div(), None)

def test5(): #repcols
    cols = utils.dofile(the['file'])['cols']
    t = data_utils.repCols(cols)

    for col in t.cols.all:
        utils.oo(col)
    for row in t.rows:
        utils.oo(row)

def test6(): #synonyms
    cols = utils.dofile(the['file'])['cols']
    t = data_utils.repCols(cols)
    # print()
    node = t.cluster()
    utils.show(node)

def test7(): #reprows
    t = utils.dofile(the['file'])
    rows = data_utils.repRows(t,utils.transpose(t['cols']))
    for col in rows.cols.all:
        utils.oo(col)
    for row in rows.rows:
        utils.oo(row)

def test8(): #prototypes
    t = utils.dofile(the['file'])
    rows = data_utils.repRows(t,utils.transpose(t['cols']))
    utils.show(rows.cluster(),"mid",rows.cols.all,1)

def test9(): #position
    t = utils.dofile(the['file'])
    rows = data_utils.repRows(t,utils.transpose(t['cols']))
    rows.cluster()
    data_utils.repPlace(rows)

def test10(): #every
    data_utils.repgrid(the['file'])


tester.eg("the", "show settings", test1)
tester.eg("copy", "check copy", test2)
tester.eg("sym", "check syms", test3)
tester.eg("num", "check nums", test4)
tester.eg("repcols", "checking repcols", test5)
tester.eg("synonyms", "checking repcols cluster", test6)
tester.eg("reprows", "checking reprows", test7)
tester.eg("prototypes", "checking reprows cluster", test8)
tester.eg("position", "where's wally", test9)
tester.eg("every", "the whole enchilada", test10)

main.main(the, tester.help, tester.egs)

# sys.stdout.close()
# sys.stdout = stdoutOrigin
