# Hard mode
# Complete all requirements of Easy Mode, as well as being able to convert many words in a single sentence.


def translate_word(word):
    if word[0] in "aeiou":
        return word[1:] + "say"
    else:
        return "{}{}ay".format(word[1:], word[0])

def convert(writing):
    new_writing = []
    for word in writing.split():
        new_writing.append(translate_word(word.lower()))
    return " ".join(new_writing)


writing = input("Please enter some text: ")

print(convert(writing))
