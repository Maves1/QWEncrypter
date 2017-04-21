abc = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
       'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
       'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
       'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def encrypt():
    file_to_encrypt = open(input('Введите название файла, который нужно зашифровать: '), 'r')
    text = file_to_encrypt.read()
    file_to_encrypt.close()

    # Просто создаем пустой файл
    new_file = open('encrypted.txt', 'w')
    new_file.close()

    encrypted_file = open('encrypted.txt', 'a')

    for letter in text:
        if letter in abc:
            try:
                letter = abc[abc.index(letter) + 1]
            except:
                pass

        encrypted_file.write(letter)

    encrypted_file.close()

def decrypt():
    file_to_decrypt = open(input('Введите название файла, который нужно расшифровать: '), 'r')
    text = file_to_decrypt.read()
    file_to_decrypt.close()

    # Просто создаем заготовку для рашифрованного файла
    new_file = open('decrypted.txt', 'w')
    new_file.close()

    decrypted_file = open('decrypted.txt', 'a')
    for letter in text:
        if letter in abc:
            if letter != 'z':
                letter = abc[abc.index(letter) - 1]

        decrypted_file.write(letter)

    decrypted_file.close()

while True:
    if input('Что вы хотите сделать? \'Зашифровать\''
             ' или \'расшифровать\'? \n').lower() == 'зашифровать':
        encrypt()
        break
    elif input('Что вы хотите сделать? \'Зашифровать\''
             ' или \'расшифровать\'? \n').lower() == 'расшифровать':
        decrypt()
        break
