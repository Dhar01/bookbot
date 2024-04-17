def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_word(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    lowered_string = text.lower()
    for letter in lowered_string:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    return letter_count


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_word(text)
    letter_count = count_letters(text)
    # print(type(text))
    #print(text)
    print(f"{word_count} number of words found in the book")
    print(f"Letter count: {letter_count}")



main()