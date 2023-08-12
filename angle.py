import torch
from numpy import (array, dot, arccos, clip)
from numpy.linalg import norm
v1 = torch.Tensor([[1,2],[4,3],[4,1],[6,7],[9,10]])
def angle(ind, v):
  points = v[ind:ind+3]
  u = points[1]-points[0]
  print(u)
  v = points[2]-points[0]
  print(v)
  c = dot(u,v)/norm(u)/norm(v) # -> cosine of the angle
  angle = arccos(clip(c, -1, 1)) 
  return angle

angles = []
for i in range(len(v1)-2):
  angles.append(angle(i,v1))
  print(angles[i])
angles
