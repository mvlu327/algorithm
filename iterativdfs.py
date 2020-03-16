
def itrativedfs(graph, start):
  '''iterative depth first search from start'''
  path=[]
  q=[start]
  while q:
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      q=graph[v]+q
  return path
print("AMAN")
a=input("enter value for A:")
b=input("enter value for B:")
c=input("enter value for C:")
d=input("enter value for D:")
e=input("enter value for E:")
f=input("enter value for F:")


graph = {a:[b,c],
         b:[d,e],
         c:[d,e],
         d:[e],
         e:[a]}
itrativedfs(graph, a)
