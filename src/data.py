from row import ROW
from cols import COLS
import copy
import utils
import math
import the

class DATA:
    def __init__(self, src) -> None:
        self.rows = []
        self.cols = None

        self.total_values = 0


        if type(src) == str:
            self.from_csv(src)
        else:
            self.from_list(src)
    
    def add(self, t) -> None:
        if self.cols :
            # if t.cells != None :
            if type(t) == list:
                t = ROW(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COLS(t)
    
    def clone(self, init = []):
        data = DATA([self.cols.names])
        map(lambda x: data.add(x), init)
        return data

    def stats(self, what, cols, nPlaces):
        ret = dict()
        if cols == None:
            cols = self.cols.y

        if what == "mid":
            for col in cols :
                ret[col.txt] = col.rnd(col.mid(), nPlaces)
            return ret
        else:
            for col in cols :
                ret[col.txt] = col.rnd(col.div(), nPlaces)
            return ret

    def from_csv(self, src):
        path = src
        with open(path, "r") as csv:
            lines = csv.readlines()
            for line in lines:
                split_line = line.split(",")
                split_line = [utils.coerce(i) for i in split_line]
                self.add(split_line)
                self.total_values += len(split_line)


    
    def from_list(self, lines):
        if lines == None:
            lines = []
        
        for line in lines:
            self.add(line)


    def dist(self, row1, row2, cols = None)->float:
        n, d, ys = 0, 0, None
        
        if cols == None:
            ys = self.cols.x
        else:
            ys = cols
        
        for col in ys:
            n += 1
            d += col.dist(row1.cells[col.at], row2.cells[col.at]) ** the.p
        
        return (d/n)**(1/the.p)

    def around(self, row1, rows = None, cols = None):
        ys = rows if rows != None else self.rows
        processed_ys = []
        for y in ys:
            processed_ys.append((y, self.dist(row1, y, cols)))
        return sorted(processed_ys,key = lambda x:x[1])
    
    def half(self, rows = None, cols = None, above = None):
        
        def dist(row1, row2):
            return self.dist(row1, row2, cols)

        rows = rows if rows != None else self.rows
        A = above if above != None else utils.any(rows)
        B = self.furthest(A, rows)[0]
        c = dist(A, B)
        left, right, mid = [], [], None

        def project(row):
            x,y = utils.cosine(dist(row,A), dist(row,B), c)
            try:
                row.x = row.x
                row.y = row.y
            except:
                row.x = x
                row.y = y
            return (row, x, y)
        
        processed_rows = []
        for row in rows:
            processed_rows.append(project(row))
        
        processed_rows = sorted(processed_rows, key = lambda x:x[1])

        for n,temp in enumerate(processed_rows) :
            if n <len(processed_rows)//2 :
                left.append(temp[0])
                mid = temp[0]
            else:
                right.append(temp[0])
        
        return left, right, A, B, mid, c

    

    def cluster(self, rows = None, cols = None, above = None):
        rows = rows if rows != None else self.rows
        cols = cols if cols != None else self.cols.x
        node = {"data" : self.clone(rows)}
        if len(rows) >= 2:
            left, right, node["A"], node["B"], node["mid"], node["c"] = self.half(rows,cols,above)
            node["left"]  = self.cluster(left, cols, node["A"])
            node["right"] = self.cluster(right, cols, node["B"])
        return node
    

    def furthest(self, row1, rows = None, cols = None):
        t = self.around(row1, rows, cols)
        return t[len(t)-1]

    


    
