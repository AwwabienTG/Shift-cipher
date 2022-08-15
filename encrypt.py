import string

all_letters_lower = list(string.ascii_lowercase)
all_letters_upper = list(string.ascii_uppercase)

def encrypt_message(message, encryption_number):

    if encryption_number > 25:
        encryption_number = encryption_number - 26
    
    if encryption_number < -25:
        encryption_number = encryption_number + 26

    new_message = ""

    def encrypt_message_helper(letter, letter_list, new_message):
        index = letter_list.index(message[letter]) + encryption_number
        if index > 25:
            index = index - 26
        new_message = new_message + letter_list[index]

        return new_message

    for letter in range(len(message)):
        if message[letter] in all_letters_lower:
            new_message = encrypt_message_helper(letter, all_letters_lower, new_message)
        elif message[letter] in all_letters_upper:
            new_message = encrypt_message_helper(letter, all_letters_upper, new_message)
        else:
            new_message = new_message + message[letter]
    
    return new_message