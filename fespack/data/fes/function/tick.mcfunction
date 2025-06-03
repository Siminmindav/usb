execute as @a[nbt={SelectedItem:{id:"minecraft:light_gray_dye"}}] at @s run execute as @s at @s run tp @e[ type= !minecraft:player,distance=..10] ^ ^1.3 ^8

execute as @a[nbt={SelectedItem:{id:"minecraft:blue_dye"}}] at @s run execute at @s run setblock ~ ~-1 ~ minecraft:acacia_leaves keep

execute as @a[nbt={SelectedItem:{id:"minecraft:white_dye"}}] at @s run execute at @s run summon minecraft:tnt ^ ^1 ^10

execute as @a[nbt={SelectedItem:{id:"minecraft:red_dye"}}] at @s run execute at @s run fill ^ ^1.5 ^ ^ ^ ^ minecraft:air destroy

execute as @a[nbt={SelectedItem:{id:"minecraft:yellow_dye"}}] at @s run tp @e[type= minecraft:item] @s