def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        
    character_counts = count_characters(file_contents)
    character_counts.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{count_words(file_contents)} words found in the document\n")
    for item in character_counts:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")



def count_words(text):
    return len(text.split())


def count_characters(text):
    counts = {}
    char_list = []
    lowered_string = text.lower()
    for char in lowered_string:
        if (char not in counts) and char.isalpha():
            counts[char] = 1
        elif char.isalpha():
            counts[char] += 1
    for char, num in counts.items():
        char_list.append({"char": char, "num": num})
    return char_list
    

def sort_on(dict):
    return dict["num"]




main()

