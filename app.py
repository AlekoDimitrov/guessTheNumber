from random import randint


def guessTheNumber():
    randomNumber = randint(1, 20)
    numberOfTries = 1
    name = input('Hello. What is your name?\n')
    print('Well, ' + name + ', I am thinking of a number'
          ' between 1 and 20.')
    while name:
        print('Take a guess')
        numGuess = int(input())
        if numGuess < randomNumber:
            print('Your guess is too low')
            numGuess
            numberOfTries += 1
        elif numGuess > randomNumber:
            print('Your guess is too high')
            numGuess
            numberOfTries += 1
        else:
            print('Good job, ' + name + '! You guessed the number in ' 
                  + str(numberOfTries) + ' tries')
            break


guessTheNumber()