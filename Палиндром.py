n = input()

r = ord('a') - ord('A')

k = ''

for i in n:

    if 'A' <= i <= 'Z':

        k +=(chr(ord(i) + r))

    else:

        k += i

o = 'YES'

for i in range(0, len(k) // 2):

    if k[i] != k[-(i+1)]:

        o = 'NO'

print(o)
