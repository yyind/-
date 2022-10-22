a,b = input().split()
a = int(a)
b = int(b)
c = list(map(int,input().split()))

for i in c:
  if(i < b):
    print(str(i) ,end = " ")
