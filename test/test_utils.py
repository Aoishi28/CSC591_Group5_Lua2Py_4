import sys
sys.path.append("./src")

import utils
import the 

file = the.file
d = utils.dofile(file)
print(type(d))
print(d['domain'])