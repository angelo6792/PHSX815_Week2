#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt
import math

#import random
from Random2 import Random
random = Random()

#loop Rayleigh through an empty array to create distribution
n=100000
a = []
for x in range(0,n):
   a.append(random.Rayleigh())

#plot array
n, bins, patches = plt.hist(a, 50, density=True, facecolor='g', alpha=0.75)
plt.xlabel('x', fontsize = 16, color = "blue")
plt.ylabel('Probability', fontsize = 16, color = "red")
plt.title('Rayleigh distribution')
#plt.legend(['cool green bars'], loc = 'upper left')
plt.grid(True)

plt.show()
