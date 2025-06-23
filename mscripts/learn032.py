import sys
sys.path.append('system/lib')

import time
import minescript as m

invdict = {}

def updateinv():
    """Populate invdict with {slot_index: item_count}."""
    global invdict
    invdict.clear()
    inv = m.player_inventory()
    for item in inv:
        # If the MineScript Item object has attributes, use them:
        try:
            count = item.count
            slot  = item.slot
        except AttributeError:
            # Fallback to parsing if needed:
            parts = str(item).split()
            count = int(parts[1].split("=")[1].rstrip(","))
            slot  = int(parts[3].split("=")[1].rstrip(","))
        invdict[slot] = count

def use_n_times(slot, n):
    """Select `slot`, then `use()` it `n` times with 5‑tick pauses."""
    m.player_inventory_select_slot(slot)
    for _ in range(n):
        m.player_press_use(True)
        time.sleep(5 / 20.0)  # 5 ticks

# 1) Prime the inventory dictionary
updateinv()
print("Initial inventory:", invdict)

# 2) Cycle through each slot and use up all items
for slot, count in list(invdict.items()):
    if count > 0:
        print(f"Using slot {slot} x{count}")
        use_n_times(slot, count)
        # small extra pause to let the server sync
        time.sleep(2 / 20.0)
        updateinv()
        print("Now inventory:", invdict)
