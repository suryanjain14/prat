n = int(input())
scorecard=[]
b = (n*(n-1)//2)

for i in range(n):
    temp=[]
    temp.extend(input().split(" "))
    temp2=temp.pop()
    temp.extend(temp2.split("-"))
    scorecard.append(temp)
a=[]

b = (n*(n-1)//2)
for c in range(65,65+b):
   a.append(chr(c))

score=dict.fromkeys(a,0)

for team in scorecard:
    if team[3]==team[2]:
        score[team[0]]+=1
        score[team[1]] += 1
    elif team[2]>team[3]:
        score[team[0]] += 1
    else:
        score[team[1]]+=2

winner = max(score, key=score.get)
print(winner.upper())
print(score[winner])


