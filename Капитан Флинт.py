x = 0
y = 0
n = 'f'
while n != 'Treasure!':
    n = input()
    if n != 'Treasure!':
        a, b = map(str, n.split())
        b = int(b)
        if a == 'North':
            y += b
        elif a == 'South':
            y -= b
        elif a == 'East':
            x += b
        elif a == 'West':
            x -= b
print(x,y)

