import base64

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

def encrypt_flag(file_path, shift):
    try:
        # 讀取flag檔案
        with open(file_path, 'r') as file:
            flag = file.read().strip()
        
        # 使用凱薩密碼加密
        encrypted_flag = caesar_cipher(flag, shift)
        
        # 使用base64編碼
        base64_encoded = base64.b64encode(encrypted_flag.encode()).decode()
        
        return base64_encoded
    except FileNotFoundError:
        return "錯誤：找不到指定的檔案。"
    except Exception as e:
        return f"錯誤：{str(e)}"


file_path = "flag"
shift = 3 

result = encrypt_flag(file_path, shift)
print("flag:", result)