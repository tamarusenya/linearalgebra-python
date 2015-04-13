# -*- coding: utf-8 -*-

from scipy import linalg

#2×2行列
a = np.array([[1,2],[3,4]])

#行列式 determinant
b = linalg.det(a)

#逆行列 inverse matrix
c = linalg.inv(a)

#対角化 diagonalisation
d = diagonal(a)

#共役行列　conjugate matrix
e =conj(a)

#固有値と固有ベクトル eigenbalue and eigenvector
f = linalg.eig(a)

#正規化
g = linalg.norm(a)

h = linalg.lu(a)

print "matrix"
print a
print "determinant"
print b
print "ineverse matrix"
print c
print "diagonalisation"
print d
print "conjugate matrix"
print e
print "eigenbalue and eigenvector"
print f
print "normalization"
print g
print "LU decomposition"
print h
