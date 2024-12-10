# Day 04 Part One
# Ans = 2646

f = open("input.txt")
a = f.read()
f.close()

b = a.split()
n = len(b)
cnt = 0


def isIndexOutOfBound(i, j):
    if i >= 0 and i < n and j >= 0 and j < n:
        return False
    return True


def universal(i, j, x):
    s = ""
    for k in range(4):
        if isIndexOutOfBound(i + x[0] * k, j + x[1] * k):
            return 0
        s = s + b[i + x[0] * k][j + x[1] * k]
    if s == "XMAS":
        return 1
    return 0


#    normal     back     down       up      diag    antidiag   oppdiag  antioppdiag
d = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]

for i in range(n):
    for j in range(n):
        if b[i][j] == "X":
            for x in d:
                cnt += universal(i, j, x)

print(cnt)
