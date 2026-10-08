
from stats import get_number_of_words


def get_book_text(file_path: str) -> str :

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents



def main():

    print( 

        f"Found {get_number_of_words( get_book_text("books/frankenstein.txt") )} total words"
        
    )

main()
