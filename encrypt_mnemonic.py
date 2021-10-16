from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


def string_to_byte_array(string):
    return bytearray(string.encode())


try:
    encryptedFileName = input("Enter Encrypted File Name (default encrypted_mnemonic): ")
    if encryptedFileName == '':
        encryptedFileName = 'encrypted_mnemonic'

    key = input("Enter Key (key_size = 16, 24, 32): ")
    key = string_to_byte_array(key)

    nonce = get_random_bytes(15)

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    data = input("Enter Mnemonic: ")
    data = string_to_byte_array(data)

    ciphertext, tag = cipher.encrypt_and_digest(data)

    print("-" * 50)
    print('Cipher Text: {}'.format(ciphertext))
    print('Tag: {}'.format(tag))
    print('Nonce: {}'.format(cipher.nonce))

    with open('./generated_key/{}.hex.key'.format(encryptedFileName), "w") as f:
        f.write(ciphertext.hex() + '\n')
        f.write(tag.hex() + '\n')
        f.write(nonce.hex())
        f.close()

except Exception as e:
    print('Exception: {}'.format(e.__str__()))
