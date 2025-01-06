def count_words(input_string: str) -> dict:
    word_count = {}
    cleaned_input = input_string.replace(".", "").lower()
    split_words = cleaned_input.split()
    for word in split_words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


input_1 = "Simple is better than complex. Complex is better than complicated."
input_2 = "If the implementation is hard to explain, it is a bad idea. If the implementation is easy to explain, it may be a good idea."
input_3 = "You are never too old to set another goal or to dream a new dream"
input_str = input_3
print(count_words(input_str))
