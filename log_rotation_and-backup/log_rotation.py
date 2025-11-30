import os
from pathlib import Path
import shutil
import logging
import tarfile
from datetime import datetime, timedelta


# configuration
log_dir = Path("/var/log")
backup_dir = Path("/var/log_backup")
days_old = 7
log_file = "app.log"

# setup logging
logging.basicConfig(filename="app.log",level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s")

def find_old_logs(directory, days_old):
    time_difference = datetime.now() - timedelta(days=days_old)
    old_files = []

    for file in directory.iterdir():
        if file.is_file():
            modified = datetime.fromtimestamp(file.stat().st_mtime)
            if modified < time_difference:
                old_files.append(file)
    return old_files

def create_archive(files, backup_dir):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    archive_name = backup_dir/f"logs_{timestamp}.tar.gz"

    with tarfile.open(archive_name, "w:gz")as tar:
        for file in files:
            tar.add(file,arcname=file.name)
            logging.info(f"Rotated: {file}")

    return archive_name
