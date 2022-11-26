n = int(input("algo: "))
f1 = [0]
f2 = [1]
s = [0]
l = []

for i in range(0,n):
  l.append(f1[0])
  s[0] = f1[0] + f2[0]
  f1[0] = f2[0]
  f2[0] = s[0]

print(l)