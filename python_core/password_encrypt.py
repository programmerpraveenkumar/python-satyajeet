import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def get_derived_key(password: str, salt: bytes) -> bytes:
    # Stretch the password using PBKDF2 with SHA-256
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# 1. Setup your master password and generate a random salt
master_password = "my_super_secret_master_password"
salt = os.urandom(16)

# 2. Generate the encryption key
key = get_derived_key(master_password, salt)
cipher = Fernet(key)

# 3. Encrypt a password/secret
user_pwd_data = "MyPassword123!"
encrypted_data = cipher.encrypt(user_pwd_data.encode())
print("Encrypted:", encrypted_data)

# # 4. Decrypt the password/secret
# decrypted_data = cipher.decrypt(encrypted_data).decode()
# print("Decrypted:", decrypted_data)
