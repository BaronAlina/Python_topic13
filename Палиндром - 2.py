n = input()

y = ''

r = ord('a') - ord('A')

for i in n:

    if 'a' <= i <= 'z':

        y += i

    elif 'A' <= i <= 'Z':

        y += chr(ord(i) + r)

i = 0

c = 'YES'

while i != len(y) // 2:

    if y[i] != y[-(i+1)]:

        c = 'NO'

    i += 1



print(c)

