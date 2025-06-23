import sys
sys.path.append('system/lib')

import time
import minescript as m
import re

run = 1
invdict = {}

def is_container_open(): #talán ez a jó
    if m.container_get_items():
        return True

def updateinv():
    global invdict
    inv = m.player_inventory()
    invdict = {}
    pattern_count = re.compile(r"count=(\d+)")
    pattern_slot  = re.compile(r"slot=(\d+)")
    
    for item in inv:
        s = str(item)
        m_count = pattern_count.search(s)
        m_slot = pattern_slot.search(s)
        if m_count and m_slot:
            count = int(m_count.group(1))
            slot = int(m_slot.group(1))
            invdict[slot] = count

def getQuantity(slot):
    updateinv()
    time.sleep(0.1)
    return invdict.get(slot, 0)

updateinv()
while run:
    for i in range(0, 8):
        while getQuantity(i) > 1:
            m.player_inventory_select_slot(i)
            if "a stranger while holding to" in str(m.player_inventory()[i]):
                time.sleep(0.1)
                m.player_press_use(True)
            else:
                print(getQuantity(i))
                m.player_press_drop(True)  

        #if is_container_open():
        #    m.press_key_bind("key.inventory", True)
    
    for i in range(0, 8):
        while getQuantity(i) > 0 and not "a stranger while holding to" in str(m.player_inventory()[i]):
            m.player_press_drop(True)  

    m.chat("/getfromsacks white gift 512")
    time.sleep(0.5)
    updateinv()
    #if getQuantity(0) == 0:
    #    run = 0

print("Finished processing items.", run)