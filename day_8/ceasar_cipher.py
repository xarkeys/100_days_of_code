import explanation


def challenge_explanation() -> None:
    """
    Request an explanation of the DAY 7 challenge.
    :return: A detailed explanation on what the program does.
    :rtype: None
    """
    expl_text = 'Encrypt and decrypt messages with the Ceasar Cipher. You can write your message and add your key. ' \
                'This program will then encrypt or decrypt the message. The key is used for shifting that amount of ' \
                'values.'
    expl = explanation.Explanation(expl_text, 8)
    expl.print_explanation()


def encrypt(message: str, key: int, decrypt=False) -> str:
    """
    Encrypt a message (or decrypt if the corresponding argument is provided) using the Ceasar cipher method, a key
    has to be entered as well which dictates the amount of shifting that needs to be done.
    :param key: This key is used to encrypt the message (the amount of shifting is done).
    :type key: int
    :param message: The message that needs to be encrypted.
    :type message: str
    :param decrypt: Default is False, set to True to decrypt instead of encrypt.
    :type decrypt: bool
    :return: The encrypted message, using the provided key.
    :rtype: str
    """
    encrypted_word = ''
    # The key can be as high as you want, so we reduce the shift to a value below 26. This way we can catch
    # whatever value for key is used.
    key_generalized = key % 26
    for letter in message:
        ord_letter = ord(letter)
        # First we check if the letter is uppercase and perform the shift. Else handles the shift for lowercase letters.
        if 65 <= ord_letter <= 90:
            if decrypt:
                # In case of decrypt: the new letter is the ASCII code of the first letter 'Z' - the difference.
                # Converted with chr into a letter.
                diff = (90 - ord_letter + key_generalized) % 26
                new_letter = chr(90 - diff)
            else:
                # In case of encrypt: the new letter is the ASCII code of the first letter 'A' + the difference.
                # Converted with chr into a letter.
                diff = (ord_letter - 65 + key_generalized) % 26
                new_letter = chr(65 + diff)
        else:
            if decrypt:
                # In case of decrypt: the new letter is the ASCII code of the first letter 'z' - the difference.
                # Converted with chr into a letter.
                diff = (122 - ord_letter + key_generalized) % 26
                new_letter = chr(122 - diff)
            else:
                # The difference is calculated, modulo 26 is used to check if we go beyond z and have to start at 'a'
                # again.
                diff = (ord_letter - 97 + key_generalized) % 26
                # The new letter is the ASCII code of the first letter a + the difference. Converted with chr into a
                # letter.
                new_letter = chr(97 + diff)
        encrypted_word += new_letter

    return encrypted_word
