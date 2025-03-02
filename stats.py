def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_char_count(book_text):
    char_counts = {}
    lcase_text = book_text.lower()
    
    for char in lcase_text:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_char_counts(char_counts):
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=lambda x: x["count"])
    return char_list