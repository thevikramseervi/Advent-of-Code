# Part One ---> ans = 1666427

f = open("input.txt", "r")
a = f.read()
f.close()

b = a.split()
c = []
left = []
right = []
sum = []
ans = 0

for i in b:
    c.append(int(i))

i = 0
while i < 2000:
    left.append(c[i])
    right.append(c[i+1])
    i += 2

left.sort()
right.sort()

j = 0
while j < 1000:
    sum.append(abs(left[j] - right[j]))
    j += 1

for k in sum:
    ans += k

print(ans)


# Part Two ---> ans = 24316233
d = {}
sum2 = []
ans2 = 0

for _ in left:
    d[_] = right.count(_)

for x, y in d.items():
    sum2.append(x * y)

for _ in sum2:
    ans2 += _

print(ans2)
