# Program Developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github https://github.com/Horlalaycon
"""
This program is used to replace a word in sentences.
"""

texts = """
hey bro, how are you bro
"""
word_to_replace = input("Enter word to replace: ")
word_replacement = input("Enter word replacement: ")
new_texts = texts.replace(word_to_replace, word_replacement)
print(new_texts)
