# Importing libraries
import numpy as np

# Given values
X = [28, 50, 61, 72, 80, 51, 20, 35, 28, 97, 37, 64, 46, 67, 34, 21, 21, 59, 46, 46]
Y = [62, 87, 88, 109, 95, 104, 58, 82, 70, 102, 67, 104, 83, 89, 69, 68, 65, 103, 78, 102]

print("Given X:\n", X)
print("Given Y:\n", Y)

# Mean of X
print("Mean of X:", np.mean(X))

# Variance of X
print("Variance of X:",np.var(X, ddof=0 ))

# Mean vector
mean_vect = np.stack((np.mean(X), np.mean(Y)), axis = 0)
print("Mean vector: ", mean_vect)

# Covariance Matrix
cov_mat = np.stack((X, Y), axis = 0)
cov_mat = np.cov(cov_mat, ddof=0)
print("Covariance Matrix:\n", cov_mat)

# Eigenvalues and Eigenvectors
evalue, evect = np.linalg.eig(cov_mat)

print("Eigenvalues:\n", evalue)

print("Eigenvectors:\n", evect)

# Counting the no. of observations with age >=75
count = len([each for each in X if each >= 75])

# Probability of observing an age of 75 or higher
prob = count/len(X)

print("Probability of observing an age of 75 or higher: ", prob)

