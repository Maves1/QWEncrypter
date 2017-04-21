abc = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
       'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
       'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
       'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

file_to_encrypt = open(input('Введите название файла, который нужно зашифровать: '), 'r')
text = file_to_encrypt.read()
file_to_encrypt.close()

# Просто создаем пустой файл
new_file = open('encoded.txt', 'w')
new_file.close()

encrypted_file = open('encoded.txt', 'a')

for letter in text:
    if letter in abc:
        letter = abc[abc.index(letter) + 1]
    encrypted_file.write(letter)

encrypted_file.close()