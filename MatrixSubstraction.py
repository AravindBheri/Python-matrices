A = [[1,2,7],
     [8,11,12],
     [2,8,1]]
     
B = [[1,7,4],
     [1,2,7],
     [0,3,5]]
     
C = [[0,0,0],
     [0,0,0],
     [0,0,0]]      
    
for i in range(0, len(C)):
    for j in range(0, len(C)):
        for k in range(0, len(C)):
              C[i][k] = A[i][k] - B[i][k]
            
            
for c in C:
    print(c)
        

