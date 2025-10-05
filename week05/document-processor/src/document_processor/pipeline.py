from pathlib import Path
from .models import ProcessingResult
from .utils import detect_file_type
from .processors import process_csv_file, process_json_file, process_pdf_file
from typing import List
import asyncio

import logging





async def process_single_file(file_path: Path) -> ProcessingResult:

    logging.info(f"processing: {file_path}")
    detected_type= detect_file_type(file_path)

    if detected_type== "csv":
        return await process_csv_file(file_path)
    elif detected_type == "json":
        return await process_json_file(file_path)
    elif detected_type == "pdf":
        return await process_pdf_file(file_path)
    else:
        logging.warning(f"Skipping Unsupported file type: {file_path.suffix} - {file_path}")
        return ProcessingResult(
            file_path=file_path,
            file_type="Unknown",
            success= False,
            error_message=f"Unsupported file: {file_path.suffix}"
        )
    



async def process_multiple_files(file_paths: List[Path], max_concurrent: int=10) -> List[ProcessingResult]:

    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def process_with_semaphore(file_path: Path):
        async with semaphore:
            return await process_single_file(file_path)


    tasks = [process_with_semaphore(file_path) for file_path in file_paths]

    results= await asyncio.gather(*tasks)
    for result in results:
        if result.success:
            logging.info(f"✓ Success: {result.file_path.name} - {result.rows_processed} rows")
        else:
            logging.error(f"✗ Failed: {result.file_path.name} - {result.error_message}")
        

    return list(results)