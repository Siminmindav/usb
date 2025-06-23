import sys
sys.path.append('system/lib')  

import random
import minescript as m

sentences = [
    "Sometimes I sing soppy, love songs in the car.",
    "Sometimes I sing soppy love songs in the car.",
    "I sometimes try to say bad things and then this happens :(",
    "Please go easy on me, this is my first game!",
    "Behold, the greatest and powerful, my magnificent and almighty nemesis!",
    "I like to eat pasta, do you prefer nachos?",
    "I heard you like minecraft, so I built a computer so you can minecraft, minecrafting in your minecraft.",
    "When nothing is going right, go left.",
    "Doin a bamboozle fren.",
    "I had something to say, then I forgot it.",
    "I enjoy long walks on the beach and playing Hypixel",
    "Your Clicks per second are godly. :eek:",
    "You are very good at this game friend.",
    "Let's be friends instead of fighting okay?",
    "You are a great person! Do you want to play some Hypixel games with me?",
    "If the world in Minecraft is infinite.. ..how can the sun revolve around it?",
    "When I saw the guy with a potion I knew there was trouble brewing.",
    "Your personality shines brighter than the sun.",
    "Pls give me doggo memes!",
    "Hey Helper, how play game?",
    "In my free time, I like to watch cat videos on youtube",
    "Maybe we can have a rematch?",
    "Blue is greener than purple for sure",
    "Can you paint with all the colors of the wind",
    "I like Minecraft pvp but you are thruly better than me!",
    "I like pineapple on my pizza",
    "Hello everyone! I am an innocent player who loves everything Hypixel.",
    "Pineapple doesn't go on pizza!",
    "I have really enjoyes playing with you! <3",
    "Wait... This isn't what I typed!",
    "I need help, teach me how to play!",
    "Why can't Ender Dragon read a book? Because he always starts at the End.",
    "What happens if I add chocolate milk to macaroni and cheese?",
    "ILY<3",
    "Anybody else really like Rick Astley?"
]



with m.EventQueue() as event_queue:
  event_queue.register_chat_listener()
  while True:
    event = event_queue.get()
    if event.type == m.EventType.CHAT and "ez" in event.message.lower():
        m.chat(random.choice(sentences))
