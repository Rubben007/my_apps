import random


def guess_number(secret_number, guesses):
    guess_count = 0
    guess_limit = 3
    results = []

    for guess in guesses:
        guess_count += 1
        if guess == secret_number:
            results.append("congratulation you won")
            break
        elif guess > secret_number:
            results.append("value too high try again")
        elif guess < secret_number:
            results.append("value too low try again")

    if guess_count >= guess_limit and guesses[-1] != secret_number:
        results.append("oh sorry you failed all try attempt")

    return results


def main():
    print("welcome to the guessing game")
    print("I have a number between 1 and 20, can you guess?")
    print("[choice: press 1 to try, press 2 to close the game]")

    choice = input("enter choice: ")
    if choice == "2":
        print("Game closed")
    elif choice == "1":
        secret_number = random.randint(1, 20)
        guesses = []
        for _ in range(3):
            guess = int(input("enter a guess: "))
            guesses.append(guess)
        results = guess_number(secret_number, guesses)
        for result in results:
            print(result)


if __name__ == "__main__":
    main()
