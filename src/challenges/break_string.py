"""
Given a string s, break s such that every substring of the partition can be found in the dictionary.
Return the minimum break needed.

Example:
    Given a String CatMat
    Given a dictionary ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
    return 1

    We can break the sentences in three ways, as follows:
    CatMat = Cat Mat break 1
    CatMat = Ca tM at break 2
    CatMat = C at Mat break 2
    But the first way has the minimum break, thus return 1

https://www.careercup.com/question?id=5682428306784256
"""


def break_string(string, word_list):
    word_list = [word for word in word_list if word in string]

    if len(word_list) == 0:
        raise Exception()

    if len(word_list) == 1 and word_list[0] == string:
        return 0

    word_list.sort(key=len, reverse=True)

    breaks = 0

    for word in word_list:
        if word not in string:
            continue
        try:
            if string.replace(word, ''):
                break_string(string.replace(word, ''), word_list)
        except Exception:
            continue
        else:
            string = string.replace(word, '')
            if not string:
                return breaks
            else:
                breaks += 1

    if string:
        raise Exception()

    return breaks
