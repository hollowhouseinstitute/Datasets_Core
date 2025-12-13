import os
import yaml

REQUIRED = [
    "title", "slug", "description", "keywords",
    "license", "version", "authors",
    "schema", "citation"
]

def validate_dataset(path):
    meta = os.path.join(path, "dataset-metadata.yaml")
    if not os.path.exists(meta):
        raise ValueError(f"Missing metadata: {path}")

    with open(meta, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    for field in REQUIRED:
        if field not in data:
            raise ValueError(f"{path}: missing {field}")

    if data["license"] != "HHI-DATA":
        raise ValueError(f"{path}: invalid license")

def main():
    root = "datasets"
    for name in os.listdir(root):
        path = os.path.join(root, name)
        if os.path.isdir(path):
            validate_dataset(path)
    print("All datasets valid.")

if __name__ == "__main__":
    main()
