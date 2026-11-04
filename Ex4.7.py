import stdio, random

RANGE = 1000000

secret = random.randrange(1, RANGE + 1)
print('Guess a number between 1 and %d' %RANGE)

guess = 0
while guess != secret:
    
    print('What is your guess?', end=' ')
    guess = stdio.readInt()
    
    if guess < secret: print('Too low')
    elif guess > secret: print('Too high')
    else: print('You win!')
