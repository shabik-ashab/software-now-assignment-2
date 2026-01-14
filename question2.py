def encrypt_text(shift1, shift2):
    with open("raw_text.txt", "r") as infile, open("encrypted_text.txt", "w") as outfile:
        for char in infile.read():
            if char.islower():
                shift = shift1 + shift2  # consistent shift
                outfile.write(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            elif char.isupper():
                shift = shift2 ** 2  # consistent shift
                outfile.write(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            else:
                outfile.write(char)

def decrypt_text(shift1, shift2):
    with open("encrypted_text.txt", "r") as infile, open("decrypted_text.txt", "w") as outfile:
        for char in infile.read():
            if char.islower():
                shift = shift1 + shift2
                outfile.write(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            elif char.isupper():
                shift = shift2 ** 2
                outfile.write(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            else:
                outfile.write(char)

def verify_decryption():
    with open("raw_text.txt", "r") as original, open("decrypted_text.txt", "r") as decrypted:
        if original.read() == decrypted.read():
            print("Decryption successful: Files match.")
        else:
            print("Decryption failed: Files do not match.")

def main():
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    encrypt_text(shift1, shift2)
    decrypt_text(shift1, shift2)
    verify_decryption()

main()
