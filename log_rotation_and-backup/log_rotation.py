import os
from pathlib import Path
import shutil
import logging
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