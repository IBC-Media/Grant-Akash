import os
import json
# import requests
from datetime import datetime
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import b64encode, b64decode
# from PIL import Image
import secrets
# import ipfshttpclient
import hashlib
from cryptography.hazmat.primitives import padding 
import os 
from decentralise import demo

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt.encode(),
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def generate_salt():
    return secrets.token_hex(16)

def encrypt_image(image_path, key):
    with open(image_path, 'rb') as f:
        image_data = f.read()

    # Pad the data to be a multiple of the block size
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(image_data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return b64encode(encrypted_data).decode()


def main(): 
    folder_path = "C:/xampp/htdocs/blob1/images"
    input_folder_path = "C:/xampp/htdocs/blob1/images"
    output_folder_path = "C:/xampp/htdocs/blob1/images_encrypted"

    image_folder = 'C:/xampp/htdocs/blob1/images'
    output_folder = 'C:/xampp/htdocs/blob1/images_encrypted'    
    password = 'datarelayx'
    salt = generate_salt()


    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_list = os.listdir(image_folder)

    encrypted_images = {}

    for image_name in image_list:
        image_path = os.path.join(image_folder, image_name)

        key = derive_key(password, salt)
        encrypted_data = encrypt_image(image_path, key)
        CID =  hashlib.sha256(encrypted_data.encode()).hexdigest()

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        encrypted_images[image_name] = {'data': encrypted_data, 'timestamp': timestamp, 'CID' : CID }

    output_json_path = os.path.join(output_folder, 'encrypted_images.json')
    with open(output_json_path, 'w') as json_file:
        json.dump(encrypted_images, json_file, indent=2)
    demo()

if __name__ == "__main__":
    main()




# import os
# import json
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from datetime import datetime

# def encrypt_image(input_path, output_path, key):
#     with open(input_path, 'rb') as file:
#         plaintext = file.read()

#     cipher = Cipher(algorithms.AES(key), modes.CFB(b'\0' * 16), backend=default_backend())
#     encryptor = cipher.encryptor()
#     ciphertext = encryptor.update(plaintext) + encryptor.finalize()

#     with open(output_path, 'wb') as file:
#         file.write(ciphertext)

# def encrypt_images_in_folder(folder_path, key):
#     encrypted_images = {}

#     for filename in os.listdir(folder_path):
#         if filename.endswith(('.jpg', '.jpeg', '.png')):
#             image_path = os.path.join(folder_path, filename)
#             encrypted_filename = f"encrypted_{filename}"
#             encrypted_path = os.path.join(folder_path, encrypted_filename)

#             encrypt_image(image_path, encrypted_path, key)

#             timestamp = str(datetime.now())
#             encrypted_images[filename] = {"encrypted_filename": encrypted_filename, "timestamp": timestamp}

#     return encrypted_images

# def save_to_json(data, output_path):
#     with open(output_path, 'w') as json_file:
#         json.dump(data, json_file, indent=4)

# if __name__ == "__main__":
#     folder_path = "C:/xampp/htdocs/blob1/images"
#     input_folder_path = "C:/xampp/htdocs/blob1/images"
#     output_folder_path = "C:/xampp/htdocs/blob1/images_encrypted"
#     key = os.urandom(16)  # Generating a random 128-bit key

#     encrypted_images = encrypt_images_in_folder(folder_path, key)

#     json_output_path = "C:/xampp/htdocs/blob1/images_encrypted/output.json"
#     save_to_json(encrypted_images, json_output_path)

#     print(f"Images encrypted successfully. Encrypted information saved to {json_output_path}.")


# import os
# import json
# import secrets

# def generate_32_byte_key():
#     # Generate a random 32-byte (256-bit) key
#     return secrets.token_bytes(32)


# # Replace this function with your actual JSON input file reading logic
# def read_input_file(input_file_path):
#     with open(input_file_path, 'r') as file:
#         input_data = json.load(file)
#     return input_data

# # Replace this function with your actual JSON object processing logic
# def process_json_object(json_obj, encryption_key):
#     # For simplicity, this example just returns the input JSON object
#     return json_obj

# # Replace this function with your actual JSON output file writing logic
# def write_output_file(output_file_path, encrypted_results):
#     with open(output_file_path, 'w') as file:
#         json.dump(encrypted_results, file, indent=2)

# # Specify the path to the folder containing images
# input_folder_path = "C:/xampp/htdocs/blob1/images"

# # Specify the path to the folder where encrypted output will be saved
# output_folder_path = "C:/xampp/htdocs/blob1/images_encrypted"

# # Ensure the output folder exists
# os.makedirs(output_folder_path, exist_ok=True)

# # List all files in the input folder
# files = os.listdir(input_folder_path)

# # Apply the provided logic to each image
# for file_name in files:
#     # Check if the file is an image (you may need to adjust this check)
#     if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
#         # Construct full paths for input and output files
#         input_file_path = os.path.join(input_folder_path, file_name)
#         output_file_path = os.path.join(output_folder_path, file_name.replace('.', '_encrypted.'))

#         # Apply the provided logic to each image
#         encryption_key = generate_32_byte_key()
#         input_data = read_input_file(input_file_path)
#         encrypted_results = [process_json_object(json_obj, encryption_key) for json_obj in input_data]
#         write_output_file(output_file_path, encrypted_results)

#         print(f"Processed {file_name}. Encrypted output saved to {output_file_path}")
