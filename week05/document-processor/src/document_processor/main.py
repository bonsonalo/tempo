
import asyncio
from pathlib import Path
from .config import setup_logging
from .pipeline import process_multiple_files
import sys

def main():
    setup_logging()
    
    # get folder from command line argument
    if len(sys.argv) < 2:
        print("Usage: python -m document_processor <folder_path>")
        sys.exit(1)
    
    folder = Path(sys.argv[1])
    
    if not folder.exists():
        print(f"Error: Folder {folder} doesn't exist")
        sys.exit(1)
    
    # get all files
    files = list(folder.glob("*"))
    print(f"Found {len(files)} files")
    
    # Process them
    results = asyncio.run(process_multiple_files(files))
    
    # Summary
    success_count = sum(1 for r in results if r.success)
    print(f"\nProcessed {len(results)} files: {success_count} succeeded, {len(results)-success_count} failed")

if __name__ == "__main__":
    main()