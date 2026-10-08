

def get_number_of_words(book_content: str) -> int :

    words_list = book_content.split()

    return len(words_list)


def count_characters(book_content: str) -> dict[str,int] :

    D={}

    for char in book_content :

        low = char.lower()

        if low in D :

            D[low]+=1

        else :

            D[low]=1 

    return D