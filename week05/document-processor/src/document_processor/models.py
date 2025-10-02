from pydantic import BaseModel, field_validator
from typing import Optional
from pathlib import Path
import os


class FileInfo(BaseModel):
    file_path: Path
    file_type: Optional[str]= None
    file_size: Optional[int]= None


class ProcessingResult(BaseModel):
    file_path: Path
    file_type: str
    success: bool
    error_message: Optional[str]= None
    processing_time: Optional[float]= None
    rows_processed: Optional[int]= None