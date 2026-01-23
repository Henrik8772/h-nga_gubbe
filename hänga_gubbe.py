import random


def hänga_gubbe():
    guesses = 8
    play = True

    print("Välkommen till Hänga Gubbe!!!")

    while play == True:
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
            while guesses > 0 or "".join(word_guess) != word:
                guess = input("Gissa på en bokstav!: ")
                for i, letter in enumerate(word):
                    if guess == letter:
                        word_guess[i] = guess
                        print("".join(word_guess))
                    # elif guess != letter:
                        # guessed_letters.append(guess)
                        # print("guessed letters", guessed_letters)
            if "".join(word_guess) == word:
                print("Yippie du vann!!")
                play_again = input("Vill du spela igen? ja/nej: ")
                if play_again.lower() == "ja":
                    hänga_gubbe()

                elif play_again.lower() == "nej":
                    print("Hejdå!!")
                    break

        elif spela.lower() == "nej":
            print("Hejdå! Ses igen")
            play = False

        else:
            ValueError


if __name__ == "__main__":
    hänga_gubbe()
