lst = [ii**2 for ii in range(1,3)]
#print(lst)
import math
import numpy as np
prutt=[math.gamma(ii) for ii in range(1,9)]
#print(prutt)
def prutt(x):
    f=lambda x:x+1
    return f(x)
#print(prutt(4))
lista1=[1,2,3]
lista2=[2,3,4]
lista3=[3,4,5]
tuple(map(lambda x,y:x+y,lista1,lista2))
listt=((0,1),(3,4))
#print(list(map(list,listt)))
import functools
lst=[1,1,-1,1]
#print(list(map(abs,lst)))
lista = [1,2,3,4]
n=4
points = np.random.uniform(-1,1,n).round(2)
#print(points)
#print([round(ii,2) for ii in list(map(lambda x:x**2,points))])
a=[7,1,-3,4]
r =list(filter(lambda x: x>2, a))
#print(r)
tal = [1,2,3]
tal2 = [4,5,6]
tal3= [7,8,9]
zip_tal=list(zip(tal,tal2,tal3))
#print(zip_tal)
d = 2
n = 10
s=[[np.random.uniform(-1,1) for ii in range(d)] for jj in range(n)]
print(s)


