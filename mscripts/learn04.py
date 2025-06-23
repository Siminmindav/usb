import sys
sys.path.append('system/lib')

import minescript as m
import time
import re 

def is_container_open(): #nem müködik
    for item in m.player_inventory():
        if "slot=" in str(item):
            slot = int(re.search(r"slot=(\d+)", str(item)).group(1))
            if slot >= 36:
                return True
    return False

while True: 
    print(m.container_get_items()) #ez igen

    time.sleep(5) 