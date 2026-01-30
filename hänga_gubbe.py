import random


def play_again():
    while True:
        play_again_input = input("Vill du spela igen? ja/nej: ").lower()
        if play_again_input == "ja":
            return True
        elif play_again_input == "nej":
            print("Hejdå!!")
            return False
        else:
            print("Var snäll och skriv 'ja' eller 'nej'.")
            play_again()


def play_game():
    print("Välkommen till Hänga Gubbe!!!")
    spela = input("Vill du spela? ja/nej: ").lower()
    if spela == "ja":
        hänga_gubbe()
    elif spela == "nej":
        print("Okej, hejdå!")
        exit
    else:
        print("Skriv antingen 'ja' eller 'nej'")
        play_game()


def hänga_gubbe():
    guesses = 0
    play = True

    while play:

        guessed_letters = []

        word_list = open("words.txt", "r")
        word = random.choice(word_list.readline().split("," " "))

        word_length = len(word)
        word_guess = ["_"] * len(word)

        delimiter = ""
        join_word_guess = delimiter.join(word_guess)

        print("Ordet har", word_length, "bokstäver")
        print(join_word_guess)

        guesses = word_length * 2

        while guesses > 0 and "".join(word_guess) != word:
            guess = input("Gissa på en bokstav!: ")

            if guess in word and guess not in guessed_letters:

                for i, letter in enumerate(word):
                    if guess == letter:
                        word_guess[i] = guess
                print("".join(word_guess))

            elif len(guess) != 1:
                print("Skriv EN bokstav.")
                continue

            elif guess in guessed_letters:
                print("Denna bokstav har du redan använt")
                continue

            else:
                guesses -= 1
                print("Fel gissning! Du har", guesses, "försök kvar.")

            guessed_letters.append(guess)
            print("Dessa bokstäver har du använt:")
            print(", ".join(guessed_letters))

        if "".join(word_guess) == word:
            print("Yippie du vann!! Du hade", guesses, "försök kvar!!!")

        else:
            print("Tyvärr, du förlorade. Ordet var:", word)

        play = play_again()


if __name__ == "__main__":
    play_game()
