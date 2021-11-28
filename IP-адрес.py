b = str(input())
k = b.split('.')

if (len(k)!=4):
  print("NO")
else:
  error = False
  for  num  in  k:
      if int(num)<0 or int(num)>255:
        print('NO')
        error = True
        break
  if not error:
    print("YES")
