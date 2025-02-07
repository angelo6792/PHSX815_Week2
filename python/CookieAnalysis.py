#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE
w = np.ones_like(times) / len(times)


fig1 = plt.figure()
#quant = np.quantile(fig1, [0.05, 0.5, 0.95], axis=1)
ax1 = fig1.add_subplot()
ax1.hist(times, 50,  weights = w)
ax1.set_yscale('log')
ax1.set_xlabel('Time between missing cookies')
ax1.set_ylabel('Probability')

W = np.ones_like(times_avg) / len(times_avg)

fig2 = plt.figure()
ax2 = fig2.add_subplot()
ax2.hist(times_avg, 50, weights = W)
ax2.set_yscale('log')
ax2.set_xlabel('Average times')
ax2.set_ylabel('Probability')

fig1.savefig('time.png')
fig2.savefig('average.png')
plt.show()

