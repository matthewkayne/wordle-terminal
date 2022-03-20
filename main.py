import random
from functools import partial
from termcolor import colored


def ordinal(n):
    """Ordinal"""
    return "%d%s" % (n, "tsnrhtdd"[(n//10 % 10 != 1)*(n % 10 < 4)*n % 10::4])


file = open("words.txt", "r")
wordList2D = [(line.strip()).split() for line in file]
file.close()
wordList = []

for i in range(len(wordList2D)):
    wordList.append(wordList2D[i][0])

word = list(wordList[random.randint(0, len(wordList)-1)])


def green(text):
    """Green"""
    return colored(text, "green", attrs=['reverse', 'blink'])


def yellow(text):
    """Yellow"""
    return colored(text, "yellow", attrs=['reverse', 'blink'])


def grey(text):
    """Grey"""
    return colored(text, "white", attrs=['reverse', 'blink'])


for i in range(5):
    greens = [None, None, None, None, None]
    yellows = [None, None, None, None, None]
    greys = [None, None, None, None, None]

    while True:
        guess = input(f"\nGuess {i+1}: ").lower()
        if len(guess) != 5:
            print("5 Letters Exactly!")
        elif guess not in wordList:
            print("Not In Word List")
        else:
            break

    guessChar = list(guess)

    for character in range(len(word)):
        if guessChar[character] == word[character]:
            greens[character] = word[character]
    for character in range(len(word)):
        if (guessChar[character] in word) and (guessChar[character] not in greens) and (guessChar[character] not in yellows):
            yellows[character] = guessChar[character]
    for character in range(len(word)):
        if greens[character] is None and yellows[character] is None:
            greys[character] = guessChar[character]

    output = [None, None, None, None, None]

    for item in range(len(greens)):
        if greens[item] is not None:
            output[item] = partial(green, greens[item])
    for item in range(len(yellows)):
        if yellows[item] is not None:
            output[item] = partial(yellow, yellows[item])
    for item in range(len(greys)):
        if greys[item] is not None:
            output[item] = partial(grey, greys[item])

    for out in range(len(output)):
        print(output[out](), end="")

    if None in greens:
        pass
    else:
        print("\nCongrats That's Correct!!!")
        print(f"You got it on your {ordinal(i+1)} try!")
        break
print("\nThe End")
