
import sys
from stats import get_number_of_words, count_characters, chars_dict_to_sorted_list


def get_book_text(file_path: str) -> str :

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents



def print_report(book_path: str, word_count: int, sorted_list: list[tuple[str, int]]) :

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {book_path}")

    print("----------- Word Count ----------")

    print(f"Found {word_count} total words")

    print("--------- Character Count -------")

    for couple in sorted_list:

        if couple[0].isalpha() == True :

            print( f"{couple[0]}: {couple[1]}" )

    print("============= END ===============")


def check_sys():

     if len(sys.argv) < 2 :
          print("Usage: python3 main.py <path_to_book>")
          return sys.exit(1)


def main():

        check_sys()
        
        print_report(
            sys.argv[1], 
            get_number_of_words( get_book_text(sys.argv[1]) ),
            chars_dict_to_sorted_list( count_characters( get_book_text(sys.argv[1]) ) )
        )
            



main()

