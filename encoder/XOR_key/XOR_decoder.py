import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'text_data')


def bits_to_bytes(bits: str) -> bytes:
    bits = bits.replace(" ", "").replace("\n", "").strip()
    if len(bits) % 8 != 0:
        raise ValueError("Длина битовой строки должна быть кратна 8")
    return bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))


def bytes_to_bits(data: bytes, sep: str = " ") -> str:
    return sep.join(f"{b:08b}" for b in data)


def xor_bytes(data: bytes, key: bytes) -> bytes:
    if not key:
        raise ValueError("Ключ пустой!")
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def decoder():
    # 1. Ключ
    with open(os.path.join(DATA_DIR, 'key.txt'), 'r', encoding='utf-8') as f:
        key = bits_to_bytes(f.read())
    print(f"Ключ: {len(key)} байт")

    # 2. Шифр в битах -> байты
    with open(os.path.join(DATA_DIR, 'crypt_message.txt'), 'r', encoding='utf-8') as f:
        encrypted = bits_to_bytes(f.read())

    # 3. XOR
    decrypted = xor_bytes(encrypted, key)

    # 4. Результат в битах ПОСЛЕ XOR
    decoded_bits = bytes_to_bits(decrypted)
    with open(os.path.join(DATA_DIR, 'binary_message_decoded.txt'), 'w', encoding='utf-8') as f:
        f.write(decoded_bits)
    print("Сохранено: binary_message_decoded.txt")

    # 5. Байты -> UTF-8 текст
    try:
        text = decrypted.decode('utf-8')
    except UnicodeDecodeError:
        print("Неверный ключ или повреждённый файл.")
        return

    with open(os.path.join(DATA_DIR, 'decrypt_message.txt'), 'w', encoding='utf-8') as f:
        f.write(text)
    print("Сохранено: decrypt_message.txt")
    print("Результат:", text)


if __name__ == '__main__':
    decoder()