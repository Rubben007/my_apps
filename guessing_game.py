import random

print("wellcome to the guessing game")
print("I have a number betwwen 1 and 10 can you nguess?")
print("[choice: press 1 to try, press 2 to close the game]")

def Guess():
    rang1 = 1
    rang2 = 20
    guess_count = 0
    guess_limit = 3
    secret_number = random.randint(rang1, rang2)
    while guess_count < guess_limit:
        guess_count += 1
        guess = int(input("enter a guess: "))
        if guess == secret_number:
            print("congratulation you won")
            break
        elif guess > secret_number:
            print("value too high try again")
        elif guess < secret_number:
            print("value too low try again")
    else:
        print("oh sorry you failed all try attempt")


choice = input("enter choice: ")
if choice == "2":
    print("Game closed")
elif choice == "1":
    return Guess()


Guessing_game()
