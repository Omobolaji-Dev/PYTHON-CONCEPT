import random
words = ["peniel","ayooluwa","Justine","skye","Jackson","Raymond"]
secret_word = random.choice(words)
number_guesses = 0
while True:
    guess = input("Type your guess: ")
    number_guesses +=1
    if guess == secret_word:
        print("congratulations you guessed the secret word in", number_guesses, "Guesses")
        break
    elif number_guesses == 3:
        print("You are out of guesses. The secret word was:", secret_word)
    else:
        print("Sorry, that is incorrect secret word. Please try again")

