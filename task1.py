# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect


from random import choices


def InputNumbers(inputText):
    okey = False
    while not okey:
        try:
            number = int(input(f"{inputText}"))
            okey = True
        except ValueError:
            print("Какое-то неправильное число!")
    return number


def list_rand_words(num, alp='абв'):
    words_list = []
    for i in range(num):
        letters = choices(alp, k=3)
        words_list.append("".join(letters))
    return words_list


def shows_text(li):
    res = ' '.join([str(elem) for elem in li])
    return res


def removes_characters(text):
    li = text.split(' ')
    unnecessary = 'абв'
    res_list = []
    for i in li:
        if unnecessary not in i:
            res_list.append(i)
        res = ' '.join(res_list)
    return res


num = InputNumbers("Введите количество слов: ")
li = list_rand_words(num)
text = shows_text(li)
print(text)
print(removes_characters(text))
