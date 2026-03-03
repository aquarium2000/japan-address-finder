r=100
for x in range(1,r):
  for y in range(0,r):
    if x*x+y*y < r*r:
      if x>=y:
        print(1000000+x*x+y*y,x,y)
