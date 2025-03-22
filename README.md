# PRODIGY_CS_02
### 🔐 Pixel Manipulation for Image Encryption

### 📌 Introduction
This project demonstrates image encryption using pixel manipulation by swapping and modifying pixel values. Instead of traditional cryptographic methods, we use XOR operations to scramble pixel data, making the image unreadable until it is decrypted using the same technique.

This method is useful for:

✔ Basic image obfuscation for privacy protection

✔ Custom encryption experiments in cybersecurity research

✔ Understanding pixel-level image transformations

The encryption is reversible, meaning the same script can restore the original image.

🛠️ Step-by-Step Explanation of the Code

1️⃣ Load the Image
We use the Pillow (PIL) library to open an image file and convert it into a NumPy array.
This allows us to manipulate pixel values directly.

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

key = 42  # Encryption key (must be the same for decryption)
encrypted_array = img_array ^ key  # XOR each pixel with the key
Each pixel’s RGB value is modified by XORing it with the key (42), making the image unrecognizable.

3️⃣ Save the Encrypted Image

We convert the modified array back into an image and save it as encrypted.png.

output_image = Image.fromarray(encrypted_array)  # Convert back to image
output_filename = "encrypted.png"
output_image.save(output_filename)  # Save encrypted image

print(f"Image saved as {output_filename}")
At this point, the image is encrypted and cannot be understood visually.

4️⃣ Decrypt the Image (Reversing the Process)
To decrypt, we simply run the same XOR operation again. Since XOR is reversible, applying the same key restores the original pixel values.


decrypted_array = encrypted_array ^ key  # XOR again with the same key
decrypted_image = Image.fromarray(decrypted_array)  # Convert back to image
decrypted_image.save("decrypted.png")  # Save decrypted image

✔ Why does this work?
XORing a value twice with the same key returns the original value:

(A XOR K) XOR K = A

✔ Example:
If a pixel has a value of 200, and we XOR it with 42:


200 XOR 42 = 226  (encrypted value)
226 XOR 42 = 200  (decrypted value)
This ensures that the encryption is perfectly reversible.

📌 Summary of the Process

1️⃣ Step: Load Image		           | Action: Open the image and convert it to an array

2️⃣ Step: Encrypt	                 | Action: Apply XOR with a key to scramble pixel values

3️⃣ Step: Save Encrypted Image	     | Action: Store the encrypted result

4️⃣ Step: Decrypt                   | Action: XOR again with the same key to restore the image

5️⃣ Step: Save Decrypted Image    |   Action: Store the restored image

📂 Folder Setup

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

