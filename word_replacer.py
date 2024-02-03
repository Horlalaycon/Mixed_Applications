# Program Developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github https://github.com/Horlalaycon
"""
This program is used to replace a word in sentences.
"""


def replace_words(texts):
    word_to_replace = input("Enter word to replace: ")
    word_replacement = input("Enter word replacement: ")
    new_texts = texts.replace(word_to_replace, word_replacement)
    print("--------------------------------------------------------------------------")
    print(new_texts)
    print("--------------------------------------------------------------------------")


if __name__ == "__main__":
    full_texts = """
    hey bro, how are you bro
    """
    replace_words(full_texts)
