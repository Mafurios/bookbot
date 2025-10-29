from stats import word_counter, character_counter, data_sorter

def get_book_text(file_path): # open the book and get the full content
    with open(file_path) as content:
        text = content.read()
    return text

def main():
    library = "books/"
    book = "frankenstein"
    file_path = f"./{library}{book}.txt"
    text = get_book_text(file_path)
    num_words = word_counter(text)
    num_characters = [character_counter(text)]
    sorted_data = data_sorter(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {library}{book}.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in sorted_data:
        if character[0].isalpha() != True:
            continue
        print(f"{character[0]}: {character[1]}")
    print("============= END ===============")

main()
