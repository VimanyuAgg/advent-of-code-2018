from collections import Counter

def inventory_management_system_part1(input_list):
    two_alike = 0
    three_alike = 0

    for word in input_list:
        set_two_alike = False
        set_three_alike = False

        # print("word:{}".format(word))
        word_counter = dict(Counter(word))

        for key, val in word_counter.items():

            # print("key:{}, val:{}".format(key,val))

            if not set_two_alike and (val == 2):
                two_alike += 1
                set_two_alike = True

            elif not set_three_alike and (val == 3):
                three_alike += 1
                set_three_alike = True

        # print("*****")
    return two_alike * three_alike


def compare_words(word1, word2):

    print("comparing {} & {}".format(word1,word2))

    min_len = min(len(word1),len(word2))
    one_diff = False
    result = ""
    for i in range(0,min_len):

        if word1[i] == word2[i]:
            result += word1[i]
        elif not one_diff:
            one_diff = True
            continue
        else:
            return False, result

    if len(word1) == len(word2) and one_diff:
        ## If lengths are same and we reach this point - words are alike with one off
        return True, result

    elif len(word1) != len(word2) and (not one_diff):
        ## If words are not of same length - the smaller word should match exactly
        return True, result

    else:
        return False, result



def inventory_management_system_part2(input_list):

    for i in range(0,len(input_list)):
        word1 = input_list[i]
        for j in range(i+1,len(input_list)):
            word2 = input_list[j]
            is_diff_one, result = compare_words(word1, word2)
            if is_diff_one:
                return result

    print("Should never be printed")
    return "Unknown"