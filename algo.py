import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes


# Generate key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Encrypt a message
message = b"salem new, Amen!"
ciphertext = private_key.public_key().encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt the message
decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f"Original Message: {message.decode()}")
print(f"Encrypted Message: {ciphertext}")
print(f"Decrypted Message: {decrypted_message.decode()}")


# Hash a string using SHA-256
data = "Hello, SHA-256!"
hashed_data = hashlib.sha256(data.encode()).hexdigest()

print(f"Original Data: {data}")
print(f"SHA-256 Hash: {hashed_data}")


# Known SHA-256 hash
known_hash = "d0e8b8f11c98f369016eb2ed3c541e1f01382f9d5b3104c9ffd06b6175a46271"

# New data to check
new_data = "Hello, Amen!"

# Calculate SHA-256 hash of the new data
new_hash = hashlib.sha256(new_data.encode()).hexdigest()

# Compare the hashes
if new_hash == known_hash:
    print("The data matches the known hash.")
else:
    print("The data does not match the known hash.")
