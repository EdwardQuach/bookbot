from stats import word_count
from stats import char_count
from stats import sort_list, sort_on, sort_test


def main():
    return print(f'Found {word_count()} total words')

print("============ BOOKBOT ============ ")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
main()
print("--------- Character Count -------")
for item in sort_list:
    print(f"{item["char"]}: {item["num"]}")
print("============= END ===============")