import sys

from stats import count_character, count_words, sorted_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    for item in sorted_dict(count_character(get_book_text(sys.argv[1]))):
        if item["char"].isalpha() is True:
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
