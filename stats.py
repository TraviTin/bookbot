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



