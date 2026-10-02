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


def coder():
    # 1. Ключ: 0 и 1 -> байты
    with open(os.path.join(DATA_DIR, 'key.txt'), 'r', encoding='utf-8') as f:
        key = bits_to_bytes(f.read())
    print(f"Ключ: {len(key)} байт")

    # 2. Сообщение: текст UTF-8 -> байты
    with open(os.path.join(DATA_DIR, 'input.txt'), 'r', encoding='utf-8') as f:
        data = f.read().encode('utf-8')

    # 3. Текст в битах ДО XOR
    before = bytes_to_bits(data)
    with open(os.path.join(DATA_DIR, 'binary_message_before.txt'), 'w', encoding='utf-8') as f:
        f.write(before)
    print("Сохранено: binary_message_before.txt")

    # 4. XOR
    encrypted = xor_bytes(data, key)

    # 5. Шифр в битах ПОСЛЕ XOR
    after = bytes_to_bits(encrypted, sep="")
    with open(os.path.join(DATA_DIR, 'crypt_message.txt'), 'w', encoding='utf-8') as f:
        f.write(after)
    print("Сохранено: crypt_message.txt")
    print(f"Зашифровано {len(data)} байт")


if __name__ == '__main__':
    coder()