#!/usr/bin/env python

# value, position, dimension, whole_ma(value, postion)
xx1 = map(lambda x: (zip(x.replace('\n', ''), range(1, len(x.replace('\n', ''))+1), (len(x.split('\n')) for _ in range(1, len(x.replace('\n', ''))+1)), (zip( map( lambda xx: 0 if xx == '.' else 1 ,x.replace('\n', '')) , range(1, len(x.replace('\n', ''))+1)) for _ in range(1, len(x.replace('\n', ''))+1)))), ['\n'.join(iter(raw_input, ''))])

# print(x1[0])
# value, position, dimension, alive_neigbors
xx2 = map(lambda x_0: (x_0[0], x_0[1], x_0[2], reduce(lambda a, b: a+b, map(lambda d: d[0], filter(lambda c: c[1] in {x_0[1]+1, x_0[1]-1, x_0[1]-x_0[2]-1, x_0[1]-x_0[2], x_0[1]-x_0[2]+1, x_0[1]+x_0[2]-1, x_0[1]+x_0[2], x_0[1]+x_0[2]+1,}, x_0[3])) ) ), xx1[0] )
# print(x1[0][0])
# print(xx2)

# value, position, dimension, should_change
xx3 = map(lambda x1: (x1[0], x1[1], x1[2],  ((x1[0] == '0' and x1[3] <= 1) or (x1[0] == '.' and x1[3] == 3) or (x1[0] == '0' and x1[3] >= 4))), xx2)
print(xx3)

# new_value, , position, dimension
xx4 = reduce(lambda a1, b1: a1+b1 ,map(lambda x2: ('.' if ((x2[0] == '.' and not x2[3]) or (x2[0] == '0' and x2[3]) ) else '0')+('\n' if x2[1]% x2[2] == 0 else ''), xx3))
print(xx4)

# xx3 = map(lambda )