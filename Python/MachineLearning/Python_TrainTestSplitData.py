#The training set is applied to train, or fit, your model. For example, you use the training set to find the optimal weights, or coefficients, for linear regression, logistic regression, or neural networks.
#The validation set is used for unbiased model evaluation during hyperparameter tuning. For example, when you want to find the optimal number of neurons in a neural network or the best kernel for a support vector machine, you experiment with different values. For each considered setting of hyperparameters, you fit the model with the training set and assess its performance with the validation set.
#The test set is needed for an unbiased evaluation of the final model. You shouldn’t use it for fitting or validation.

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x = np.arange(1, 25).reshape(12, 2)
x
y = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])

