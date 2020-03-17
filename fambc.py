# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

a = int(input())
c = int(input())

h = math.sqrt(a**2 + c**2)
h = h / 2.0
adj = c / 2.0
result=round(math.degrees(math.acos(adj/h)))
print(str(result)+'°')
