deliver = int(input())
collision = int(input())

deliverpoint = deliver*50
collisionpoint = collision*10

pointtotal = deliverpoint - collisionpoint
if deliver > collision:
  pointtotal += 500
print(pointtotal)
