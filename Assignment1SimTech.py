#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 20:08:21 2019

@author: jacquelynschreck
"""
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sobol_seq



"""Part 1.4"""


class escalator():

    def __init__(self, n, sp, d, c, s):
        self.name = n
        self.speed = sp
        self.direction = d
        self.capacity = c
        self.safety = s


    def __str__(self, n, sp, d, c, s):
        escalator.__int__(self, n, sp, d, c, s)
            

    def speed(self):
        if self.constant:
            print ("The escalator speed does not change throughout the day.")
        if self.changing:
            print("The speed of the escaltor changes at different times of the day.")
        
        
    def direction(self):
        if self.up:
            print("The escalator is ascending.")
        if self.down:
            print("The escalator is descending.")
        

    def capacity(self):
        if self.max:
            print("Max capacity.")
        

    def safety(self):
        if self.walkingetiquette:
            print("Walking etiquette followed.")
        if self.brake:
            print("Emergency brake active.")
        if self.sensor: 
            print("Escalator sensors running")









"""Part 3.1"""



assign1 = pd.read_csv('/users/jacquelynschreck/desktop/assign1.csv')
station1 = pd.read_csv('/users/jacquelynschreck/desktop/Station1.csv')
station2 = pd.read_csv('/users/jacquelynschreck/desktop/Station2.csv')
station3 = pd.read_csv('/users/jacquelynschreck/desktop/Station3.csv')
station4 = pd.read_csv('/users/jacquelynschreck/desktop/Station4.csv')
station5 = pd.read_csv('/users/jacquelynschreck/desktop/Station5.csv')


print(np.std(assign1))
print(np.std(station1))
print(np.std(station2))
print(np.std(station3))
print(np.std(station4))
print(np.std(station5))


print(np.mean(assign1))
print(np.mean(station1))
print(np.mean(station2))
print(np.mean(station3))
print(np.mean(station4))
print(np.mean(station5))


"""Means Wait"""

MeansPeople = pd.DataFrame({
    'Station':['1','2','3','4','5'],
    'People':[4700,3140,1560,2320,3040],
})
MeansPeople.plot(kind='bar',x='Station',y='People')




"""Means People"""

MeansWait = pd.DataFrame({
    'Station':['1','2','3','4','5'],
    'Wait':[16,19.4,14.2,9.2,11.2],
})
MeansWait.plot(kind='bar',x='Station',y='Wait')


assign1[0:25].plot(
    x='Day', 
    y='Wait', 
    kind='bar', 
    legend=False, 
    color='blue',
    width=0.8)
plt.title('Overall')
plt.ylabel('Wait')

assign1[0:25].plot(
    x='Day', 
    y='People', 
    kind='bar', 
    legend=False, 
    color='blue',
    width=0.8)
plt.title('Overall')
plt.ylabel('People')


station1[0:5].plot(
    x='Day', 
    y='Wait', 
    kind='bar', 
    legend=False, 
    color='blue',
    width=0.8)
plt.title('Station One')
plt.ylabel('Wait')

station1[0:5].plot(
    x='Day', 
    y='People', 
    kind='bar', 
    legend=False, 
    color='blue',
    width=0.8)
plt.title('Station One')
plt.ylabel('People')


station2[0:5].plot(
    x='Day', 
    y='Wait', 
    kind='bar', 
    legend=False, 
    color='blue',
    width=0.8)
plt.title('Station Two')
plt.ylabel('Wait')


station2[0:5].plot(
    x='Day', 
    y='People', 
    kind='bar', 
    legend=False, 
    color='blue',
    width=0.8)
plt.title('Station Two')
plt.ylabel('People')


station3[0:5].plot(
    x='Day', 
    y='Wait', 
    kind='bar', 
    legend=False, 
    color='blue',
    width=0.8)
plt.title('Station Three')
plt.ylabel('Wait')


station3[0:5].plot(
    x='Day', 
    y='People', 
    kind='bar', 
    legend=False, 
    color='blue',
    width=0.8)
plt.title('Station Three')
plt.ylabel('People')


station4[0:5].plot(
    x='Day', 
    y='Wait', 
    kind='bar', 
    legend=False, 
    color='blue',
    width=0.8)
plt.title('Station Four')
plt.ylabel('Wait')


station4[0:5].plot(
    x='Day', 
    y='People', 
    kind='bar', 
    legend=False, 
    color='blue',
    width=0.8)
plt.title('Station Four')
plt.ylabel('People')


station4[0:5].plot(
    x='Day', 
    y='Wait', 
    kind='bar', 
    legend=False, 
    color='blue',
    width=0.8)
plt.title('Station Five')
plt.ylabel('Wait')


station4[0:5].plot(
    x='Day', 
    y='People', 
    kind='bar', 
    legend=False, 
    color='blue',
    width=0.8)
plt.title('Station Five')
plt.ylabel('People')








"""Part 3.2"""

plt.subplot(2, 5, 1)
N = 100
x = np.random.rand(N)
y = np.random.rand(N)
plt.scatter(x, y)

plt.subplot(2, 5, 6)
vals = sobol_seq.i4_sobol_generate(2, 100)
vals[:,0]
vals[:,1]
plt.scatter(x=vals[:,0], y=vals[:,1])           

plt.subplot(2, 5, 2)
N = 500
x = np.random.rand(N)
y = np.random.rand(N)
plt.scatter(x, y)

plt.subplot(2, 5, 7)
vals = sobol_seq.i4_sobol_generate(2, 500)
vals[:,0]
vals[:,1]
plt.scatter(x=vals[:,0], y=vals[:,1])

plt.subplot(2, 5, 3)
N = 1000
x = np.random.rand(N)
y = np.random.rand(N)
plt.scatter(x, y)

plt.subplot(2, 5, 8)
vals = sobol_seq.i4_sobol_generate(2, 1000)
vals[:,0]
vals[:,1]
plt.scatter(x=vals[:,0], y=vals[:,1])

plt.subplot(2, 5, 4)
N = 2000
x = np.random.rand(N)
y = np.random.rand(N)
plt.scatter(x, y)

plt.subplot(2, 5, 9)
vals = sobol_seq.i4_sobol_generate(2, 2000)
vals[:,0]
vals[:,1]
plt.scatter(x=vals[:,0], y=vals[:,1])

plt.subplot(2, 5, 5)
N = 5000
x = np.random.rand(N)
y = np.random.rand(N)
plt.scatter(x, y)

plt.subplot(2, 5, 10)
vals = sobol_seq.i4_sobol_generate(2, 5000)
vals[:,0]
vals[:,1]
plt.scatter(x=vals[:,0], y=vals[:,1])
plt.show()







"""Part 3.3"""

plt.subplot(4, 5, 1)
x = np.random.uniform(-1,1,100)
plt.hist(x, 10, density=True)

plt.subplot(4, 5, 2)
x = np.random.uniform(-1,1,500)
plt.hist(x, 10, density=True)

plt.subplot(4, 5, 3)    
x = np.random.uniform(-1,1,1000)
plt.hist(x, 10, density=True)

plt.subplot(4, 5, 4)
x = np.random.uniform(-1,1,2000)
plt.hist(x, 10, density=True)

plt.subplot(4, 5, 5)
x = np.random.uniform(-1,1,5000)
plt.hist(x, 10, density=True)

plt.subplot(4, 5, 6)
x = np.random.normal(-1,1,100)
plt.hist(x, 10, density=True)

plt.subplot(4, 5, 7)
x = np.random.normal(-1,1,500)
plt.hist(x, 10, density=True)

plt.subplot(4, 5, 8)        
x = np.random.normal(-1,1,1000)
plt.hist(x, 10, density=True)

plt.subplot(4, 5, 9)
x = np.random.normal(-1,1,2000)
plt.hist(x, 10, density=True)

plt.subplot(4, 5, 10)
x = np.random.normal(-1,1,5000)
plt.hist(x, 10, density=True)
  
plt.subplot(4, 5, 11)    
x = np.random.binomial(10,.5,100)
plt.hist(x, 10, density=True)

plt.subplot(4, 5, 12)
x = np.random.binomial(10,.5,500)
plt.hist(x, 10, density=True)

plt.subplot(4, 5, 13)       
x = np.random.binomial(10,.5,1000)
plt.hist(x, 10, density=True)

plt.subplot(4, 5, 14)
x = np.random.binomial(10,.5,2000)
plt.hist(x, 10, density=True)

plt.subplot(4, 5, 15)
x = np.random.binomial(10,.5,5000)
plt.hist(x, 10, density=True)

plt.subplot(4, 5, 16)
sobol1=sobol_seq.i4_sobol_generate(1,100)
plt.hist(sobol1, 50)

plt.subplot(4, 5, 17)
sobol2=sobol_seq.i4_sobol_generate(1,500)
plt.hist(sobol2, 50)

plt.subplot(4, 5, 18)
sobol3=sobol_seq.i4_sobol_generate(1,1000)
plt.hist(sobol3, 50)

plt.subplot(4, 5, 19)
sobol4=sobol_seq.i4_sobol_generate(1,2000)
plt.hist(sobol4, 50)

plt.subplot(4, 5, 20)
sobol5=sobol_seq.i4_sobol_generate(1,5000)
plt.hist(sobol5, 50)














