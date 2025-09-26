import subprocess

def run_command(command):
    """Run a shell command and return its output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def check_disk_usage():
    print("🔍 Disk Usage:")
    print(run_command("df -h"))

def check_memory_usage():
    print("\n🧠 Memory Usage:")
    print(run_command("free -h"))

def check_cpu_load():
    print("\n⚙️ CPU Load:")
    print(run_command("uptime"))

def check_uptime():
    print("\n⏱️ Uptime:")
    print(run_command("uptime -p"))

if __name__ == "__main__":
    print("📋 Server Health Check Report\n")
    check_disk_usage()
    check_memory_usage()
    check_cpu_load()
    check_uptime()
