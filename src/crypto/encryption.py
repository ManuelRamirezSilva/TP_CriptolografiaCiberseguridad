def encrypt(data, key):
    # Mock implementation of encryption
    return f"encrypted({data}) with key({key})"

def decrypt(encrypted_data, key):
    # Mock implementation of decryption
    return encrypted_data.replace("encrypted(", "").replace(") with key(" + key + ")", "")