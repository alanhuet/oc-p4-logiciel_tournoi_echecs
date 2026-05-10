
import json
import os
from pathlib import Path

class StorageManager:
    def __init__(self, filename):
        self.base_dir = Path(__file__).resolve().parent.parent
        self.data_dir = self.base_dir / "data"
        self.filepath = self.data_dir / f"{filename}.json"
        
        if not self.data_dir.exists():
            self.data_dir.mkdir(parent=True, exist_ok=True)

    def save(self, data):
        """ Stores a list of objects converted into dictionaries. """
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load(self):
        """ Loads data from the JSON file. """
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
        