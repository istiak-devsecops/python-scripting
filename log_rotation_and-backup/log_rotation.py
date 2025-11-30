import os
from pathlib import Path
import shutil
import logging
import tarfile
from datetime import datetime, timedelta
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Rotate and archive old log files."
    )

    parser.add_argument(
        "--dir",
        required=True,
        help="Directory containing log files."
    )

    parser.add_argument(
        "--backup",
        required=True,
        help="Directory where archives will be stored."
    )

    parser.add_argument(
        "--days",
        type=int,
        default=7,
        help="Rotate files older than this many days (default: 7)."
    )

    parser.add_argument(
        "--logfile",
        default="app.log",
        help="Log file name for script logs (default: app.log)."
    )

    return parser.parse_args()

def setup_logging(logfile):
    logging.basicConfig(
        filename=logfile,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s"
    )

def find_old_logs(directory, days_old, logfile):
    cutoff = datetime.now() - timedelta(days=days_old)
    old_files = []

    for file in directory.iterdir():
        if file.is_file() and file.name != logfile:
            modified = datetime.fromtimestamp(file.stat().st_mtime)
            if modified < cutoff:
                old_files.append(file)

    return old_files

def create_archive(files, backup_dir):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    archive_name = backup_dir / f"logs_{timestamp}.tar.gz"

    with tarfile.open(archive_name, "w:gz") as tar:
        for file in files:
            tar.add(file, arcname=file.name)
            logging.info(f"Rotated: {file}")

    return archive_name

def main():
    args = parse_args()

    log_dir = Path(args.dir)
    backup_dir = Path(args.backup)
    days_old = args.days
    logfile = args.logfile

    setup_logging(logfile)

    if not log_dir.exists():
        print(f"Source directory does not exist: {log_dir}")
        return

    if not backup_dir.exists():
        backup_dir.mkdir(parents=True)

    old_logs = find_old_logs(log_dir, days_old, logfile)

    if not old_logs:
        print("No files to rotate.")
        logging.info("No files older than threshold.")
        return

    archive = create_archive(old_logs, backup_dir)
    print(f"Archive created: {archive}")

    # Remove old logs
    for file in old_logs:
        file.unlink()
        logging.info(f"Deleted original: {file}")

    print("Rotation complete!")

if __name__ == "__main__":
    main()