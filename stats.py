def word_counter(text): # take book content and count all words
    num_words = len(text.split())
    return num_words

def character_counter(text): # take book content and count all characters ignoring capitalization
    num_characters = {}

    lowered_text = text.lower()
    for character in list(lowered_text):
        if character in num_characters:
            num_characters[character] += 1
        else:
            num_characters[character] = 1
    return num_characters

def data_sorter(num_characters): # take counted characters and sort them by amount (descending)
    character = num_characters[0]
    sorted_data = sorted(character.items(), key=lambda x: x[1], reverse=True)
    return sorted_data