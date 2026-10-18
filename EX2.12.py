import random

money = 10
goal = 20

while money > 0 and money < goal:
    if random.randint(0, 1) == 0:
        money += 1
    else:
        money -= 1

print("Final money:", money)

if money == 0:
    print("Gambler lost")
else:
    print("Gambler won")