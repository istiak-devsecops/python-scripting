# check multiple server connectivity status at once

import threading
import subprocess

def host_check(host):
    result = subprocess.run(["ping", "c", "1", host], stdout=subprocess.DEVNULL)    # run the process and store the result in a variable
    status = "UP" if result.returncode == 0 else "DOWN" # store the host status at a variable
    print(f"{host} is {status}")

hosts = ["8.8.8.8", "1.1.1.1", "192.168.1.1"]
threads = []

for host in hosts:
    t = threading.Thread(target=host_check, args=(host, ))  # target host_check function take n number of host as arguments
    threads.append(t)   # append the thread to the threads list
    t.start()   # start the thread

for t in threads:
    t.join()    # wait for thread to finish before finishes the program

print("All pings completed.")
