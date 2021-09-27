using Statistics
using LinearAlgebra

X = [28, 50, 61, 72, 80, 51, 20, 35, 28, 97, 37, 64, 46, 67, 34, 21, 21, 59, 46, 46];
println("Given X:\n", X)

Y = [62, 87, 88, 109, 95, 104, 58, 82, 70, 102, 67, 104, 83, 89, 69, 68, 65, 103, 78, 102];
println("Given Y:\n", Y)

println("Mean of X: ", Statistics.mean(X))

println("Variance of X: ", Statistics.var(X, corrected = false))

A = [Statistics.mean(X) Statistics.mean(Y)]
println("Mean vector:\n", A)

A = [cov(X, corrected = false) cov(X, Y, corrected = false); cov(X, Y, corrected = false) cov(Y, corrected = false)];
println("Covariance Matrix:\n", A)

println("Eigenvalues:\n", eigvals(A))

println("Eigenvectors:\n", eigvecs(A))