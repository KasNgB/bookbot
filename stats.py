def count_words(text):
    word_list = text.split()
    num_words = len(word_list)
    return num_words


def count_character(text):
    count = {}
    all_char = set()
    for char in text:
        if char.lower() not in all_char:
            count[char.lower()] = 0
            all_char.add(char.lower())
        count[char.lower()] += 1
    return count


def sort_on(item):
    return item["num"]


def sorted_dict(count_dict):
    sorted_dict = []
    for key in count_dict:
        sorted_dict.append({"char": key, "num": count_dict[key]})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict
