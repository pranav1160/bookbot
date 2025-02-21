import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)  # Exit with status code 1

frankpath = sys.argv[1]

from stats import get_words, get_char_dict, sorted_char_list, pretty_report



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

print("============ BOOKBOT ============")
print(f"Analyzing book found at {frankpath}...")
print("----------- Word Count ----------")
print(f"Found {get_words(frankpath, get_book_text)} total words")

char_dict = get_char_dict(frankpath, get_book_text)

sorted_chars = sorted_char_list(char_dict)  # Get sorted character list

pretty_report(char_dict)  # Print formatted report

print("============= END ===============")
