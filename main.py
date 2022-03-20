import random
from functools import partial
from termcolor import colored


def ordinal(var):
    """Ordinal"""
    return "%d%s" % (var, "tsnrhtdd"[(var//10 % 10 != 1)*(var % 10 < 4)*var % 10::4])


with open("words.txt", "r") as file:
    wordList2D = [(line.strip()).split() for line in file]

file.close()
wordList = []

for i, _ in enumerate(wordList2D):
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

    for character, _ in enumerate(word):
        if guessChar[character] == word[character]:
            greens[character] = word[character]
    for character, _ in enumerate(word):
        if (guessChar[character] in word) and (guessChar[character] not in greens) and (guessChar[character] not in yellows):
            yellows[character] = guessChar[character]
    for character, _ in enumerate(word):
        if greens[character] is None and yellows[character] is None:
            greys[character] = guessChar[character]

    output = [None, None, None, None, None]

    for item, _ in enumerate(greens):
        if greens[item] is not None:
            output[item] = partial(green, greens[item])
    for item, _ in enumerate(yellows):
        if yellows[item] is not None:
            output[item] = partial(yellow, yellows[item])
    for item, _ in enumerate(greys):
        if greys[item] is not None:
            output[item] = partial(grey, greys[item])

    for out, _ in enumerate(output):
        print(output[out](), end="")

    if None in greens:
        pass
    else:
        print("\nCongrats That's Correct!!!")
        print(f"You got it on your {ordinal(i+1)} try!")
        break
print("\nThe End")
