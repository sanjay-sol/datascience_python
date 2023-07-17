MAX=10
w = [[0] *MAX for _ in range(MAX)]
c = [[0] *MAX for _ in range(MAX)]
r = [[0] *MAX for _ in range(MAX)]
p = [0] *MAX
q = [0] *MAX
temp = 0
min_val = 0
min1 = 0
print("Enter the number of elements:")
n = int(input())
print("Enter p's:")
for i in range(1, n + 1):
    p[i] = int(input())
print("Enter q's:")
for i in range(n + 1):
    q[i] = int(input())
print("W\t\tC\t\tR\n")
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            w[i][j] = q[i]
            c[i][j] = 0
            r[i][j] = 0
            print(f"W[{i}][{j}]: {w[i][j]}\tC[{i}][{j}]: {c[i][j]}\tR[{i}][{j}]: {r[i][j]}")
for i in range(n+1):
    for j in range(i+1,n+1):
        w[i][j] = p[j]+q[j]+w[i][j-1]
        min_val = 30000
        for k in range(i+1,j+1):
            min1 = c[i][k - 1] + c[k][j] + w[i][j]
            if min_val > min1:
                min_val = min1
                temp = k
            c[i][j] = min_val
            r[i][j] = temp
        print(f"W[{i}][{j}]: {w[i][j]}\tC[{i}][{j}]: {c[i][j]}\tR[{i}][{j}]: {r[i][j]}")