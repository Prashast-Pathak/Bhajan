import json
from pathlib import Path

DATA_DIR = Path('data')

def normalize_all():
    files = list(DATA_DIR.glob('*.json'))
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except Exception as e:
                print(f"Error loading {f.name}: {e}")
                continue
            
        if isinstance(data, list) and len(data) > 0:
            schema = {}
            # infer schema from first item
            for k, v in data[0].items():
                if isinstance(v, list): schema[k] = []
                elif isinstance(v, dict): schema[k] = {}
                elif isinstance(v, str): schema[k] = ""
                elif isinstance(v, bool): schema[k] = False
                elif isinstance(v, int): schema[k] = 0
                else: schema[k] = None
            
            # normalize all items
            new_data = []
            for item in data:
                new_item = {}
                for k, default_val in schema.items():
                    if k in item and item[k] is not None:
                        new_item[k] = item[k]
                    else:
                        if isinstance(default_val, list): new_item[k] = []
                        elif isinstance(default_val, dict): new_item[k] = {}
                        else: new_item[k] = default_val
                # copy extra keys
                for k in item:
                    if k not in schema:
                        new_item[k] = item[k]
                new_data.append(new_item)
            
            with open(f, 'w', encoding='utf-8') as out:
                json.dump(new_data, out, ensure_ascii=False, indent=2)
            print(f"Normalized list in {f.name}")
            
        elif isinstance(data, dict):
            # Probably wrapped like {"prayers": [...]}
            for root_key, arr in data.items():
                if isinstance(arr, list) and len(arr) > 0 and isinstance(arr[0], dict):
                    schema = {}
                    for k, v in arr[0].items():
                        if isinstance(v, list): schema[k] = []
                        elif isinstance(v, dict): schema[k] = {}
                        elif isinstance(v, str): schema[k] = ""
                        elif isinstance(v, bool): schema[k] = False
                        elif isinstance(v, int): schema[k] = 0
                        else: schema[k] = None
                    
                    new_arr = []
                    for item in arr:
                        new_item = {}
                        for k, default_val in schema.items():
                            if k in item and item[k] is not None:
                                new_item[k] = item[k]
                            else:
                                if isinstance(default_val, list): new_item[k] = []
                                elif isinstance(default_val, dict): new_item[k] = {}
                                else: new_item[k] = default_val
                        # copy extra keys
                        for k in item:
                            if k not in schema:
                                new_item[k] = item[k]
                        new_arr.append(new_item)
                    data[root_key] = new_arr
            with open(f, 'w', encoding='utf-8') as out:
                json.dump(data, out, ensure_ascii=False, indent=2)
            print(f"Normalized dict arrays in {f.name}")

if __name__ == '__main__':
    normalize_all()
