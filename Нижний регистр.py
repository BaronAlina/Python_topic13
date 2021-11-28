n = input()

r = ord('a') - ord('A')

for i in n:

    if 'A' <= i <= 'Z':

        print(chr(ord(i) + r), end = '')

    else:

        print(i, end = '')
