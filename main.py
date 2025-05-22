import sys
from stats import get_num_words, get_char_count, get_sorted_list


def get_book_text(path):
  
  book_text = ""
  with open(path) as f:
      book_text = f.read()
      
  return book_text  

def generate_report(char_list, word_count, file_path):
  
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file_path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  
  for entry in char_list:
    print(f"{entry["char"]}: {entry["num"]}")
    
  print("============= END ===============")
     
def main():
    #rel_path_to_text = "books/frankenstein.txt"
    
    if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
    else:
      rel_path_to_text = sys.argv[1]
      
    book_text = get_book_text(rel_path_to_text)
    word_count = get_num_words(book_text)

    char_count = {}
    char_count = get_char_count(book_text)
    
    sorted_char_counts = get_sorted_list(char_count)
    generate_report(sorted_char_counts, word_count, rel_path_to_text)
    
main()
