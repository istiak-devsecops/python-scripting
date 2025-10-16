# run simple linux command through script

import subprocess
import platform

# take multiple value as command
def custom_command(*command): 
    if platform.system() == "Linux": # check if the system is linux
        result = subprocess.run(command, capture_output=True, text=True) # capture output and convert it into string formate
        return result.stdout.strip()    # return the output from the linux command
    else:
        return "This function will only work on Linux..."

health_check = custom_command("df", "-h")
print(health_check)
