#run from here
#because this is main

import intensity_calculator as ic
import buckets as B
import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime
import simulation

"""
import cppyy
cppyy.include("buckets.h")
cppyy.load_library("buckets")
from cppyy.gbl import Buckets
B = Buckets()
"""

plt.figure(figsize = (10,5), tight_layout = True)

#user inputs
l = input("enter a wavelength (nm): ")
l = float(l) * (10**-9)
a = input("enter a slit width (micro m): ")
a = float(a) * (10**-6)
d = input("enter a slit separation (micro m): ")
d = float(d) * (10**-6)
D = input("enter a distance from the screen (m): ")
D = float(D)
n = input("enter a counting number: ")
n = int(n)
num = input("finally, input the number of particles: ")
num = int(num)

#calculating the overall intensity distribution

values = ic.double_intensity(n, a, l, D)
intensity = values[1]
x_vals = values[0]

#determining where the particle should go
x = list()
for i in range(0, num):
    bucket_info = B.bucket(intensity, x_vals)
    intensity1 = bucket_info[0]
    x_vals1 = bucket_info[1]
    while( len(x_vals1) > 1 ):
        bucket_info = B.bucket(intensity1, x_vals1)
        intensity1 = bucket_info[0]
        x_vals1 = bucket_info[1]
    if random.randint(0,10)%2 == 0:
        x.append(x_vals1[0])
    else:
        x.append(-1*x_vals1[0])

points = dict()
for i in x:
    if i in points:
        points[i] += 1
    else:
        points[i] = 1

plt.subplot(122)
x = plt.bar(points.keys(), points.values())
plt.axis([-5,5,0,max(points.values())])
plt.show()