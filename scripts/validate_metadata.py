import yaml
import sys

REQUIRED_FIELDS = [
    "title",
    "slug",
    "description",
    "keywords",
    "license",
    "version",
    "authors",
    "schema",
    "citation"
]

def validate_metadata(path):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    missing = [f for f in REQUIRED_FIELDS if f not in data]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")

    if data["license"] != "HHI-DATA":
        raise ValueError("Invalid license reference. Must be 'HHI-DATA'.")

    print("Metadata validation passed.")

if __name__ == "__main__":
    validate_metadata(sys.argv[1])
