import subprocess
import platform
import datetime
import os

# log directory
log_dir = "/tmp/docker_prune_logs"
os.makedirs(log_dir, exist_ok=True)

# log file name with timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = os.path.join(log_dir, f"docker_prune_{timestamp}.log")

# Check OS
if platform.system().lower() == "linux":
    try:
        # Run docker system prune -a -f
        result = subprocess.run(
            ["docker", "system", "prune", "-a", "-f"],
            capture_output=True,
            text=True
        )

        # Write output and errors to log file
        with open(log_file, "w") as f:
            f.write(f"Timestamp: {timestamp}\n")
            f.write("="*60 + "\n")
            f.write("STDOUT:\n")
            f.write(result.stdout + "\n")
            f.write("STDERR:\n")
            f.write(result.stderr + "\n")
            f.write("="*60 + "\n")
            f.write("Command executed successfully.\n" if result.returncode == 0 else "Command failed.\n")

        print(f"✅ Prune completed. Log saved to {log_file}")

    except Exception as e:
        print(f"Error running docker prune: {e}")
else:
    print("This script only works on Linux.")

# Log rotation — delete logs older than 7 days
now = datetime.datetime.now()
for filename in os.listdir(log_dir):
    file_path = os.path.join(log_dir, filename)
    if os.path.isfile(file_path):
        file_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        if (now - file_time).days > 7:
            os.remove(file_path)
            print(f"🗑️ Deleted old log: {filename}")
