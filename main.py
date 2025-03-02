import sys
from stats import get_word_count
from stats import get_char_count
from stats import sort_char_counts
def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text= get_book_text(sys.argv[1])
    char_counts = get_char_count(book_text)
    sorted_char_counts = sort_char_counts(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")
    
    for c in sorted_char_counts:
        print(f"{c['char']}: {c['count']}")

    print("============= END ===============")
main()