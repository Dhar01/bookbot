def get_book_text(path):
    """
    reading the file as string
    """
    with open(path) as f:
        return f.read()

def count_word(text):
    """
    counting the number of words
    """
    words = text.split()
    return len(words)

def count_letters(text):
    """
    this function will count the number of individual letters,
    and returns the result in dictionary form
    """
    chars = {}

    for char in text:
        lowered = char.lower()
        if lowered not in chars:
            chars[lowered] = 1
        else:
            chars[lowered] += 1

    return chars


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