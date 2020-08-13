import random
num = random.randint(1, 20)
while True:
    print('Guess a number between 0 and 20')
    guess = input()
    i = int(guess)
    if i == num:
        print('You won!!!')
        break
    elif i < num:
               print('Try Higher')
    elif i > num:
               print('Try Lower')
print('if you guess less than 4 times you won')



