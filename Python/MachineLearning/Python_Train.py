import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)

### CREATE THE ARRAY THAT PRESENT THE AXIS OF X AND Y:
## Exponential
x = numpy.linspace(-1, 2, 100) #The x axis
y = numpy.exp(x) #The y axis

## Polynomial
# x = numpy.linspace(-1, 2, 100)
# y = numpy.cos(x) + 0.3*numpy.random.rand(100)

## logarithm
# A = 30
# a = 3.5
# x = numpy.linspace(1, 5, 100)
# y = A * x**a
# x = numpy.log(x)
# y = numpy.log(y)

### SPLIT INTO TRAIN/SET
### % Train Data of the original
train_x = x[:80]
train_y = y[:80]

### % Test Data of the original
test_x = x[80:]
test_y = y[80:]

### DISPLAY THE TRAINING SET
plt.scatter(train_x, train_y)
plt.show()

### DISPLAY THE TESTING SET
plt.scatter(test_x, test_y)
plt.show()

### FIT THE DATA SET
## Polynomial Regression
# Training data
mymodel1 = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

#Testing data
mymodel2 = numpy.poly1d(numpy.polyfit(test_x, test_y, 4))

## Specify how the line will display
# Exponential
myline1 = numpy.linspace(-1, 2, 100)

# Polynomial
myline2 = numpy.linspace(-1, 2, 100)

# logarithm
myline3 = numpy.linspace(0.01, 1.00, 100)

### DISPLAY THE TRAINING SET AND POLYNOMIAL REGRESSION LINE:
## Exponential
plt.scatter(train_x, train_y)
plt.plot(myline1, mymodel1(myline1))
plt.show()

## Polynomial
# plt.scatter(train_x, train_y)
# plt.plot(myline2, mymodel1(myline2))
# plt.show()

## logarithm
# plt.scatter(train_x, train_y)
# plt.plot(myline3, mymodel1(myline3))
# plt.show()


### R2
# measure the relationship x and y
r2 = r2_score(train_y, mymodel1(train_x))
print(r2)

# make predict
print(mymodel2(10))