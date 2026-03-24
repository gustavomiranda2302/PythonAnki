import json
import os
class JsonHandler:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_json(self):
        if not os.path.exists(self.file_path):
            return []
        else:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
    
    def save_json(self, data: list):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

        