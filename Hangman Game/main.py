import hangmanwordbank,random

if __name__ == "__main__":
    random_number = random.randint(0, len(hangmanwordbank.words))
    word_to_guess = hangmanwordbank.words[random_number]
    blank_word = "_"*len(word_to_guess)
    guessed_letters = []
    lives = 0
    while True:
        current_status = hangmanwordbank.HANGMANPICS[lives]
        if lives == 6:
            print(current_status)
            print("You lose!")
            print("The word was: {}".format(word_to_guess))
            break
        print(current_status)
        print(blank_word)
        print(guessed_letters)
        str_or_char = input("Would you like to guess a word, or a letter? \nSay W for a word, or L for a letter ").upper()
        if str_or_char == "W":
            guess = input("Guess a word ")
            if guess.casefold() == word_to_guess.casefold():
                print("You win!")
                break
            else:
                print("Try again")
                lives += 1
        elif str_or_char == "L":
            guess = input("Guess a letter ")
            caseless_word = word_to_guess.casefold()
            guessed_letters.append(guess)
            if guess.casefold() in caseless_word:
                blank_list = list(blank_word)
                index = caseless_word.find(guess)
                while index != -1:
                    blank_list[index] = guess
                    index = word_to_guess.find(guess, index + 1)
                blank_word = "".join(blank_list)
            else:
                print("It's not in there!")
                lives += 1
        else:
            print("Invalid input")
