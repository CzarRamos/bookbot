def get_word_count(book):
    word_list = book.split()
    word_count = len(word_list)
    return word_count

def get_character_count_dict(book_contents):
    character_dict = {}
    for character in book_contents:
        current_character = character.lower()
        if current_character in character_dict:
            character_dict[current_character] += 1
        else:
            character_dict[current_character] = 1   
    return character_dict