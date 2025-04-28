import csv
import os
# from encrypt_decrypt_utils import decrypt  # Import your custom decrypt function

# Output CSV file path
output_file_path = os.path.join(os.path.dirname(__file__), "GIFTallHistories_ext_03_25.csv")
input_file_path = os.path.join(os.path.dirname(__file__), "giftHistories_02-01-2025.csv")

# Placeholder for data
data = []

def encrypt(text: str, shift: int) -> str:
    """
    Encrypts the text by shifting alphabetic characters by a given shift amount.
    Non-alphabetic characters remain unchanged.
    """
    result = []
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Uppercase letters
            if 'A' <= char <= 'Z':
                result.append(chr(((ord(char) - ord('A') + shift) % 26) + ord('A')))
            # Lowercase letters
            elif 'a' <= char <= 'z':
                result.append(chr(((ord(char) - ord('a') + shift) % 26) + ord('a')))
        else:
            result.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(result)


def decrypt(text: str, shift: int) -> str:
    """Decrypts text by shifting in the opposite direction."""
    return encrypt(text, -shift) 

def try_decrypting():
    print(os.path.dirname(__file__))

    # Read CSV and process data
    with open(input_file_path, mode="r", encoding="utf-8") as input_csv:
        reader = csv.reader(input_csv)
        for row in reader:
            # Process and decrypt the email field
            email = decrypt(row[2], 5).replace("\\", "v").replace("]", "w")
            data.append({
                "email": email,
                "id": row[0],
                "create_at": row[1],
                "hostname": row[3],
                "login_type": row[6],
                "domain": row[7],
                "vps": row[8],
            })

    # Write processed data to a new CSV file
    fieldnames = ["email", "id", "create_at", "hostname", "login_type", "domain", "vps"]
    with open(output_file_path, mode="w", encoding="utf-8", newline="") as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("First Row:", data[0] if data else "No Data")
    print("...Done")
    print("No more rows!")

# Run the function
if __name__ == "__main__":
    try_decrypting()
