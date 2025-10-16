# generate a timestamped system report

import os
import platform
import datetime
import subprocess

time_stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # mapped format for filename
filename = f"health_snapshot_{time_stamp}.txt"  # actual filename with mapped time format

system_info = {"OS": platform.system(), "Release": platform.release(), "Architecture": platform.machine(), "Timestamp": time_stamp} # store system info into a dictionary


# function to run the linux command
def linux_command(*command):    
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()

disk_usages_output = linux_command("df", "-h")  # stored disk usages
uptime_output = linux_command("uptime")         # stored uptime
memory_usages_output = linux_command("free", "-m")  # stored memory usages


# saved the output into a file
with open(filename, "w")as file:
    file.write("$$$ Author: MD ISTIAK AHMED $$$\n###############################\n") # showcase script writer name at the top
    file.write("\n=== System Info ===\n")
    for key, value in system_info.items():
        file.write(f"{key}: {value}\n")
    
    file.write("\n=== Disk Usage (df -h) ===\n")
    file.write(f"{disk_usages_output}\n")

    file.write(f"\n=== Uptime ===\n")
    file.write(f"{uptime_output}\n")

    file.write(f"\n=== Memory usages ===\n")
    file.write(f"{memory_usages_output}\n")

print(f"System health snapshot saved to {filename}")