import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'text_data')

KEEP = {'input.txt', 'key.txt'}


def clean():
    if not os.path.isdir(DATA_DIR):
        print(f"Папка не найдена: {DATA_DIR}")
        return

    removed = 0
    for name in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, name)

        # Пропускаем то, что нужно сохранить
        if name in KEEP:
            continue

        # Удаляем только файлы (папки не трогаем)
        if os.path.isfile(path):
            os.remove(path)
            print(f"Удалён: {name}")
            removed += 1
        else:
            print(f"Пропущена папка: {name}")

    print(f"\nГотово. Удалено файлов: {removed}")
    print(f"Оставлены: {', '.join(sorted(KEEP))}")


if __name__ == '__main__':
    clean()