# Snake

## Запуск игры

```bash
python main.py
```

## Компилирование
```bash
pyinstaller --onefile --noconsole --icon=snake.ico main.py -n snake
```

```bash
.\dist\snake.exe
```

## Установка зависимостей Windows

Создание виртуального окружения

```bash
python.exe -m venv venv
.\venv\Scripts\activate.bat
```

Установка зависимостей

```bash
python.exe -m pip install --upgrade pip
pip.exe install -r requirements.txt
```

## Установка зависимостей Linux

Создание виртуального окружения

```bash
python3.11 -m venv venv
. ./venv/bin/activate
```

Установка зависимостей

```bash
pip install --upgrade pip
pip install -r requirements.txt
```
