import random
guessesTaken = 0
print ('hi, wat is your name?')
myName = input()
number = random.randint(1,20)
print ('So what, ' + myName + ',I am guessing a number between 1 and 20.')
for guessesTaken in range(6):
    print ('take a wild guess')
    guess = input()
    guess = int(guess)
    
    if guess < number:
        print ('your number is small.')
    if guess > number:
        print('your nmber is big ')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print ('Good, ' + myName + '! you did it for ' + guessesTaken + 'attempt!')
if guess != number:
    number = str(number)
    print('oh, I guessed a number '+ number +'.')
