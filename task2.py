# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

from itertools import groupby, starmap

def encodes_text(input_text, input_code):
    with open((input(f"{input_text}")), "a") as text_words,\
        open((input(f"{input_code}"))) as text_code:
        for i in text_code:
            text_words.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))



def decode_text(input_text):
    with open((input(f"{input_text}"))) as my_file:
        res = ""
        for i in my_file:
            word_nums = []
            for j in i.strip():
                if j.isdigit():
                    res += j
                else:
                    word_nums.append([int(res), j])
                    res = ""
        print("".join(starmap(lambda x, y: x * y, word_nums)))
     


encodes_text("Введите название новго файла для записи: ", "Введите название файла c текстом: ")
decode_text("Введите имя файла для декодирования: ")
