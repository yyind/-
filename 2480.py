a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

if (a == b == c): 
    print(10000 + a* 1000)
    
elif a == b:
    print(1000 + a* 100)
    
elif b == c:
    print(1000 + b* 100)
    
elif c == a:
    print(1000 + c* 100)
    

elif (a > b > c):
    print(a * 100)
    
elif (a > c > b):
    print(a * 100)
    
elif (b > a > c):
    print(b * 100)
    
elif (b > c > a):
    print(b * 100)    

elif (c > a > b):
    print(c * 100)
    
elif (c > b > a):
    print(c * 100)
