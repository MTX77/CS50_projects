from cs50 import get_string

print("Program that computes the approximate grade level needed to comprehend some text.")
text = get_string("Text: ").lower()

letters = list()
words = text.split()
sentences_count = 0

for index, word in enumerate(words):
    if len(word) == 1 and word.isalpha() == False:
        words.pop(index)

for word in words:
    for letter in word:
        if letter == "." or letter == "!" or letter == "?":
            sentences_count += 1
        if letter.isalpha() or letter.isdigit():
            letters.append(letter)

letters_count = len(letters)
words_count = len(words)

# print(letters_count)
# print(words_count)
# print(sentences_count)

L = letters_count / words_count * 100
S = sentences_count / words_count * 100

index = round(0.0588 * L - 0.296 * S - 15.8)

if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
