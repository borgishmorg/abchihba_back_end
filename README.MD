## Абчихба

Разварачивание сервиса:
```bash
sudo source deploy.sh
```

Проверка сервиса:
```bash
# Подготовка окружения
python3.9 -m venv venv
. ./venv/bin/activate
pip install -U pip
pip install -Ur requirements.txt
pip install -Ur requirements-dev.txt

# Запуск скрипта
python test.py --host 89.208.198.209 --port 4100
```

OpenAPI спецификация: [тут](http://89.208.198.209:4100/docs)