from numpy import *

A = [[2,1,4],
     [0,1,1]]

B = [[6,3,-1,0],
     [1,1,0,4],
     [-2,5,0,2]]
     
C = [[0,0,0,0],
     [0,0,0,0]]    
    
for i in range(0, len(A)):
    for j in range(0, len(C[0])):
        for k in range(0, len(B)):
            C[i][j] += A[i][k] * B[k][j]
            
            '''
            no. of columns of 1st matrix and no. of rows in 2nd matrix 
            should be same to perform matrix multiplication.
            M1(m * n) = M2(n * q)
            result matrix = m * q

            C[0][0] = A[0][0] * B[0][0]
                     = 1 * 1 
                     A[0][1] * B[1][0]
                     = 5 * 1
                     A[0][2] * B[2][0]
                     =3 * 5
                     '''
            
for c in C:
    print(c)
    
print()
print()

m = matrix(C)          #Use Numpy's Matrix fun to convert list C into matrix m
print(m)
        
'''       
 A = [[2,1,4],
      [0,1,1]]

 B = [[6,3,-1,0],
      [1,1,0,4],
      [-2,5,0,2]]
      
 Result = [[5,27,-2,12],
           [-1,6,0,6]]
           
 A = [[-2,1],
      [0,4]]
      
 B = [[6,5],
      [-7,1]]
      
 Result = [[-19,-9],
           [-28,4]]

'''