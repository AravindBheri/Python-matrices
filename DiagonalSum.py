A = [[1, -5, 2], 
     [-3, 7, 9], 
     [4, -1, 6]]

'''

Sum of Primary Diagonal 
--------------------------------------------
     
primary_diagonal_sum = 0  #sum is 14

for i in range(len(A)):
    for j in range(len(A[0])):
        if i == j:
            primary_diagonal_sum += A[i][j]
            
print(primary_diagonal_sum)

--------------------------------------------

'''


'''
Sum of Secondary Diagonal Approach 1
--------------------------------------------

n = len(A)
     
secondary_diagonal_sum = 0  #sum is 13

for i in range(len(A)):
    for j in range(len(A[0])):
        if i + j == n - 1:
            secondary_diagonal_sum += A[i][j]
            
print(secondary_diagonal_sum)

--------------------------------------------

'''



'''

Sum of Secondary Diagonal Approach 2
--------------------------------------------

n = len(A)
     
secondary_diagonal_sum = 0  #sum is 13

for i in range(len(A)):
    for j in range(len(A[0])):
        if j == n - i - 1:
            secondary_diagonal_sum += A[i][j]
            
print(secondary_diagonal_sum)

--------------------------------------------

'''

'''
Using Numpy
--------------------------------------------

import numpy as np

# x = np.matrix('1 2 3; 4 5 6; 7 8 9')

x = np.array([[1, -5, 2], [-3, 7, 9], [4, -1, 6]])  

print(x.trace())  #Trace() tp print sum of primary diagonal

print(x[::-1].trace()) #x[::-1] to reverse matrix

print(x.diogonal().sum())

print(x[::-1].diagonal().sum())
--------------------------------------------
'''