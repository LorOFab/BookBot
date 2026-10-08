
from stats import get_number_of_words, count_characters


def get_book_text(file_path: str) -> str :

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents






def main():

    print( 

        f"Found {get_number_of_words( get_book_text("books/frankenstein.txt") )} total words"
        
    )

    print(f"{count_characters( get_book_text("books/frankenstein.txt") )}")

main()
