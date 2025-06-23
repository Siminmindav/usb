import sys
sys.path.append('system/lib')

import random
import time
import minescript as m

"""
keys = ["key.advancements", "key.attack", "key.back ", "key.chat", "key.command", "key.drop", "key.forward", "key.fullscreen", "key.hotbar.1", "key.hotbar.2", "key.hotbar.3", "key.hotbar.4", "key.hotbar.5", "key.hotbar.6", "key.hotbar.7", "key.hotbar.8", "key.hotbar.9", "key.inventory", "key.jump", "key.left", "key.loadToolbarActivator", "key.pickItem", "key.playerlist", "key.right", "key.saveToolbarActivator", "key.screenshot", "key.smoothCamera", "key.sneak", "key.socialInteractions", "key.spectatorOutlines", "key.sprint", "key.swapOffhand", "key.togglePerspective", "key.use"]

print(m.player_name())
print(m.player_position())
print(m.player_hand_items())
print(m.player_inventory())
print(m.player_inventory_slot_to_hotbar(10)) #1.21.4-óta nincs
print(m.player_inventory_select_slot(0))

key = random.choice(keys)
print(f"Selected key: {key}")
print(m.press_key_bind(key, True))
time.sleep(2)  
print(m.press_key_bind(key, False))

for _ in range(40):
    ori = m.player_orientation()[0]%360
    if ori < 180:
        print(round(ori, 2),", ",m.player_orientation()[1])
    else:
        print(round(ori-360, 2),", ",m.player_orientation()[1])
    time.sleep(0.05)

for y in range(20):
    for x in range(100):
        m.player_set_orientation(x/100*360-180, y/20*180-90)

maxdistance = 20
for x in range(5):
    print(m.player_get_targeted_block(maxdistance))
    time.sleep(2)

maxdistance = 20
for x in range(5):
    print(m.player_get_targeted_entity(maxdistance, True))
    time.sleep(2)

print(m.player_health())
print(m.player())
print(m.entities())#ntities(*, nbt: bool = False, uuid: str = None, name: str = None, type: str = None, position: Vector3f = None, offset: Vector3f = None, min_distance: float = None, max_distance: float = None, sort: str = None, limit: int = None)
print(m.world_info())
print(m.getblock(*list(map(round,m.player_position()))))

with m.EventQueue() as event_queue:
  event_queue.register_chat_listener()
  while True:
    event = event_queue.get()
    if event.type == m.EventType.CHAT and "knock knock" in event.message.lower():
      m.echo("Who's there?")
"""
m.player_look_at(0,0,0)



print("Done")