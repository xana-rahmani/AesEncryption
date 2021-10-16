from Cryptodome.Cipher import AES

def string_to_byte_array(string):
    return bytearray(string.encode())


try:
    encryptedFileName = input("Enter Encrypted File Name: ")
    with open('./generated_key/{}.hex.key'.format(encryptedFileName), "r") as f:
        data = f.read().split('\n')

    # convert hex data to bytes
    ciphertext = bytes.fromhex(data[0])
    tag = bytes.fromhex(data[1])
    nonce = bytes.fromhex(data[2])

    key = input("Enter Key (key_size = 16, 24, 32): ")
    key = bytearray(key.encode())

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    message_decoded = cipher.decrypt_and_verify(ciphertext, tag).decode()
    print('mnemonic: ', message_decoded)

except Exception as e:
    print('Exception: {}'.format(e.__str__()))
