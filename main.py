def get_book_text(file_path):
    with open(file_path) as content:
        text = content.read()
    return text

def word_counter(text):
    num_words = len(text.split())
    return num_words

def main():
    file_path = "./books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = word_counter(text)
    print(f"Found {num_words} total words")

main()
