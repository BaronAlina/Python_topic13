def CaseChange(c):
    if 'A' <= a <= 'Z':
        return chr(ord(a) + 32)
    elif 'a' <= a <= 'z':
        return chr(ord(a) - 32)
    elif chr(32) <= a <= chr(64) or chr(91) <= a <= chr(96) or chr(123) <= a <= chr(127):
        return chr(ord(a))
a = input()
ans =  CaseChange(a)
print (ans)
