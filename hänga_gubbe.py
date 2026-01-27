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


def hänga_gubbe():
    guesses = 0
    play = True

    print("Välkommen till Hänga Gubbe!!!")

    while play:
        spela = input("Vill du spela? ja/nej: ")

        if spela.lower() == "ja":

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

                if guess in word:
                    for i, letter in enumerate(word):
                        if guess == letter:
                            word_guess[i] = guess
                    print("".join(word_guess))

                else:
                    guesses -= 1
                    print("Fel gissning! Du har", guesses, "försök kvar.")

            if "".join(word_guess) == word:
                print("Yippie du vann!! Du hade", guesses, "försök kvar!!!")

            else:
                print("Tyvärr, du förlorade. Ordet var:", word)

            play = play_again()

        elif spela.lower() == "nej":
            print("Hejdå! Ses igen")
            play = False

        else:
            raise ValueError("Du måste skriva 'ja' eller 'nej'")


if __name__ == "__main__":
    hänga_gubbe()
