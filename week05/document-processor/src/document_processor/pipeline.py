from pathlib import Path
from .models import ProcessingResult
from .utils import detect_file_type
from .processors import process_csv_file, process_json_file, process_pdf_file
from typing import List




def process_single_file(file_path: Path) -> ProcessingResult:

    detected_type= detect_file_type(file_path)

    if detected_type== "csv":
        return process_csv_file(file_path)
    elif detected_type == "json":
        return process_json_file(file_path)
    elif detected_type == "pdf":
        return process_pdf_file(file_path)
    else:
        return ProcessingResult(
            file_path=file_path,
            file_type="Unknown",
            success= False,
            error_message=f"Unsupported file: {file_path.suffix}"
        )
    



def process_multiple_files(file_paths: List[Path]) -> List[ProcessingResult]:

    processed_list= []
    for file_path in file_paths:
        processed= process_single_file(file_path)
        processed_list.append(processed)

    return processed_list