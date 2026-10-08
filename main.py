

def get_book_text(file_path: str) -> str :

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents



def number_of_words(book_content: str) -> int :

    words_list = book_content.split()

    return len(words_list)



def main():

    print( 

        f"Found {number_of_words ( get_book_text("books/frankenstein.txt") )} total words"
        
    )

main()
