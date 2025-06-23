import sys
sys.path.append('system/lib')  

import time
import re 
import minescript as m

invdict = {}
used_block_count = 0

def updateinv():
    """
    global invdict
    inv = m.player_inventory()
    invdict = {}
    for item in inv:
        szám = int(list(str(item).split())[1].split("=")[1].strip(','))
        hely = int(list(str(item).split())[3].split("=")[1].strip(','))
        invdict[hely] = szám
    """
    """
    Populate invdict with {slot_index: item_count}.
    Safely skips any inventory entries that don't parse correctly.
    """
    global invdict
    invdict.clear()
    pattern_count = re.compile(r"count=(\d+)")
    pattern_slot  = re.compile(r"slot=(\d+)")
    
    for item in m.player_inventory():
        s = str(item)
        m_count = pattern_count.search(s)
        m_slot  = pattern_slot.search(s)
        if not (m_count and m_slot):
            # couldn’t parse this line—skip it
            continue
        
        count = int(m_count.group(1))
        slot  = int(m_slot.group(1))
        invdict[slot] = count

def recursiveuse(slot, n):
    if n <= 0:
        return
    m.player_inventory_select_slot(slot)
    time.sleep(1/20)
    m.player_press_use(True)
    time.sleep(1/20)
    recursiveuse(slot, n-1)
    global used_block_count
    used_block_count += 1

def use(slot):
    m.player_inventory_select_slot(slot)
    time.sleep(1/20)
    m.player_press_use(True)
    time.sleep(1/20)
    global used_block_count
    used_block_count += 1

while True:
    updateinv()

    for slot, count in list(invdict.items()):
        if slot < 8:
            m.player_inventory_select_slot(slot)
            while count:
                use(slot)
                count -= 1
            time.sleep(2/20)
            updateinv()
            print(f"Used slot {slot}, {count} times")

    """
    for x in range(8):
        m.player_inventory_select_slot(x)
        m.player_press_drop(True)
        time.sleep(2/20)
    """
    m.chat("/getfromsacks white gift 512")
    

    updateinv()
    if list(invdict.items()):
        for slot, count in list(invdict.items()):
            if slot < 8:
                continue
            else:
                print("used block count", used_block_count)
                print("Estimated profit", used_block_count * 3421, "coins")    
                break
    else:
        break


