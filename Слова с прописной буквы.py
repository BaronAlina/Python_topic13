n = input()

r = ord('a') - ord('A')

p = 0

for i in n:

    if 'a' <= i <= 'z' and p == 0:

        print(chr(ord(i) - r), end = '')

        p += 1

    elif 'A' <= i <= 'Z' and p == 0:

        print(i, end = '')

        p += 1

    else:

        if 'a' <= i <= 'z':

            p += 1

            print(i, end = '')

        elif 'A' <= i <= 'Z':

            p += 1

            print(chr(ord(i) + r), end = '')

        else:

            p = 0

            print(i, end = '')
        
