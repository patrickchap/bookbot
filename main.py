def words_in_book(file_contents):
    words = file_contents.split()
    return len(words)

def characters_in_book(file_contents):
    file_contents = file_contents.lower()
    char_count = {}
    for i in file_contents:
        if i.isalpha() == False:
            continue

        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count

def sort_on(dict):
    return dict["count"]

def characters_in_book_list(characters_in_book):
    chars = []
    for key, value in characters_in_book.items():
        dict = {}
        dict['name'] = key
        dict['count'] = value 
        chars.append(dict)

    chars.sort(reverse=True, key=sort_on) 
    return chars

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = words_in_book(file_contents)
        character_count = characters_in_book(file_contents)
        print(f"--- Begin report of {path_to_file} ---")
        print(f"{word_count} words found in the document")

        for i in characters_in_book_list(character_count):
            print(f"The '{i['name']}' character was found {i['count']} times")

        print("--- End report ---")

main()
