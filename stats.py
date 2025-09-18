letters = {}
list = []
def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def word_count():
    text = get_book_text()
    words = text.split()
    return len(words)

def char_count():
    text = get_book_text()
    words = text.split()
    for word in words: 
        for char in word:
            lower_case_char = char.lower()
            if lower_case_char not in letters:
                letters[lower_case_char] = 1
            else:letters[lower_case_char] += 1
    return letters

def sort_test():
    char_count()
    for letter in letters:
        list.append({"char":letter, "num": letters[letter]})
    return list

def sort_on(items):
    return items["num"]

sort_list = sort_test()
sort_list.sort(reverse=True, key=sort_on)
