from pathlib import Path


def detect_file_type(file_path: Path) -> str:

    suffix = file_path.suffix.lower()
    if suffix == ".csv":
        return "csv"
    elif suffix== ".pdf":
        return "pdf"
    elif suffix == ".json":
        return "json"
    else:
        return "Unknown"
