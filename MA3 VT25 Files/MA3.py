""" MA3.py

Student:Mika Holst Norin
Mail:mikaholstnorin@gmail.com
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import numpy as np
import math as m
from math import pi,gamma
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc
import functools

def approximate_pi(n): # Ex1
    #for i in range(n):
    XCirk = []
    YCirk = []
    XRekt = []
    YRekt = []
    Hela=[]
    x = np.random.uniform(-1,1,n)
    y = np.random.uniform(-1,1,n)
    for i in range(n):
        if ((x[i])**2 +(y[i])**2)<=1:
            XCirk.append(x[i])
            YCirk.append(y[i])
        else:
            XRekt.append(x[i])
            YRekt.append(y[i])
    r=4*len(XCirk)/n
    print(type(r))
    return r

    #plt.scatter(XCirk,YCirk,color='r')
    #plt.scatter(XRekt,YRekt,color='b')
    #plt.scatter(x,y,color='tab:pink')
    #plt.show()

    #y1 = np.random.uniform(low=0.5, high=1, size=(50,))
    #for i in range(n):
    
    #plt.scatter(x1,y1,color='r')
    #plt.scatter(x2,y2,color='b')
    
    

def sphere_volume(n, d): #Ex2, approximation
    #generar punkter
    points=[[np.random.uniform(-1,1) for ii in range(d)] for jj in range(n)]
    
    #metod 1
    najs = [functools.reduce(lambda x,y:x+y,[points[ii][jj]**2 for jj in range(d)]) for ii in range(n)]
    Inside=list(filter(lambda x: x<=1,najs))
    ratio=(len(Inside))/n
    Volym_S=(2**d)*ratio
    return Volym_S


    #metod 2
    # p = 0
    # klar=0
    # for i in range(n):
    #     p=0
    #     for j in range(d):
    #         p+=(points[i])**2
    #     if p <=1:
    #         klar+=1
    # print(f'antalet innaför sfären är {klar}')
    # print(f'Volumen är ungefär: {(2**d)*klar/n}')
            

def hypersphere_exact(d): #Ex2, real value
    # d is the number of dimensions of the sphere 
    V = lambda d:(pi**(d/2))/gamma(d/2+1)
    return V(d)

#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=10):
    Number_Poi = [n]*np
    Dimension = [d]*np
    with future.ProcessPoolExecutor() as ex:
        result = ex.map(sphere_volume,Number_Poi,Dimension)
    result = list(result)
    return mean(result)
        

#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=10):
    Number_Poi = [n//np]*np
    Dimension = [d]*np
    with future.ProcessPoolExecutor() as ex:
        result = ex.map(sphere_volume,Number_Poi,Dimension)
    result = mean(list(result))
    return result
    

    
def main():
    #Ex1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)
    #Ex2
    n = 100000
    d = 2
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    n = 100000
    d = 11
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    #Ex3
    n = 100000
    d = 11
    avarage=[]
    start = pc()
    for y in range (10):
        avarage.append(sphere_volume(n,d))
    print(sum(avarage)/10)
    stop = pc()
    print(f"Ex3: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    #Ex4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    
def annan():
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")
    n = 100000
    d = 11
    start = pc()
    sphere_volume_parallel2(n,d)
    end = pc()
    print(f'tiden blev {end-start}')

if __name__ == '__main__':
	annan()
