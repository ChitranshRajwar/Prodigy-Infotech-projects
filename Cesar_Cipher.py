def caesar_cipher(text, shift, mode="encrypt"):
    shift = shift % 26
    if mode == "decrypt":
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def main():
    print("===== Caesar Cipher =====")
    while True:
        message = input("Enter your message: ")
        try:
            shift = int(input("Enter shift value: "))
        except ValueError:
            print("Please enter a valid integer.\n")
            continue

        choice = input("Encrypt or Decrypt? (e/d): ").strip().lower()
        if choice == "e":
            print("Result:", caesar_cipher(message, shift, "encrypt"))
        elif choice == "d":
            print("Result:", caesar_cipher(message, shift, "decrypt"))
        else:
            print("Invalid choice!\n")
            continue

        again = input("\nRun again? (y/n): ").strip().lower()
        if again != "y":
            break


if _name_ == "_main_":
    main()
