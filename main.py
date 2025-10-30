import sys
from stats import word_counter, character_counter, data_sorter

def get_book_text(file_path): # open the book and get the full content
    with open(file_path) as content:
        text = content.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = f"{sys.argv[1]}"
    text = get_book_text(file_path)
    num_words = word_counter(text)
    num_characters = [character_counter(text)]
    sorted_data = data_sorter(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in sorted_data:
        if character[0].isalpha() != True:
            continue
        print(f"{character[0]}: {character[1]}")
    print("============= END ===============")

main()
