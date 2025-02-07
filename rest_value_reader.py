#!/usr/bin/env python
"""
Simple value collector from REST Interface

Feb 2025 xaratustrah@github

"""

import threading
import requests
import time
import json

url1 = "path to your server and device 1"
url2 = "path to your server and device 2"

# Shared variables
shared_variable1 = {}
shared_variable2 = {}

# Function to update the first shared variable
def update_variable1():
    global shared_variable1
    s = requests.Session()
    r = s.get(url1, stream=True)
    for line in r.iter_lines():
        if line:
            byte_array_str = line.decode("utf-8")
            json_str = byte_array_str.replace("data: ", "")
            shared_variable1 = json.loads(json_str)

# Function to update the second shared variable
def update_variable2():
    global shared_variable2
    s = requests.Session()
    r = s.get(url2, stream=True)
    for line in r.iter_lines():
        if line:
            byte_array_str = line.decode("utf-8")
            json_str = byte_array_str.replace("data: ", "")
            shared_variable2 = json.loads(json_str)

# Create and start the first thread
update_thread1 = threading.Thread(target=update_variable1)
update_thread1.daemon = True  # Daemon thread will exit when the main program exits
update_thread1.start()

# Create and start the second thread
update_thread2 = threading.Thread(target=update_variable2)
update_thread2.daemon = True  # Daemon thread will exit when the main program exits
update_thread2.start()

# Main thread to print the latest values of the variables every second
try:
    while True:
        # now do whatever you like with the variables
        print(shared_variable1, shared_variable2)
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print("Program terminated.")

