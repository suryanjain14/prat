from itertools import combinations_with_replacement,permutations,combinations

dist = int(input())
crangetemp = input().split(" ")
irangetemp = input().split(" ")

crange=[]

for c in range(ord(crangetemp[0]),ord(crangetemp[1])+1):
   crange.append(chr(c))

irange=[]
for i in range(int(irangetemp[0]),int(irangetemp[1])+1):
    irange.append(i)

print(irange ,"ir")
print(crange, "cr")
totalc = list(combinations_with_replacement(crange,2))
totali = list(combinations_with_replacement(irange,4))
a=[]
for i in totali:
    a.extend(permutations(i))
a=set(a)
z=[]
for i in totalc:
    z.extend(permutations(i))
z=set(z)
# print(totalip ,totalic)
print(totali)
print(totalc)

print(dist*len(a)*len(z))
