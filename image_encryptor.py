from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Open the image
    img = Image.open(input_path)
    img_array = np.array(img)  # Convert image to NumPy array
    
    # Apply XOR encryption
    encrypted_array = img_array ^ key  # XOR operation with key
    
    # Convert back to image
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(encrypted_path, output_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_path)
    encrypted_array = np.array(encrypted_img)
    
    # Apply XOR decryption (same operation as encryption)
    decrypted_array = encrypted_array ^ key
    
    # Convert back to image
    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_img.save(output_path)
    print(f"Decrypted image saved as {output_path}")

# Example Usage
key = 200  # Change this for better security

encrypt_image("Red and Blue Pill.jpeg", "encrypted.png", key)
decrypt_image("encrypted.png", "decrypted.png", key)
