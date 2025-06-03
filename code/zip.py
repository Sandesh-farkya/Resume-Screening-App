import msoffcrypto
import itertools
import string
from io import BytesIO

def brute_force_excel(file_path, max_length=4):
    chars = string.ascii_lowercase  # a-z
    with open(file_path, "rb") as f:
        file_data = f.read()

    for length in range(1, max_length + 1):
        print(f"Trying passwords of length {length}...")
        for pwd_tuple in itertools.product(chars, repeat=length):
            password = ''.join(pwd_tuple)
            try:
                f = BytesIO(file_data)  # reset file pointer
                office_file = msoffcrypto.OfficeFile(f)
                office_file.load_key(password=password)
                decrypted = BytesIO()
                office_file.decrypt(decrypted)
                print(f"[✓] Password found: {password}")
                return password
            except Exception:
                continue
    print("[-] Password not found.")
    return None

# Usage
file_path = "C:\\Users\\Sandesh\\Downloads\\Book1.xlsx"  # apni file ka path daaliye
brute_force_excel(file_path, max_length=4)
