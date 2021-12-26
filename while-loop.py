import math

number = 7
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input(f'Guess {guess_count + 1}: '))
    if guess == number:
        print('You won..!')
        print('Score: ', math.ceil((guess_limit - guess_count) / guess_limit * 100))
        break
    guess_count += 1
else:
    print(f'Game Over!!!\nThe Number is: {number}')
