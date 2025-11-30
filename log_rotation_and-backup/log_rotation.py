import os
from pathlib import Path
import shutil
import datetime
import logging
from datetime import timedelta


# configuration
log_dir = Path("/var/log")
backup_dir = Path("/var/log_backup")
days_old = 7
log_file = "app.log"

# setup logging
logging.basicConfig(filename="app.log",level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s")

