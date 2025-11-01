import sys
from stats import (
    get_num_words, 
    amount_of_characters,
    chars_dict_to_sroted_list,
)

def inputs():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():

    book_path = inputs() 
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = amount_of_characters(text)
    chars_sorted_list = chars_dict_to_sroted_list(char_count)
    print_report(book_path, num_words, chars_sorted_list)

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

if __name__ == "__main__": 
    main()    

