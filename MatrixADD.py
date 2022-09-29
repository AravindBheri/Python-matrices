A = [[1,2,7],
     [8,11,12],
     [2,8,1]]
     
B = [[1,7,4],
     [1,2,7],
     [0,3,5]]
     
C = [[0,0,0],
     [0,0,0],
     [0,0,0]]      

#Rows and columns of first and second matrix should be same!! m * n = m * n
    
for i in range(0, len(C)):
        for j in range(0, len(C)):
              C[i][j] = A[i][j] + B[i][j]
            
            
for c in C:
    print(c)
        

