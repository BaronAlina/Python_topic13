n = input()

f = ''

r = ord('a') - ord('A')

for i in n:

    if 'a' <= i <= 'z':

        f += chr(ord(i) - r)

    elif 'A' <= i <= 'Z':

        f += i



i = 0

mx = 0

y = ''

while f != '':

    c = f.count(f[i])

    if mx < c:

        mx = c

        y = f[i]

    elif mx == c:

        y += f[i]

    f = f.replace(f[i], '')



i = 0

while y != '':

    m = ord('Z')

    a = ''

    for j in y:

        if m > ord(j):

            m = ord(j)

            a = j

    print(a, end = '')

    y = y.replace(a, '')



print('\n', mx, sep = '')
