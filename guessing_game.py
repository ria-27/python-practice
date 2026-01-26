secret_word="giraffe"
guess=""     # to store the user's guess
guess_count=0
guess_limit = 3
out_of_guesses=False    # whether they are out of guesses - loses if true

while guess != secret_word and not(out_of_guesses):     #keeps looping as long as it is true
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")  # the guess variable will store whatever they input as answer
        guess_count += 1   # increments guess count for each try
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, You Lose.")
else:
    print("You Win!")