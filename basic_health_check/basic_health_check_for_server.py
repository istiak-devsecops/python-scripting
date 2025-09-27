import subprocess  # Allows Python to run shell commands

def run_command(command):
    result = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    return result.stdout.strip()  # Remove leading/trailing whitespace

def check_disk_usage(): #Check disk usage using 'df -h' (human-readable format), Shows mounted filesystems and their usage.
    print("Disk Usage:")
    print(run_command("df -h"))

def check_memory_usage(): # Check memory usage using 'free -h'. Displays total, used, and free memory.
    print("\nMemory Usage:")
    print(run_command("free -h"))

def check_cpu_load(): # Check CPU load using 'uptime'.Shows system uptime and load averages.
    print("\nCPU Load:")
    print(run_command("uptime"))

def check_uptime():  # Show readable uptime using 'uptime -p'. Example: 'up 2 hours, 15 minutes'
    print("\nUptime:")
    print(run_command("uptime -p"))

if __name__ == "__main__":  # Entry point of the script
    print("Server Health Check Report\n")
    check_disk_usage()
    check_memory_usage()
    check_cpu_load()
    check_uptime()
