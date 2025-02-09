def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_characters(text)
    chars_list = [{"char": key, "num": value} for key, value in chars_dict.items()]
    chars_list.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    report(chars_list)

    print("--- End report ---")    

def report(chars_list):
    for char_info in chars_list:
        char = char_info["char"]
        num = char_info["num"]
        print(f"The '{char}' character was found {num} times")
                  

def sort_on(chars_list):
        return chars_list["num"]


def get_num_characters(text):
    lowered_text = text.lower()
    chars = {}       
    for char in lowered_text:
        if char.isalpha() == True:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()