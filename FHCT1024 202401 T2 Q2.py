repeat = True

while repeat:
    text = input("Enter text <Q>uit >> ").strip()
    char_list = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    upper_char_list = char_list.split(" ")
    lower_char_list = char_list.lower().split()

    if text == "Q":
        repeat = False
    else:
        print("Binary equivalent: ", end="")
        for char in text:
            if char == " ":
                decimal = 32  # Space character
            elif char in upper_char_list:
                decimal = upper_char_list.index(char) + 65  # Convert character to its decimal value
            elif char in lower_char_list:
                decimal = lower_char_list.index(char) + 97
            else:
                continue  # Skip invalid characters such as numbers

            binary_list = []
            for i in [128, 64, 32, 16, 8, 4, 2, 1]:
                if decimal >= i:
                    decimal -= i
                    binary_list.append("1")
                else:
                    binary_list.append("0")

            binary_value = "".join(binary_list)
            print(binary_value, end=" ")

    print()
