import math
from queue import PriorityQueue

def euclid(x,y):
    return math.sqrt((x[0]-y[0])*(x[0]-y[0]) + (x[1]-y[1])*(x[1]-y[1]))

def kelement(l, k):
    x = PriorityQueue()
    for i in range(k):
        x.put((l[i], l[i]))
    for i in range(k, len(l)):
        mini = x.get()
        if l[i] > mini[1]:
            x.put((l[i],l[i]))
        else:
            x.put(mini)
    return x.get()[0]
    
def onetime(cuv):
    words = cuv.split(' ')
    d = {}
    for el in words:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    for el in d.keys():
        if d[el] == 1:
            print(el)

def twovalues(l):
    sum(s) - len(l) * (len(l) - 1) // 2

def lastword(l):
    words = l.split(' ')
    maxi = ''
    for el in words:
        if maxi == '' or maxi < el:
            maxi = el
    return maxi
            

print(euclid([1,5],[4,1]))
onetime('ana are ana are mere rosii')
print(kelement([7,10,8,9,3,1],2))
print(lastword('Ana are mere rosii si galbene'))
