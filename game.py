import random
import sys

while True:
    try:
        level = int(input("Level: "))
        rand = random.randint(1, level)
        while True:
            try:
                guess = int(input("Guess: "))
                if guess < 0:
                    continue
                elif guess < rand:
                    print("Too small!")
                    continue
                elif guess > rand:
                    print("Too large!")
                    continue
                else :
                    print("Just right!")
                    sys.exit()
            except ValueError:
                    continue
    except ValueError:
        continue
