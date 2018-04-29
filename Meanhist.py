# Mary McHale, 14th April 2018
# Plotting the histogram for the mean of the Iris Data set
# Use of numpy and matplotlib.pyplot

import numpy

#Read data file into array

data = numpy.genfromtxt('data/iris.csv', delimiter=',')
firstcol = data[:,0,0,0,0]
print("Average of Petal length is" ,meanfirstcol)

