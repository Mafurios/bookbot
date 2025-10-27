from stats import word_counter

def get_book_text(file_path):
    with open(file_path) as content:
        text = content.read()
    return text

def main():
    file_path = "./books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = word_counter(text)
    print(f"Found {num_words} total words")

main()
