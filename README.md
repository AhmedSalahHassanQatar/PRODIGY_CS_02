# PRODIGY_CS_02
🔐 Pixel Manipulation for Image Encryption
📌 Introduction
This project demonstrates image encryption using pixel manipulation by swapping and modifying pixel values. Instead of traditional cryptographic methods, we use XOR operations to scramble pixel data, making the image unreadable until it is decrypted using the same technique.

This method is useful for:
✔ Basic image obfuscation for privacy protection
✔ Custom encryption experiments in cybersecurity research
✔ Understanding pixel-level image transformations

The encryption is reversible, meaning the same script can restore the original image.

🛠️ Step-by-Step Explanation of the Code
1️⃣ Load the Image
We use the Pillow (PIL) library to open an image file and convert it into a NumPy array. This allows us to manipulate pixel values directly.

python
Copy
Edit
from PIL import Image
import numpy as np

# Load the image
img = Image.open("input.jpg")  # Load the target image
img_array = np.array(img)  # Convert image to a NumPy array
2️⃣ Encrypt the Image (Pixel Manipulation)
We use XOR encryption with a numeric key to scramble pixel values.

✔ Why XOR?

It’s a lightweight encryption technique used in cryptography.

The same operation can both encrypt and decrypt the image.

python
Copy
Edit
key = 42  # Encryption key (must be the same for decryption)
encrypted_array = img_array ^ key  # XOR each pixel with the key
Each pixel’s RGB value is modified by XORing it with the key (42), making the image unrecognizable.

3️⃣ Save the Encrypted Image
We convert the modified array back into an image and save it as encrypted.png.

python
Copy
Edit
output_image = Image.fromarray(encrypted_array)  # Convert back to image
output_filename = "encrypted.png"
output_image.save(output_filename)  # Save encrypted image

print(f"Image saved as {output_filename}")
At this point, the image is encrypted and cannot be understood visually.

4️⃣ Decrypt the Image (Reversing the Process)
To decrypt, we simply run the same XOR operation again. Since XOR is reversible, applying the same key restores the original pixel values.

python
Copy
Edit
decrypted_array = encrypted_array ^ key  # XOR again with the same key
decrypted_image = Image.fromarray(decrypted_array)  # Convert back to image
decrypted_image.save("decrypted.png")  # Save decrypted image
✔ Why does this work?
XORing a value twice with the same key returns the original value:

vbnet
Copy
Edit
(A XOR K) XOR K = A
✔ Example:
If a pixel has a value of 200, and we XOR it with 42:

pgsql
Copy
Edit
200 XOR 42 = 226  (encrypted value)
226 XOR 42 = 200  (decrypted value)
This ensures that the encryption is perfectly reversible.

📌 Summary of the Process
Step	Action
1️⃣ Load Image	Open the image and convert it to an array
2️⃣ Encrypt	Apply XOR with a key to scramble pixel values
3️⃣ Save Encrypted Image	Store the encrypted result
4️⃣ Decrypt	XOR again with the same key to restore the image
5️⃣ Save Decrypted Image	Store the restored image
📂 Folder Setup
pgsql
Copy
Edit
📁 Image-Encryption-Project
   ├── 🖼 input.jpg    (Your original image)
   ├── 🔐 encrypted.png (Encrypted image)
   ├── 🔓 decrypted.png (Decrypted image)
   ├── 🐍 image_encryptor.py (Python script)
📢 Final Notes
✔ This project demonstrates pixel manipulation encryption using XOR operations.
✔ The same script encrypts and decrypts the image when run twice.
✔ You can change the encryption key to make the encryption more secure.
✔ This method is not suitable for strong security applications but is a great learning tool for image processing and encryption basics.

📜 Complete Python Script for Image Encryption & Decryption
python
Copy
Edit
# Import necessary libraries
from PIL import Image  # Used to handle image files
import numpy as np  # Used for numerical operations on images

# Define the encryption key (You can change this for stronger encryption)
KEY = 42  

# Function to encrypt an image
def encrypt_image(input_filename, encrypted_filename):
    """
    Encrypts an image using XOR pixel manipulation.
    
    Parameters:
        input_filename (str): Name of the original image file.
        encrypted_filename (str): Name of the encrypted image file to be saved.
    """
    try:
        # Load the image
        img = Image.open(input_filename)
        img_array = np.array(img)  # Convert image to NumPy array

        # Apply XOR encryption
        encrypted_array = img_array ^ KEY  

        # Convert the encrypted array back to an image
        encrypted_img = Image.fromarray(encrypted_array)
        encrypted_img.save(encrypted_filename)  # Save encrypted image

        print(f"✅ Image encrypted successfully! Saved as: {encrypted_filename}")

    except Exception as e:
        print(f"❌ Error encrypting image: {e}")

# Function to decrypt an image
def decrypt_image(encrypted_filename, decrypted_filename):
    """
    Decrypts an image using XOR pixel manipulation.
    
    Parameters:
        encrypted_filename (str): Name of the encrypted image file.
        decrypted_filename (str): Name of the decrypted image file to be saved.
    """
    try:
        # Load the encrypted image
        img = Image.open(encrypted_filename)
        img_array = np.array(img)  # Convert image to NumPy array

        # Apply XOR decryption (same operation as encryption)
        decrypted_array = img_array ^ KEY  

        # Convert the decrypted array back to an image
        decrypted_img = Image.fromarray(decrypted_array)
        decrypted_img.save(decrypted_filename)  # Save decrypted image

        print(f"✅ Image decrypted successfully! Saved as: {decrypted_filename}")

    except Exception as e:
        print(f"❌ Error decrypting image: {e}")

# Run the script
if __name__ == "__main__":
    # Define filenames
    input_image = "input.jpg"  # Change this to your image name
    encrypted_image = "encrypted.png"
    decrypted_image = "decrypted.png"

    # Encrypt the image
    encrypt_image(input_image, encrypted_image)

    # Decrypt the image
    decrypt_image(encrypted_image, decrypted_image)
