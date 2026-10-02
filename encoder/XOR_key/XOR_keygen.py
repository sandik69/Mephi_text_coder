import os
import secrets

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'text_data')

KEY_FILE = os.path.join(DATA_DIR, 'key2.txt')

# Длина ключа в байтах (1 байт = 8 бит)
KEY_LENGTH_BYTES = 16


def generate_key(length_bytes: int = KEY_LENGTH_BYTES,
                 sep: str = "",
                 output: str = KEY_FILE) -> str:
    """Генерирует случайный ключ и возвращает его в виде строки из 0 и 1."""
    if length_bytes <= 0:
        raise ValueError("Длина ключа должна быть > 0")

    # secrets.token_bytes — криптостойкий генератор
    raw = secrets.token_bytes(length_bytes)

    key_bits = sep.join(f"{b:08b}" for b in raw)

    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, 'w', encoding='utf-8') as f:
        f.write(key_bits)

    return key_bits


if __name__ == '__main__':
    bits = generate_key()
    print(f"Сгенерирован ключ: {KEY_LENGTH_BYTES} байт ({len(bits)} бит)")
    print(f"Файл: {KEY_FILE}")
    print(f"Ключ: {bits}")