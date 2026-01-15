def encrypt_text(shift1, shift2):
    with open("raw_text.txt", "r") as infile, open("encrypted_text.txt", "w") as outfile:
        for char in infile.read():
            if char.islower():
                if 'a' <= char <= 'm':
                    shift = shift1 * shift2
                    outfile.write(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
                else:
                    shift = shift1 + shift2
                    outfile.write(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            elif char.isupper():
                if 'A' <= char <= 'M':
                    shift = shift1
                    outfile.write(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
                else:                        
                    shift = shift2 ** 2
                    outfile.write(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            else:
                outfile.write(char)
 
def decrypt_text(shift1, shift2):
    with open("encrypted_text.txt", "r") as infile, open("decrypted_text.txt", "w") as outfile:
        for enc_char in infile.read():
            if enc_char.islower() or enc_char.isupper():
                # Try all 26 letters as candidate
                for i in range(26):
                    if enc_char.islower():
                        candidate = chr(i + ord('a'))
                        if 'a' <= candidate <= 'm':
                            result = chr((ord(candidate) - ord('a') + shift1 * shift2) % 26 + ord('a'))
                        else:
                            result = chr((ord(candidate) - ord('a') - (shift1 + shift2)) % 26 + ord('a'))
                    else:
                        candidate = chr(i + ord('A'))
                        if 'A' <= candidate <= 'M':
                            result = chr((ord(candidate) - ord('A') - shift1) % 26 + ord('A'))
                        else:
                            result = chr((ord(candidate) - ord('A') + (shift2 ** 2)) % 26 + ord('A'))
                    if result == enc_char:
                        outfile.write(candidate)
                        break
            else:
                outfile.write(enc_char)
 
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