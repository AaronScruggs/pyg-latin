# Easy mode
# Create a program that when given a word, converts the word into it's pig latin version.


def translate_word(word):
    if word[0] in "aeiou":
        return word[1:] + "say"
    else:
        return "{}{}ay".format(word[1:], word[0])


word = input("Please enter a word: ").lower()

print(translate_word(word))

