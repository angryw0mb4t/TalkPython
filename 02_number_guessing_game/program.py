import random

print('---------------------------------')
print('    Guess That Number Game    ')
print('---------------------------------')
print()

the_number = random.randint(0, 100)
guess = 101
name = input('What is your name? ')

while guess != the_number:
    guess_text = input("Guess a number between 0 and 100: ")
    guess = int(guess_text)
    if guess < the_number:
        print("Your guess of " + str(guess) + " is too low")
    elif guess > the_number:
        print("{0} your guess of {1} is too high".format(name, guess))
    else:
        print("You win!")
