#My inital code

char_count = {}

def word_count(full_text):
    num_words = len(full_text)
    print(f"Found {num_words} total words")
    
def count_characters(full_text):
    for i in full_text:
        word = list(i)
        for c in word:
            char = c.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

def sort_dict():
    sorted_items = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_items)
    for key, value in sorted_dict.items():
        if key.isalpha() == True:
            print(f"{key}: {value}")
        else:
            pass

#Boot.dev version

#Counts the words in the text file
# def get_num_words(text):
#     words = text.split
#     return len(words)

#Creates the characters dictionary
# def get_chars_dict(text):
#     chars = {}
#     for c in text:
#         lowered = c.lowered()
#         if lowered in chars:
#             chars[lowered] += 1
#         else:
#             chars[lowered] = 1
#     return chars

#What is this doing?
# def sort_on(d):
#     return d["num"]

#Creates the sorted list from the dictionary
# def chars_dict_to_sorted_list(num_chars_dict):
#     sorted_list = []
#     for ch in num_chars_dict:
#         sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
#     sorted_list.sort(reverse=True, key=sort_on)
#     return sorted_list
