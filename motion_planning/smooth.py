import pygame
from scipy import interpolate
import numpy as np
import matplotlib

# 0. Start by importing Numpy and interpolate from Scipy



# 1. Get cumulative function
cumulative_generation = np.array([0, 0.5, 2.5, 7.5, 15.5, 25.5, 35.5, 45, 53.5, 60.5, 65.5, 67.5])
hours = np.arange(8, 20)

# 2. Interpolate the cumulative function (Spline interpolation)
interpolator = interpolate.CubicSpline(hours, cumulative_generation)

# 3. Differentiate and substitute.
#    For example, differentiate and interpolate the power at 10am:
print(interpolator(10, 1))
# 3.37 is the output of the interpolation at 10am.






""" def B_spline(waypoints):
        x1=[]
        y1=[]

        for point in waypoints:
            x1.append(point[0])
            y1.append(point[1])

        tck, *rest = interpolate.splrep([x1, y1])
        u = np.linspace(0, 1, num=100)
        smooth = interpolate.splev(u, tck)
        print(tck)

        return smooth

def waypoints():
    waypoints (1,5) """