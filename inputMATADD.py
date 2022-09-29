def matrix(m, n):
    O = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter O[{i}][{j}]: "))
            row.append(inp)
        O.append(row)
    return O

def sum(A, B):
    output = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output

m = int(input("Enter m: ")) #Enter the no. of rows
n = int(input("Enter n: "))#Enter the no. of columns

print("Enter Matrix A: ")
A = matrix(m ,n)
print(A)

print("Enter Matrix B: ")
B = matrix(m, n)
print(B)

s = sum(A, B)

print(s)