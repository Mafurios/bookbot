from stats import word_counter, character_counter

def get_book_text(file_path): # open the book and get the full content
    with open(file_path) as content:
        text = content.read()
    return text

def main():
    file_path = "./books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = word_counter(text)
    num_characters = [character_counter(text)]
    print(num_characters)
    print(f"Found {num_words} total words")

main()
