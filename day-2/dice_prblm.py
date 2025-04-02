import random

#all the possible outcomes
d1=[1,2,3,4,5,6]
d2=[1,2,3,4,5,6]
li=[]
for i in d1:
    for j in d2:
        li.append((i,j))
print(li)
#probability
di={}
for i in range(2,13):
    c=0
    for j in li:
        if i==j[0]+j[1]:
            c+=1
        di[i] = c / len(li) 
print(di)

r = int(input("Enter number of rounds: "))
p1_wins, p2_wins = 0, 0
for i in range(r):
    p1_d1, p1_d2 = random.randint(1, 6), random.randint(1, 6)
    p2_d1, p2_d2 = random.randint(1, 6), random.randint(1, 6)
    p1_sum, p2_sum = p1_d1 + p1_d2, p2_d1 + p2_d2
    print(f"Round No: {i+1}: Player 1 : ({p1_d1}, {p1_d2}) = {p1_sum} and  Player 2 : ({p2_d1}, {p2_d2}) = {p2_sum}")
    if di[p1_sum] < di[p2_sum]: 
        p1_wins += 1
    elif di[p1_sum] > di[p2_sum]:
        p2_wins += 1
if p1_wins > p2_wins:
    print("Player 1 wins")
elif p2_wins > p1_wins:
    print("Player 2 wins")
else:
    print("It's a draw")