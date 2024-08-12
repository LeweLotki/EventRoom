import os
import uuid
from datetime import datetime

UPLOAD_DIR = "uploads/profile_photos"

def save_file_to_disk(file: bytes) -> str:
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    
    current_date = datetime.now().strftime("%Y%m%d")
    file_name = f"{uuid.uuid4()}_{current_date}.png"  # Save as PNG, change extension as needed
    file_path = os.path.join(UPLOAD_DIR, file_name)
    
    with open(file_path, "wb") as f:
        f.write(file)
    
    return file_path

