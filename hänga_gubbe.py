import random


guesses = 8
play = True

print("Välkommen till Hänga Gubbe!!!")

while play == True:
    spela = input("Vill du spela? ja/nej: ")

    if spela == "ja" or "Ja":
        word_list = open("words.txt", "r")
        word = random.choice(word_list.readline().split(","))
        word_guess_längd = len(word)
        word_guess = ["_"] * word_guess_längd
        delimiter = ""
        join_word_guess = delimiter.join(word_guess)
        print(join_word_guess)
        guess = input("Gissa på en bokstav!: ")

    elif spela == "nej" or "Nej":
        print("Hejdå! Ses igen")
        play = False

    else:
        ValueError
