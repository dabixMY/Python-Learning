repeat = True

while repeat:
    text = input("Enter text <Q>uit >> ").strip().upper()
    char_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if text == "Q":
        repeat = False
    else:
        print("Binary equivalent: ", end="")
        for char in text:
            if char == " ":
                decimal = 32  # Space character
            elif char in char_list:
                # decimal = ord(text) <---- only for one char
                decimal = char_list.index(char) + 65  # Convert character to its decimal value
            else:
                continue  # Skip invalid characters such as number

            binary = bin(decimal)[2:]

            if len(binary) != 7:
                print("00" + binary, end=" ")
            else:
                print("0" + binary, end=" ")
    print()
