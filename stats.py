

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


def sort_on(couple: tuple[str, int]) -> int :

    return couple[1]



def chars_dict_to_sorted_list(dictio: dict[str, int]) -> list[tuple[str, int]] :

    L = []

    for dict in dictio :

        L.append( (dict, dictio[dict]) )

    
    return sorted(L, reverse=True, key=sort_on)



        

#print(sort_on(("g", 58)))

#print(chars_dict_to_sorted_list({"k": 8, "o": 17, "!": 86}))