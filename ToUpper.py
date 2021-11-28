n=input()
r=ord('a')-ord('A')
if ord(n)<ord('a') or ord(n)>ord('z'):
    print (n)
else:
    print(chr(ord(n)-r))
