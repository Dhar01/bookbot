import sys
import os.path
from stats import (
    get_num_words,
    get_chars_dict,
    chars_dict_to_sorted_list,
)


def get_book_text(path):
    """
    reading the file as string
    """
    if not os.path.isfile(path):
        print("book doesn't exist")
        sys.exit(1)

    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def get_name():
    book = sys.argv

    if len(book) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    return book[1]

def main():
    book_path = get_name()
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


main()
