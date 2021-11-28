n = input()
s = int(n[0])
for i in range(len(n)):
    if n[i] == '+':
        s += int(n[i+1])
    if n[i] == '-':
        s -= int(n[i+1])
print(s)
