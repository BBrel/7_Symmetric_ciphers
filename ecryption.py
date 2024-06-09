# -- шифрация и дешифрация шифра цезаря с известным ключом
def caesar(text, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    shifted_alphabet = alphabet[shift % len(alphabet):] + alphabet[:shift % len(alphabet)]
    table = str.maketrans(alphabet + alphabet.lower(), shifted_alphabet + shifted_alphabet.lower())

    return text.translate(table)


encrypted = caesar("HELLO WORLD", 3)
print("ЦЕЗАРЬ Зашифровано:", encrypted)

decrypted = caesar(encrypted, -3)
print("ЦЕЗАРЬ Дешифровано:", decrypted)


# -- шифрация и дешифрация шифра Вернама
import os


def generate_key(length):
    """ Генерирует случайный ключ равной длины с сообщением """
    return os.urandom(length)


def vernam_cipher(message, key):
    """ Шифрует или дешифрует сообщение с использованием ключа Вернама """
    if len(message) != len(key):
        raise ValueError("Ключ должен быть такой же длины, как и сообщение.")

    return bytes([m ^ k for m, k in zip(message, key)])

# Пример использования
original_message = b"Hello, World!"
key = generate_key(len(original_message))
print("ВЕРНАМА Случайный ключ:", key)

encrypted_message = vernam_cipher(original_message, key)
print("ВЕРНАМА Зашифрованное сообщение:", encrypted_message)

decrypted_message = vernam_cipher(encrypted_message, key)
print("ВЕРНАМА Расшифрованное сообщение:", decrypted_message)