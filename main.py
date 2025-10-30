from stats import get_num_words
from stats import amount_of_characters
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(text)
    char_count = amount_of_characters(text)
    print(f"Found {num_words} total words")
    print(f"{char_count}")
if __name__ == "__main__":  # python
    main()    

