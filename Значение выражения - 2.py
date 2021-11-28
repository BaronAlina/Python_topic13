n = input()
i = 0
a = ''
while '0' <= n[i] <= '9':
    a += n[i]
    i += 1
a = int(a)
k = n[i]
i += 1
b = ''
while i < len(n) and '0' <= n[i] <= '9':
    b += n[i]
    i += 1
b = int(b)
if k == '+':
    print(a+b)
elif k == '-':
    print(a-b)
else:
    print(a*b)

