"""
Very hard mode
Complete all requirements of Hard Mode, as well as giving your program the ability to read in a pig latin string
 and output a plain english sentence. Replace first vowel characters with a "_".
"""


def translate_word(word):
    if word[0] in "aeiou":
        return word[1:] + "say"
    else:
        return "{}{}ay".format(word[1:], word[0])


def convert_to_pyglatin(writing):
    new_writing = []
    for word in writing.split():
        new_writing.append(translate_word(word.lower()))
    return " ".join(new_writing)


def back_to_english(writing):
    new_writing = []
    for word in writing.split():
        word = word.lower()
        if word[-3:] == "say":
            new_writing.append("_" + word[:-3])
        else:
            new_writing.append("{}{}".format(word[-3], word[:-3]))
    return " ".join(new_writing)


writing = input("Please enter some text: ").lower()

option = input("""
What do you want to do?
a)convert English to Pyglatin
b)convert Pyglatin to English
""").lower()

if option == 'a':
    print(convert_to_pyglatin(writing))
elif option == 'b':
    print(back_to_english(writing))
else:
    print("Not a valid option")


