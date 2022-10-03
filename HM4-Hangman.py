import random

with open("Words.txt", "r") as f:
    words = f.readlines()

word = random.choice(words)[:-1]
allowed_errors = 3
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Allowed errors left {allowed_errors}, Next guess please: ")
    guesses.append(guess.lower())
    if not guess.isalpha():
         print("The character is not a letter!")
         continue
    elif not len(guess.lower()) == 1:
         print("Please enter only one letter")
         continue
    elif guess.lower() not in word.lower():
        allowed_errors -= 1

        if allowed_errors == 0:
             break

        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False

if done:
    print(f"You won! The word was {word}")
else:
    print(f"You lost. The word was {word}")