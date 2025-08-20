import sys
from stats import word_count, count_characters, sort_dict

#book = input("What book would you like to analyze? ").lower()
#filepath = f"books/{book}.txt"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    return text.split()

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
full_text = main()

word_count(full_text)

count_characters(full_text)

sort_dict()