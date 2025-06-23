import sys
sys.path.append('system/lib')

import time
import minescript as m
import re

run = 1
invdict = {}

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
"""
def getName(slot):
    inv = m.player_inventory()
    for item in inv:
        item_str = str(item)

        match_slot = re.search(r"slot=(\d+)", item_str)
        if match_slot and int(match_slot.group(1)) == slot:
            # Look for the custom name in the NBT data
            custom_name_match = re.search(r'"minecraft:custom_name":"[^"]*text\\":\\"([^\\]+)', item_str)
            if custom_name_match:
                return custom_name_match.group(1)
            # Fallback to base item name
            match_item = re.search(r"item=([\w:]+)", item_str)
            if match_item:
                return match_item.group(1)
    return ""
"""

def getQuantity(slot):
    """
    Returns the quantity of items in the specified slot.
    If the slot is empty, returns 0.
    """
    updateinv()
    return invdict.get(slot, 0)

"""
updateinv()
print(invdict)
for i in range(0, 9):
    print(f"Slot {i}: {getQuantity(i)}")
"""
updateinv()
while run:
    for i in range(0, 8):
        while getQuantity(i) > 0:
            m.player_inventory_select_slot(i)
            if "a stranger while holding to" in str(m.player_inventory()[i]):
                m.player_press_use(True)
            else:
                time.sleep(0.1)
                print(getQuantity(i))
                m.player_press_drop(True)  
                time.sleep(0.1)
    
    for i in range(0, 8):
        while getQuantity(i) > 0 and not "a stranger while holding to" in str(m.player_inventory()[i]):
            m.player_press_drop(True)  

    m.chat("/getfromsacks white gift 512")
    updateinv()
    if getQuantity(0) == 0:
        run = 0

print("Finished processing items.", run)