test_string = '''
Elsevier helps institutions and professionals advance healthcare, open 
science and improve performance for the benefit of humanity. Combining 
content with technology, supported by operational efficiency, we turn 
information into actionable knowledge. Elsevier empowers knowledge which 
empowers those who use it.
'''

#add one blank space in the end of each line except the last line


def calculate(test_string):
    target_string1 = test_string.replace(",", "")
    target_string2 = target_string1.replace(".", "")
    target_string3 = target_string2.replace("\n", "")
    print(target_string3)
    target_list = target_string3.strip().split(" ")
    # print(target_list)
    total_length = len(target_list)
    print(total_length)
    word_dict = {}
    for word in target_list:
        if word_dict.get(word):
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    word_ratio = {key: "{:.1%}".format(value/total_length) for key, value in word_dict.items() if key not in ["and", "for", "the", "of", "with", "by", "we", "it"]}
    sorted_word_ratio = sorted(word_ratio.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_ratio


if __name__ == "__main__":
    print(calculate(test_string))
