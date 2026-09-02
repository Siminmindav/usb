import math
caption = "Végtelen spirál"
fps = f"Képkockák másodpercenként: "

instructions = [
    "---Irányítások---",
    "Szóköz:                      Új négyzetet hoz létre.",
    "Bal egérgomb:             Elhúzza a középső négyzetet.",
    "Középső egérgomb:     Vált változók között.",
    "Görgő fel:                    Az adott változót növeli.",
    "Görgő le:                     Az adott változót csökkenti.",
    "Jobb egérgomb:          Törli az előzőleg létre hozott négyzetet.",
    "OK"
    ]

variables = [
    "Sebesség: ",
    " fok/képkocka", 
    "Méret: ",
    " px^2",
    "Sugár: ",
    " px",
    "Piros: ",
    " színérték",
    "Zöld: ",
    " színérték",
    "Kék: ",
    " színérték",
    "áttetszés: ",
    " 1bites érték",
    "négyzet: ",
    " bináris",
    "kör: ",
    " bináris",
    "vonal: ",
    " bináris",
    "háttér áttetszése: ",
    " 1bites érték",
    "szög: ",
    " fok",
    "Semmi",
]

developer = [
    "Készítette: Siminmin",
    "GitHub link:",
    "https://github.com/Siminmindav/spinner",
    "",
    "Zene:",
    "szerő - dal",
    "szerő2 - dal2",
    "",
    "Köszönöm, hogy játszottál!",
]

savings = [
    "Kiválasztott fájl:",
    "Nevezd el a fájlt!",
]

trashing = [
    "Mindent kitörölsz?",
]
leaving = [
    "Elhagyod a játékot?",
]

def textgenforaction(base,opacity):
    return [
    f"{variables[0]}{math.floor(base.omega*10)/10}{variables[1]}",
    f"{variables[2]}{math.floor(base.w*10)/10}{variables[3]}",
    f"{variables[4]}{base.r}{variables[5]}",
    f"{variables[6]}{base.color.r}{variables[7]}",
    f"{variables[8]}{base.color.g}{variables[9]}",
    f"{variables[10]}{base.color.b}{variables[11]}",
    f"{variables[12]}{base.color.opacity}{variables[13]}",
    f"{variables[14]}{base.shapes[0]}{variables[15]}",
    f"{variables[16]}{base.shapes[1]}{variables[17]}",
    f"{variables[18]}{base.shapes[2]}{variables[19]}",
    f"{variables[20]}{opacity}{variables[21]}",
    f"{variables[22]}{base.angle}{variables[23]}",
    ]

textlist = [
    ["Válassz ablak méretet", (105, 20), 0],
    ["Pár példa:", (13, 70), 0],
    ["800x800", (20, 120), (13, 114, 90, 35)],
    ["700x700", (20, 170), (13, 164, 90, 35)],
    ["teljes képernyő", (20, 220), (13, 214, 148, 35)],
    ["Írhatsz be méretet", (220, 70), 0],
    ["X                  px", (220,120), (243, 114, 90, 35)],
    ["", (250,120), 0],
    ["Y                  px", (220,170), (243, 164, 90, 35)],
    ["", (250,170), 0],
]