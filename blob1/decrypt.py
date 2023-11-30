import os
import json
from datetime import datetime
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import b64decode
from PIL import Image
import hashlib
from cryptography.hazmat.primitives import padding

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt.encode(),
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def decrypt_image(encrypted_data, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    return decrypted_data

def main():
    input_json_path = 'C:/xampp/htdocs/blob1/images_encrypted/encrypted_images.json'
    output_folder = 'C:/xampp/htdocs/blob1/decrypted_images'
    password = 'datarelayx'

    with open(input_json_path, 'r') as json_file:
        encrypted_images = json.load(json_file)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for image_name, data in encrypted_images.items():
        encrypted_data = b64decode(data['data'])
        key = derive_key(password, data['CID'])

        # Print debugging information
        print(f"Image: {image_name}")
        print(f"Original Encrypted Data: {data['data']}")
        print(f"Decrypted Data: {encrypted_data}")

        try:
            decrypted_data = decrypt_image(encrypted_data, key)
            print(f"Decrypted Data (After Decryption): {decrypted_data}")
        except ValueError as e:
            # If unpadding fails, print a message or handle it as needed
            print(f"Error decrypting {image_name}: {e}")
            continue

        # Unpad the decrypted data
        unpadder = padding.PKCS7(128).unpadder()
        try:
            original_data = unpadder.update(decrypted_data) + unpadder.finalize()
            print(f"Original Data: {original_data}")
        except ValueError:
            # If unpadding fails, print a message or handle it as needed
            print(f"Error decrypting {image_name}: Invalid padding bytes.")
            continue

        output_image_path = os.path.join(output_folder, image_name)
        with open(output_image_path, 'wb') as f:
            f.write(original_data)

if __name__ == "__main__":
    main()
