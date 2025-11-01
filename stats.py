def get_num_words(text):
    list_words =text.split()
    return len(list_words)

def amount_of_characters(text):
    text_lowercase = text.lower()
    count = {}
    for n in text_lowercase:
        if n in count:
            count[n] += 1
        else:
            count[n] =1
    return count

def sort(d):
    return d["num"]

def chars_dict_to_sroted_list(num_chars_dict):
    sorted_list =[]
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort)
    return sorted_list