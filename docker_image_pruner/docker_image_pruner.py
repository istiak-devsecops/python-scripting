import subprocess
import platform
import datetime
import os
from functools import wraps

# log directory
log_dir = "/tmp/docker_prune_logs"
log_retention_days = 7
prune_command = ["docker", "system", "prune", "-a"]

def os_checker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if platform.system().lower() == "linux":
            return func(*args, **kwargs)
        else:
            print(f"skipped '{func.__name__}': not running on linux.")
            return None
    return wrapper
     

@os_checker
def rotate_logs():
    now = datetime.datetime.now()
    cutoff = now - datetime.timedelta(days=LOG_RETENTION_DAYS)

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
        return

    for filename in os.listdir(LOG_DIR):
        filepath = os.path.join(LOG_DIR, filename)
        if os.path.isfile(filepath):
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
            if mtime < cutoff:
                os.remove(filepath)
                print(f"Deleted old log: {filepath}")

@os_checker
def run_prune():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(LOG_DIR, f"prune_log_{timestamp}.txt")

    try:
        result = subprocess.run(PRUNE_COMMAND, capture_output=True, text=True, check=True)
        with open(log_file, "w") as f:
            f.write(result.stdout)
        print(f"Prune completed. Log saved to: {log_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running prune: {e.stderr}")

if __name__ == "__main__":
    rotate_logs()
    run_prune()
