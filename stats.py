def get_num_words(book_text):
    print("Text length in get_num_words: ", len(book_text))
    return len(book_text.split())

def get_char_count(book_text):
    
    #loop through text by each character
    #try to create a new dictionary entry for each character, init with the char and count of 1
    #characters that already exist in the dictionary, will increase count by one.
    char_dict = {}
    #print("Text length in get_char_count: ", len(book_text))
    #print("t: ", book_text.count('t'))
    book_text_words = book_text.split()
    book_str = "".join(book_text_words)
    for ch in book_str.lower():
        if ch in char_dict:
            char_dict[ch] = char_dict[ch] + 1
        else:
            char_dict[ch] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_list(book_char_dict):
    char_count_list = []
    
    for k, v in book_char_dict.items():
        char_count_list.append({"char": k, "num": v})
    
    char_count_list.sort(reverse=True, key=sort_on)
    
    return char_count_list
    
    
    