f = open("input.txt", "r")

a = f.read()
b = a.splitlines()

ss = 0

def fn(x: list) -> int:
    y = False
    if x[0] - x[1] < 0:                         # increasing
        y = True

    for i in range(len(x) - 1):
        if abs(x[i] - x[i+1]) < 1 or abs(x[i] - x[i+1]) > 3:
            return 0
        elif (y == True and x[i] - x[i+1] > 0):   # decreasing
            return 0
        elif (y == False and x[i] - x[i+1]) < 0:  # increasing
            return 0
        
    return 1
        

for i in b:
    c = i.split()
    for j in range(len(c)):
        c[j] = int(c[j])
    ss += fn(c)

print(ss)
