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

def sort_on(dict):
    """
    sorting dictionary contents
    """
    return dict["num"]

def dict_to_sorted_list(num_chars_dict):
    sorted_list = []

    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_word(text)
    letter_count = count_letters(text)
    letter_sorted_list = dict_to_sorted_list(letter_count)


    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in letter_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("\n--- End report ---")

main()