def get_words(path, get_text_func):
    return len(get_text_func(path).split())

def get_char_dict(path, get_text_func):
    all_text = get_text_func(path)
    char_count = {}

    for char in all_text:
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1  # Efficient counting

    return char_count

def sorted_char_list(char_dict):
    # Sort dictionary items by value (count) in descending order
    sorted_items = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Convert to list of dictionaries, filtering only alphabetic characters
    sorted_list = [{char: count} for char, count in sorted_items if char.isalpha()]
    
    return sorted_list

def pretty_report(char_dict):
    print("--------- Character Count -------")
    sorted_chars = sorted_char_list(char_dict)
    
    for item in sorted_chars:
        for char, count in item.items():
            print(f"{char}: {count}")
