# Message chiffré
import itertools
encrypted_message = [3, 14, 0, 12, 0, 69, 41, 9, 7, 63, 3, 52, 44, 29, 42, 2, 13, 84, 7, 38, 27, 33, 0, 31, 49, 36, 25, 11, 41, 89, 56, 4, 46, 33, 78, 58, 20, 38, 22, 57, 32, 2, 89, 21, 32, 23, 13, 78, 25, 24, 39, 4, 4, 42, 9, 89, 17, 17, 67, 2, 15, 0, 81, 5, 32, 2, 43, 25, 89, 0, 42, 22, 60, 78, 4, 52, 6, 69, 20, 32, 15, 44, 25, 0, 45, 28, 61, 35, 20, 85, 11, 53, 28, 45, 16, 7, 69, 19, 41, 29, 10, 62, 24, 40, 21, 1, 24, 89, 18, 36, 10, 26, 11, 25, 62, 0, 55, 80, 3, 41, 10, 6, 32, 0, 61, 30, 44, 3, 48, 23, 80, 5, 41, 89, 7, 48, 10, 27, 10, 44, 2, 48, 22, 32, 10, 30, 28, 49, 0, 51, 7, 27, 59, 3, 60, 0, 42, 79, 26, 54, 1, 22, 14, 41, 7, 45, 20, 39, 69, 3, 38, 0, 15, 59, 16, 48, 72, 30, 37, 16, 60, 17, 80, 5, 41, 89, 2, 42, 22, 59, 11, 39, 81, 6, 32, 2, 46, 5, 42, 0, 55, 6, 59, 28, 44, 18, 58, 11, 62, 14, 37, 10, 39, 4, 13, 60, 4, 44, 81, 35, 0, 37, 23, 30, 60, 23, 48, 19, 45, 28, 44, 3, 85, 8, 53, 28, 8, 54, 23, 48, 14, 13, 32, 29, 34, 85, 21, 60, 42, 13, 10, 17, 75]

# Fonction de déchiffrement par XOR
def decrypt(message, key):
    decrypted_message = [char ^ key[i % len(key)] for i, char in enumerate(message)]
    return decrypted_message

# Essai de mots de passe possibles
for password_length in range(10, 16):
    for password in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=password_length):
        password = ''.join(password)
        decrypted_message = decrypt(encrypted_message, [ord(char) for char in password])

        # Vérification si le message déchiffré se termine par "ase."
        if decrypted_message[-4:] == [97, 115, 101, 46]:  # Correspond à "ase."
            print(f"Mot de passe trouvé: {password}")
            print("Message déchiffré:", ''.join(chr(char) for char in decrypted_message))
            break
