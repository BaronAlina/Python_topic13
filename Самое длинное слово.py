n = input()
p = 0
d = ''
x = 0
w = ''
for i in n:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        p += 1
        d += i
    else:
        if p > x:
            x = p
            w = d
        p = 0
        d = ''
if p > x:
    x = p
    w = d
print(w)
