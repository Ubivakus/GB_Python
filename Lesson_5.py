# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {text}")
# find_text = "абв"
# some_list = [i for i in text.split() if find_text not in i]
# print(f'Результат: {" ".join(some_list)}')



# _______________________________________
# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# with open('file_encode.txt', 'w') as data:
#     data.write('GGGGGOOOOQRRRIIIPPDDLLLLLLFFHCIIRRR')

# with open('file_encode.txt', 'r') as data:
#     string = data.readline()

# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string


# def rle_decode(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)

#     return decoded_string


# with open('file_encode.txt', 'r') as file:
#     decoded_string = file.read()

# with open('file_decode.txt', 'w') as file:
#     encoded_string = rle_encode(decoded_string)
#     file.write(encoded_string)

# print('Decoded string: \t' + decoded_string)
# print('Encoded string: \t' + rle_encode(decoded_string))
# print(f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')