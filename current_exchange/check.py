import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

# Список ключей, которые мы хотим проверить
keys = [
    'SECRET_KEY',
    'POSTGRES_DB',
    'POSTGRES_USER',
    'POSTGRES_PASSWORD',
    'DB_HOST',
    'DB_PORT',
    'CBR_API_URL'
]

print("--- Проверка настроек .env ---")

for key in keys:
    value = os.getenv(key)
    if value:
        # Если это пароль или секретный ключ, можно скрыть часть для безопасности

            print(f"{key}: {value}")
    else:
        print(f"{key}: !!! НЕ НАЙДЕНО !!!")

print("------------------------------")