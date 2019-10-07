def fab():
    a,b = 0,1
    while True:
        yield a
        a,b = b , a+b

for f in fab():
    if f > 100:
        break
    print(f)


   # mx = lambda x,y:x if x > y else y