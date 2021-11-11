import random
number=random.randint(1,9)
print('Guess a number between 1 and 9')
chances=0

while chances<5:
    guess=int(input('Enter a guess: '))
    if(guess==number):
        print('Congratulations! You Won!')
        break
    elif(guess>number):
        print('Your guess is high')
    else:
        print('Your guess is low') 

    chances+=1

if not chances<5:
    print('You Lose! The number was ',number)    