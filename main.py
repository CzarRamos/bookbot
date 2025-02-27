import sys
from stats import get_word_count
from stats import get_character_count_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        # print(f.read())
        return file_contents
    
def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at books/frankenstein.txt...")
        book_string = get_book_text(sys.argv[1])

        print("----------- Word Count ----------")
        word_count = get_word_count(book_string)
        print(f"Found {word_count} total words")

        print("--------- Character Count -------")
        character_dict = get_character_count_dict(book_string)
        for character in character_dict:
            if character.isalpha() == True:
                print(f"{character}: {character_dict[character]}")
        print("============= END ===============")

main()
