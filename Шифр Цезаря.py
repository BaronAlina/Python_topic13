n = input()
r = ord('x') - ord('a')
for i in n:
    if 'a' <= i < 'x' or 'A' <= i < 'X':
        print(chr(ord(i) + 3), end = '')
    elif 'x' <= i <= 'z' or 'X' <= i <= 'Z':
        print(chr(ord(i) - r), end = '')
    else:
        print(i, end = '')
