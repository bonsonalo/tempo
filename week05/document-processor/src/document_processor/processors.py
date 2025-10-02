from pathlib import Path
from .models import ProcessingResult
import pandas as pd
import time
import tabula



# INCLUDE THE HELPER FUNCTION HERE

def _create_error_result(file_path: Path, error: Exception, error_type: str, start_time: float):   #the _ in the first of the function name indicates that it is meant only for 
                                                                                                    #this file and will not be working for other files when this file is imported into other files.
    processing_time= time.time() - start_time

    return ProcessingResult(
        file_path=file_path,
        file_type= file_path.suffix.lower().replace(".", ""),
        success=False,
        error_message= f"{error_type}: {file_path} - {str(error)}",
        processing_time= processing_time,
        rows_processed=None
    )


def process_csv_file(file_path: Path)-> ProcessingResult:
    start_time= time.time()

    try:
        df= pd.read_csv(file_path)
        row_count= len(df)

        processing_time= time.time() - start_time

        return ProcessingResult(
            file_path=file_path,
            file_type=file_path.suffix.lower().replace(".", ""),
            success=True,
            processing_time= processing_time,
            rows_processed=row_count
    )
    except FileNotFoundError as e:  
        return _create_error_result(file_path, e, "File not found", start_time)
    except pd.errors.EmptyDataError as e:  
        return _create_error_result(file_path, e, "Empty data error", start_time)
    except pd.errors.ParserError as e:   # Occurs due to issues in parsing the file, such as malformed CSV syntax
       return _create_error_result(file_path, e, "Parsing error", start_time)
    


def process_json_file(file_path: Path)-> ProcessingResult:
    start_time= time.time()

    try:
        df= pd.read_json(file_path)
        row_count= len(df)

        processing_time= time.time() - start_time

        return ProcessingResult(
            file_path=file_path,
            file_type=file_path.suffix.lower().replace(".", ""),
            success=True,
            processing_time= processing_time,
            rows_processed=row_count
    )
    except FileNotFoundError as e:  
        return _create_error_result(file_path, e, "File not found", start_time)
    except pd.errors.EmptyDataError as e:  
        return _create_error_result(file_path, e, "Empty data error", start_time)
    except pd.errors.ParserError as e:   # Occurs due to issues in parsing the file, such as malformed CSV syntax
        return _create_error_result(file_path, e, "Parsing error", start_time)
    except ValueError as e:        # JSON decoding error
        return _create_error_result(file_path, e, "json decoding error", start_time)
    

def process_pdf_file(file_path: Path)-> ProcessingResult:
    start_time= time.time()

    try:
        tables= tabula.read_pdf(file_path, pages="all")
        row_count= sum(len(table) for table in tables)

        processing_time= time.time() - start_time

        return ProcessingResult(
            file_path=file_path,
            file_type=file_path.suffix.lower().replace(".", ""),
            success=True,
            processing_time= processing_time,
            rows_processed=row_count
    )
    except FileNotFoundError as e:  
        return _create_error_result(file_path, e, "File not found", start_time)
    except pd.errors.EmptyDataError as e:  
        return _create_error_result(file_path, e, "Empty data error", start_time)
    except pd.errors.ParserError as e:   # Occurs due to issues in parsing the file, such as malformed CSV syntax
        return _create_error_result(file_path, e, "parsing error", start_time)
    except ValueError as e:        # pdf specific issues error
        return _create_error_result(file_path, e, "pdf value error", start_time)
