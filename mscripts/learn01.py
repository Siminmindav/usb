import sys
sys.path.append('system/lib')  

import minescript

def build_floor():
    # Get and round player position to integers
    x, y, z = minescript.player_position()
    x, y, z = int(round(x)), int(round(y)), int(round(z))

    # Build a 3x3 floor in front of player
    for dx in range(-2, 2):    # -1, 0, 1
        for dz in range(-2, 2):  # -1, 0, 1
            bx = x + dx
            by = y - 1  # one block below feet
            bz = z + 2 + dz  # a bit in front

            current_block = minescript.getblock(bx, by, bz)
            if current_block != "minecraft:stone":
                minescript.execute(f"setblock {bx} {by} {bz} minecraft:stone replace")

    minescript.echo("3x3 floor placed!")

build_floor()

