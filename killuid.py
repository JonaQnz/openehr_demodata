import os
import json

BASE_DIR = "modules"

def process_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Nur wenn es ein Dict ist und uid auf oberster Ebene existiert
        if isinstance(data, dict) and "uid" in data:
            print(f"Cleaning uid in: {filepath}")
            del data["uid"]

            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

    except Exception as e:
        print(f"Error in {filepath}: {e}")

def walk_directory(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".json"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    walk_directory(BASE_DIR)
    print("Done.")