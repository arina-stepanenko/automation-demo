import json
import os

def read_json(file_path):
    """Читает JSON-файл и возвращает данные"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
