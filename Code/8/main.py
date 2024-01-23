def encode(message, shift):
    cipher_text = ""
    for c in message:
        current_pos = alphabet.index(c)
        new_pos = current_pos + shift
        if new_pos >= 26:
            new_pos = (current_pos + shift) - 26

        new_letter = alphabet[new_pos]

        cipher_text += new_letter
    return cipher_text


def decode(message, shift):
    cipher_text = ""
    for c in message:
        current_pos = alphabet.index(c)
        new_pos = current_pos - shift
        if new_pos < 0:
            new_pos = (current_pos + 26) - 5

        new_letter = alphabet[new_pos]

        cipher_text += new_letter
    return cipher_text


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:

    option = input(f"Type 'encode' to encrypt, type 'decode' to decrypt:")

    message = input(f"Type your message:").lower()

    shift = int(input("Type your shift: "))

    if option == "encode":
        message = encode(message, shift)
    else:
        if option == "decode":
            message = decode(message, shift)
        else:
            print("Wrong input, try again")

    print(f"{message}")

    out = input(f"Type 'yes' if you want to go again. Otherwise type 'no'.")

    if out == "no":
        break
    else:
        if out != "yes":
            print("Wrong input, try again")
