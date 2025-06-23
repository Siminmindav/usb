import sys
sys.path.append('system/lib')

import minescript as m

run = 1

invdict = {}


def updateinv():
    
    global invdict
    inv = m.player_inventory()
    invdict = {}
    for item in inv:
        szám = int(list(str(item).split())[1].split("=")[1].strip(','))
        hely = int(list(str(item).split())[3].split("=")[1].strip(','))
        invdict[hely] = szám

def getQuantity(slot):
    """
    Returns the quantity of items in the specified slot.
    If the slot is empty, returns 0.
    """
    updateinv()
    return invdict.get(slot, 0)

def getName(slot):
    """
    Returns the name of the item in the specified slot.
    If the slot is empty, returns an empty string.
    """
    updateinv()
    inv = m.player_inventory()
    for item in inv:
        if int(list(str(item).split())[3].split("=")[1].strip(',')) == slot:
            return str(item).split()[0].split('=')[1]


updateinv()
print(invdict)
for i in range(0, 9):
    print(f"Slot {i}: {getQuantity(i)}")

while run:
    for i in range(0, 9):
        while getQuantity(i) > 0:
            m.player_inventory_select_slot(i)
            if getName(i) == "'minecraft:player_head',":
                m.player_press_use(True)
                m.player_press_use(False)
            else:
                print(getName(i))
                m.player_press_drop(True)  
            
    m.chat("/getfromsacks white gift 504")
    if getQuantity(0) == 0:
        run = 0
