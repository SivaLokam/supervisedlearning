# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:03:27 2020

@author: ADMIN
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(2)
import math
import seaborn as sns

#positive correlation 

pc = pd.DataFrame()
pc['x'] = np.random.randint(0,50,100)
pc['y'] = pc['x'] + np.random.randint(0,20,100)

plt.scatter(pc['x'],pc['y'])
plt.show()
print(f"The correlation between two variables x and y is { round(pc['x'].corr(pc['y']))}")


#Negative correlation
nc = pd.DataFrame()
nc['x'] = np.random.randint(0,50,100)
nc['y'] = 50 - nc['x'] - np.random.randint(0,20,100)
#pc['y'] = pc['x'] - np.random.randint(0,20,100)

plt.scatter(nc['x'],nc['y'])
plt.show()
print(f"The correlation between two variables x and y is {round(nc['x'].corr(nc['y']))}")

wc = pd.DataFrame()
wc['x'] = np.random.randint(0,50,100)
wc['y'] = np.random.randint(0,50,100)
plt.scatter(wc['x'],wc['y'])
plt.show()
print(f"The correlation between two variables x and y is {round(wc['x'].corr(wc['y']))}")

np.random.normal(0,5,100000)

s=5
pie = math.pi
const = 1/(np.sqrt(2*pie*(s**2)))
li = [-1,1]
dist = const*np.exp(-1*((np.random.randint(5)**2)/2*(s**2)))
values = [ const*np.exp((np.random.choice(li)*np.random.randint(5)**2)/2*(s**2)) for val in range(100)]
#plt.plot(values,'ro')
sns.distplot(values)


def normaldist(u=0,s=1,n=100):
    li = [-1,1]
    values = [np.random.choice(li)*np.random.randint(s) for _ in range(n)]
    const = 1/(np.sqrt(2*pie*(s**2)))    
    dist = [const*np.exp(-((val-u)**2)/2*(s**2)) for val in values]
    return values,dist
val,dist = normaldist(s=10,n=10000)
plt.scatter(val,dist)



values = np.random.normal(0,1,100)
sns.distplot(values)

sns.distplot(values,kde_kws={"color": "k", "lw": 3, "label": "KDE"},rug=False)

penguins = sns.load_dataset("penguins")

sns.distplot(data=penguins, x="flipper_length_mm", kind="kde")


values = [ np.exp(-1*np.random.rand()) for _ in range(100)]

(np.random.binomial(1,0.5)>0)*1
np.random.binomial(1,0.5)







