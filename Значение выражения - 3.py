n = input()

s = 0

r = '+'

a = ''

for i in n:

    if '0' <= i <= '9':

        a += i

    else:

        if r == '+':

            s += int(a)

        elif r == '-':

            s -= int(a)

        r = i

        a = ''

if r == '+':

    s += int(a)

elif r == '-':

    s -= int(a)

print(s)
