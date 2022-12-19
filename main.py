a=[]
b=[]
for x in range (1,101):
  if x%5==0:
    a[len(a):] = [x]
    y=x**3
    b[len(b):] = [y]
print(a) 
print(b)