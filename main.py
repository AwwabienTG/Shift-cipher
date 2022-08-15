import encrypt

print("Welcome to my shift cipher program!")

while True:
    print("-------------------------------------------------------")
    response = input("Enter 1 for encryption and 2 for decryption: ")
    message = input("Enter the message you want to encrypt/decrypt: ")
    encryption_number = int(input("Enter the shift: "))

    try:
        if response == "1":
            print("Your encrypted message is: " + encrypt.encrypt_message(message, encryption_number))
        elif response == "2":
            print("Your decrypted message is: " + encrypt.encrypt_message(message, -abs(encryption_number)))
        else:
            print("Invalid response, Try Again!")
    except:
        print("You have entered an invalid input, Try Again!")
