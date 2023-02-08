#!/usr/bin/env python3

__author__ = "NCSU CSC 591 021 Spring 23 Group-3"
__version__ = "1.0.0"
__license__ = "MIT"

from utils import *
from test_hw4 import *

def main():
    saved,fails={},0
    for k,v in cli(settings(help)).items():
        the[k] = v
        saved[k] = v
    if the['help'] == True:
        print(help)
    else:
        for what, fun in egs.items():
            if the['go'] == 'all' or the['go'] == what:
                for k,v in saved.items():
                    the[k] = v
                Seed = the['seed']
                if egs[what]() == False:
                    fails += 1
                    print('❌ fail:', what)
                else:
                    print('✅ pass:', what)
    sys.exit(fails)

if __name__ == '__main__':
    eg('the', 'show settings', test_the)
    eg('copy','check copy', test_copy)
    eg('sym', 'check syms', test_sym)
    eg('num', 'check nums', test_num)
    eg('repcols', 'checking repcols', test_repCols)
    eg('synonyms','checking repcols cluster', test_synonyms)
    eg('reprows','checking reprows', test_repRows)
    eg('prototypes','checking reprows cluster', test_prototypes)
    eg('position','where\'s wally', test_position)
    eg('every','the whole enchilada', test_every)
    main()